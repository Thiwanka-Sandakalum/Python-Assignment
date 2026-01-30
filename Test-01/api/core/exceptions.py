class ServiceNotFoundException(Exception):
    def __init__(self, service_name: str):
        self.service_name = service_name
