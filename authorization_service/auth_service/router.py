import opentracing
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from opentracing_instrumentation.request_context import get_current_span, span_in_context
from auth_service.service import login_user

router = APIRouter(
    tags=['auth_service']
)


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), ):
    tracer = opentracing.global_tracer()
    with tracer.start_span("login_user_method", child_of=get_current_span()) as span:
        with span_in_context(span):
            token = await login_user(request)
            return token
