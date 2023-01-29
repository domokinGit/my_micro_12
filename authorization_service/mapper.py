import opentracing

import schemas
import models

from opentracing_instrumentation.request_context import get_current_span, span_in_context


def mapping_model_schema(model: models.User):
    tracer = opentracing.global_tracer()
    with tracer.start_span("mapping_model_schema_users", child_of=get_current_span()) as span:
        with span_in_context(span):
            schema = schemas.User(
                user_id=model.user_id,
                name=model.name,
                email=model.email,
                password=model.password,
            )
            return schema


def mapping_schema_model(schema: schemas.User):
    model = schemas.User(
        user_id=schema.user_id,
        name=schema.name,
        email=schema.email,
        password=schema.password,
    )
    return model
