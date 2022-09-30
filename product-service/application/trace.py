from base64 import b64encode
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource as OTLResource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

from application.base import app
from application.database import db

# auth_info = f"{app.config['OTLP_ENDPOINT_USER']}:{app.config['OTLP_ENDPOINT_PASSWORD']}"
# message_bytes = auth_info.encode("ascii")
# userAndPass = b64encode(message_bytes).decode("ascii")
# headers = {'Authorization': 'Basic %s' % userAndPass}
# otlp_exporter = OTLPSpanExporter(endpoint=f"{app.config['OTLP_ENDPOINT']}",
#                                  headers=headers)

otlp_exporter = OTLPSpanExporter(endpoint=f"{app.config['OTLP_ENDPOINT']}")

# Implement OTLP Tracing
resource = OTLResource(attributes={"service.name": "product-service"})
tracer = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer)

span_processor = BatchSpanProcessor(otlp_exporter)
tracer.add_span_processor(span_processor)

LoggingInstrumentor().instrument(set_logging_format=True)

# Initialize `Instrumentor` for the `requests` library
RequestsInstrumentor().instrument()
# Initialize `Instrumentor` for the `flask` web framework
FlaskInstrumentor().instrument_app(app)
# Initialize `Instrumentor` for the `SQLAlchemy` library
SQLAlchemyInstrumentor().instrument(engine=db.engine)