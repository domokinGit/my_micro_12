import opentracing

import schemas
import models

from opentracing_instrumentation.request_context import get_current_span, span_in_context


def mapping_model_schema(model: models.Product):
    tracer = opentracing.global_tracer()
    with tracer.start_span("mapping_model_schema_menu", child_of=get_current_span()) as span:
        with span_in_context(span):
            schema = schemas.Product(
                product_id=model.product_id,
                product=model.product,
                price=model.price,
            )
            return schema


def mapping_schema_model(schema: schemas.Product):
    model = schemas.Product(
        product_id=schema.product_id,
        product=schema.product,
        price=schema.price,
    )
    return model
