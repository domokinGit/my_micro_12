import opentracing

from models import User
import schemas
import uuid

from opentracing_instrumentation.request_context import get_current_span, span_in_context


async def get_all_users() -> list[User]:
    tracer = opentracing.global_tracer()
    with tracer.start_span("get_users_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            return User.objects


async def create_user(user: schemas.PostUser) -> User:
    tracer = opentracing.global_tracer()
    with tracer.start_span("create_user_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            new_user = User(
                user_id=uuid.uuid4(),
                name=user.name,
                email=user.email,
                password=user.password,
            ).save()
            return new_user


async def delete_user(user_id):
    tracer = opentracing.global_tracer()
    with tracer.start_span("delete_user_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            for user in User.objects:
                if user.user_id == user_id:
                    user.delete()
                    return


async def update_user(user_id, user_post: schemas.PostUser) -> User:
    tracer = opentracing.global_tracer()
    with tracer.start_span("update_users_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            for user in User.objects:
                if user.user_id == user_id:
                    user.name = user_post.name
                    user.email = user_post.email
                    user.password = user_post.password
                    user.save()
                    return user
