from textSummarizer.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx========X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx========X")
except Exception as e:
    logger.exception(e)
    raise e
