import uuid

import opentracing
from fastapi import APIRouter, status

import mapper
import user_service
from schemas import User, PostUser
from opentracing_instrumentation.request_context import get_current_span, span_in_context

router = APIRouter(
    tags=['User'],
    prefix='/users',
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[User])
async def get_all_users():
    tracer = opentracing.global_tracer()
    with tracer.start_span("get_users_request", child_of=get_current_span()) as span:
        with span_in_context(span):
            users = await user_service.get_all_users()
            result = [
                mapper.mapping_model_schema(user)
                for user in users
            ]
            return result


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=User)
async def add_new_user(user: PostUser):
    tracer = opentracing.global_tracer()
    with tracer.start_span("add_user_request", child_of=get_current_span()) as span:
        with span_in_context(span):
            new_user = await user_service.create_user(user)
            return mapper.mapping_model_schema(new_user)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: uuid.UUID):
    tracer = opentracing.global_tracer()
    with tracer.start_span("delete_user_request", child_of=get_current_span()) as span:
        with span_in_context(span):
            await user_service.delete_user(user_id)
            return


@router.put('/{user_id}', status_code=status.HTTP_202_ACCEPTED, response_model=User)
async def update_user(user_id: uuid.UUID, user_post: PostUser):
    tracer = opentracing.global_tracer()
    with tracer.start_span("update_user_request", child_of=get_current_span()) as span:
        with span_in_context(span):
            upd_user = await user_service.update_user(user_id, user_post)
            result = mapper.mapping_model_schema(upd_user)
            return result

