from abc import ABC, abstractmethod

class IElasticService(ABC):
    @abstractmethod
    def create_index_if_not_exists(self):
        pass

    @abstractmethod
    def index_document(self, payload: dict):
        pass

    @abstractmethod
    def get_latest_service(self, service_name: str):
        pass

    @abstractmethod
    def get_all_latest(self):
        pass