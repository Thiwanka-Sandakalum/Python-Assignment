import socket
from service_checker import ServiceChecker
from app_evaluator import ApplicationEvaluator
from json_writer import JSONWriter
from config import APPLICATION_NAME, SERVICES
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_payload(service_name, service_status, hostname, timestamp):
    return {
        "application_name": APPLICATION_NAME,
        "service_name": service_name,
        "service_status": service_status,
        "host_name": hostname,
        "@timestamp": timestamp
    }

def run_monitor():
    hostname = socket.gethostname()
    timestamp = JSONWriter.generate_timestamp()
    service_statuses = {}
    logger.info("Starting service monitoring...")
    # Check each service
    for service in SERVICES:
        status = ServiceChecker.check_service(service)
        service_statuses[service] = status
        logger.info(f"{service} status: {status}")
        payload = build_payload(service, status, hostname, timestamp)
        filepath = JSONWriter.write_json(service, payload)
        logger.info(f"Written JSON file: {filepath}")
    # Evaluate application status
    app_status = ApplicationEvaluator.evaluate(service_statuses)
    logger.info(f"Application {APPLICATION_NAME} status: {app_status}")
    # write application-level JSON
    app_payload = {
        "application_name": APPLICATION_NAME,
        "application_status": app_status,
        "host_name": hostname,
        "@timestamp": timestamp
    }
    JSONWriter.write_json(APPLICATION_NAME, app_payload)
    logger.info("Monitoring completed successfully.")

if __name__ == "__main__":
    run_monitor()
