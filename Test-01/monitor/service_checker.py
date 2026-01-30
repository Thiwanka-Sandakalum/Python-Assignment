import subprocess

class ServiceChecker:
    @staticmethod
    def check_service(service_name: str) -> str:
        """
        Checks the status of a Linux service using systemctl.
        Returns 'UP' or 'DOWN'
        """
        try:
            result = subprocess.run(
                ["systemctl", "is-active", service_name],
                capture_output=True,
                text=True
            )
            if result.stdout.strip() == "active":
                return "UP"
            else:
                return "DOWN"
        except Exception:
            return "DOWN"
