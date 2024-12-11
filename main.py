from textSummarizer.pipeline.stage_01_data_ingestion  import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import  DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import  DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_pipeline import ModelTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation_pipeline import ModelEvaluationPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Date Ingestion"


try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Date Validation"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Date Transformation"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e