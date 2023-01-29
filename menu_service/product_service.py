import opentracing

from models import Product
import schemas
import uuid

from opentracing_instrumentation.request_context import get_current_span, span_in_context


async def get_all_products() -> list[Product]:
    tracer = opentracing.global_tracer()
    with tracer.start_span("get_products_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            return Product.objects


async def create_product(product: schemas.PostProduct) -> Product:
    tracer = opentracing.global_tracer()
    with tracer.start_span("create_product_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            new_product = Product(
                product_id=uuid.uuid4(),
                product=product.product,
                price=product.price,
            ).save()
            return new_product


async def delete_product(product_id):
    tracer = opentracing.global_tracer()
    with tracer.start_span("delete_product_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            for product in Product.objects:
                if product.product_id == product_id:
                    product.delete()
                    return
