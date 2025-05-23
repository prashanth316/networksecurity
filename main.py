from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
if __name__=="__main__":
    try:
        train=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(train)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Enter")
        artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed ")
        data_validation_config=DataValidationConfig(train)
        data_validation=DataValidation(artifact,data_validation_config)
        logging.info("Intitate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(train)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifacts=data_transformation.initiate_data_transformation()
        print(data_transformation_artifacts)

        model_trainer_config=ModelTrainerConfig(train)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifacts)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
    except Exception as e:
        raise NetworkSecurityException