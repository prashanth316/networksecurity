from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
if __name__=="__main__":
    try:
        train=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(train)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Enter")
        artifact=data_ingestion.initiate_data_ingestion()
        print(artifact)
    except Exception as e:
        raise NetworkSecurityException