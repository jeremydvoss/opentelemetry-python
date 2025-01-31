import logging
from os import environ

from opentelemetry import trace
from opentelemetry._logs import set_logger_provider
# from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
#     OTLPLogExporter,
# )
from opentelemetry.sdk._logs.export import ConsoleLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource


logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "shoppingcart",
            "service.instance.id": "instance-12",
        }
    ),
)
set_logger_provider(logger_provider)

exporter = ConsoleLogExporter()
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(logger_provider=logger_provider)

# Attach OTLP handler to root logger
logging.getLogger().addHandler(handler)

# Create different namespaced loggers
# It is recommended to not use the root logger with OTLP handler
# so telemetry is collected only for the application
logger1 = logging.getLogger("myapp.area1")
logger2 = logging.getLogger("myapp.area2")

logger1.debug("logger 1 debug")
logger1.info("logger 1 info")
logger2.warning("logger 2 warning")
logger2.error("logger 2 error")


# Trace context correlation
tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("foo"):
    # Do something
    logger2.error("logger 2 error in span")

logger_provider.shutdown()
