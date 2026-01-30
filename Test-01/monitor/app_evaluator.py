class ApplicationEvaluator:
    @staticmethod
    def evaluate(service_statuses: dict) -> str:
        """
        If any service is DOWN → application is DOWN
        Else → UP
        """
        if any(status == "DOWN" for status in service_statuses.values()):
            return "DOWN"
        return "UP"
