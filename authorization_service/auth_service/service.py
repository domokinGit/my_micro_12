import opentracing
from fastapi import HTTPException
from starlette import status

from auth_service.jwt import create_access_token
from models import User

from opentracing_instrumentation.request_context import get_current_span, span_in_context


async def login_user(request):
    tracer = opentracing.global_tracer()
    with tracer.start_span("login_user_response", child_of=get_current_span()) as span:
        with span_in_context(span):
            sign_user: User
            for user in User.objects:
                if user.password == request.password:
                    sign_user = user
            if sign_user is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

            if sign_user.password != request.password:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

            access_token = create_access_token(data={"email": sign_user.email})

            return {"access_token": access_token, "token_type": "bearer"}
