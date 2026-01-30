import logging
import sys

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = getattr(record, 'request_id', '-')
        return True

LOG_LEVEL = "INFO"

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s [%(request_id)s] %(message)s"
)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
handler.addFilter(RequestIdFilter())

logger = logging.getLogger("rbcapp-api")
logger.setLevel(LOG_LEVEL)
logger.handlers = [handler]
logger.propagate = False
