from textSummarizer.pipeline.stage_01_data_ingestion  import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import  DataValdationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import  DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_pipeline import ModelTrainingPipeline
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
    data_validation = DataValdationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Date Transformation"

try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_tranformation = DataTransformationTrainingPipeline()
    data_tranformation.main()
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