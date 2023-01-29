import uuid

import opentracing
from fastapi import APIRouter, status

import mapper
import product_service
from schemas import Product, PostProduct
from opentracing_instrumentation.request_context import get_current_span, span_in_context


router = APIRouter(
    tags=['Menu'],
    prefix='/menu',
)


@router.get('/', status_code=200, response_model=list[Product])
async def get_product():
    tracer = opentracing.global_tracer()
    with tracer.start_span("get_product_request", child_of=get_current_span()) as span:
        with span_in_context(span):
            products = await product_service.get_all_products()
            result = [
                mapper.mapping_model_schema(product)
                for product in products
            ]
            return result


@router.post('/add', status_code=201, response_model=Product)
async def add_product(post_product: PostProduct):
    tracer = opentracing.global_tracer()
    with tracer.start_span("add_product_request", child_of=get_current_span()) as span:
        with span_in_context(span):
            new_product = await product_service.create_product(post_product)
            return mapper.mapping_model_schema(new_product)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: uuid.UUID):
    tracer = opentracing.global_tracer()
    with tracer.start_span("delete_product_request", child_of=get_current_span()) as span:
        with span_in_context(span):
            await product_service.delete_product(product_id)
            return
