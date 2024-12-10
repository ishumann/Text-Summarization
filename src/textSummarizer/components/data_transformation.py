import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig
from pathlib import Path

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        try:
            # Convert list of dialogues/summaries to lists of encoded inputs
            input_encodings = self.tokenizer(
                example_batch['dialogue'],  # Pass the list of dialogues
                max_length=1024,
                truncation=True,
                padding="max_length",  # Add padding to handle varying lengths in a batch
            )

            with self.tokenizer.as_target_tokenizer():
                target_encodings = self.tokenizer(
                    example_batch['summary'],  # Pass the list of summaries
                    max_length=128,
                    truncation=True,
                    padding="max_length",  # Add padding to handle varying lengths in a batch
                )

            return {
                'input_ids': input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }

        except Exception as e:
            raise e

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(
            self.convert_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(
            self.config.root_dir, "samsum_dataset"))
