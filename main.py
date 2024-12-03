from textSummarizer.pipeline.stage_01_data_ingestion  import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import  DataValdationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import  DataTransformationTrainingPipeline
from textSummarizer.logging import logger



# STAGE_NAME = "Date Ingestion stage"

# try:
#     logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e




# STAGE_NAME = "Date Validation stage"

# try:
#     logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
#     data_validation = DataValdationTrainingPipeline()
#     data_validation.main()
#     logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "Date Transformation stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_tranformation = DataTransformationTrainingPipeline()
    data_tranformation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e