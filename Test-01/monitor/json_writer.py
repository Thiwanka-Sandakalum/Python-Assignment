import json
import os
from datetime import datetime
from config import OUTPUT_DIR, TIMEZONE

class JSONWriter:
    @staticmethod
    def ensure_output_directory():
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    @staticmethod
    def generate_timestamp():
        return datetime.now(TIMEZONE).isoformat()

    @staticmethod
    def sanitize_timestamp(ts: str) -> str:
        return ts.replace(":", "-")

    @staticmethod
    def write_json(service_name: str, payload: dict):
        JSONWriter.ensure_output_directory()
        timestamp = JSONWriter.sanitize_timestamp(payload["@timestamp"])
        filename = f"{service_name}-status-{timestamp}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w") as f:
            json.dump(payload, f, indent=4)
        return filepath
