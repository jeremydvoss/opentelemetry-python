import logging
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler

logging.basicConfig(
    level=logging.WARNING
)
root_logger = logging.getLogger()
handler = LoggingHandler()
root_logger.addHandler(handler)
print(logging.WARNING)
print(root_logger.level)
print(root_logger.handlers[0].level)
print(handler.level)