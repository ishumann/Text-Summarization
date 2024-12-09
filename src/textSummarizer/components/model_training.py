from transformers import DataCollatorForSeq2Seq, TrainingArguments, Trainer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
from textSummarizer.entity import ModelTrainerConfig

from dataclasses import dataclass
from pathlib import Path


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        """
        Trains the sequence-to-sequence model using the specified configuration.
        This method sets up the device (CPU or GPU), loads the tokenizer and model,
        prepares the data collator, loads the dataset, and configures the training
        arguments before starting the training process.
        Attributes:
            device (str): The device to use for training ('cuda' if GPU is available, otherwise 'cpu').
            tokenizer (AutoTokenizer): The tokenizer loaded from the specified model checkpoint.
            model_pegasus (AutoModelForSeq2SeqLM): The sequence-to-sequence model loaded from the specified model checkpoint.
            seq2seq_data_collator (DataCollatorForSeq2Seq): The data collator for sequence-to-sequence tasks.
            dataset_samsum_pt (Dataset): The dataset loaded from the specified data path.
            trainer_args (TrainingArguments): The training arguments configured with the specified parameters.
        Returns:
            None
        """
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(
            tokenizer, model=model_pegasus)
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # trainer_args = TrainingArguments(
        #     output_dir="pegasus-samsum",
        #     num_train_epochs=1,
        #     warmup_steps=500,
        #     per_device_train_batch_size=1,
        #     per_device_eval_batch_size=1,
        #     weight_decay=0.01,
        #     logging_steps=10,
        #     evaluation_strategy='steps',
        #     eval_steps=500,
        #     save_steps=1e6,
        #     gradient_accumulation_steps=16)

        trainer_args = trainerArguments(
                output_dir=self.config.root_dir,
                num_train_epochs=self.config.num_train_epochs,
                warmup_steps=self.config.warmup_steps,
                per_device_train_batch_size=self.config.per_device_train_batch_size,
                per_device_eval_batch_size=self.config.per_device_eval_batch_size,
                weight_decay=self.config.weight_decay,
                logging_steps=self.config.logging_steps,
                evaluation_strategy=self.config.evaluation_strategy,
                eval_steps=self.config.eval_steps,
                save_steps=self.config.save_steps,
                gradient_accumulation_steps=self.config.gradient_accumulation_steps)

        trainer = Trainer(model=model_pegasus,
                          args=trainer_args,
                          tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                          train_dataset=dataset_samsum_pt["test"],
                          # use train when training, here testing just code testing purpose
                          eval_dataset=dataset_samsum_pt['validation'])

        trainer.train()

        model_pegasus.save_pretrainer(os.path.join(
            self.config.root_dir, "pegaus-samsum-model"))
        tokenizer.save_pretrainer(os.path.join(
            self.config.root_dir, 'tokenizer'))
