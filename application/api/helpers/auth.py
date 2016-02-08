from application.accounts.models import User
from django.contrib.auth.backends import RemoteUserBackend

from rest_framework.views import exception_handler
from super.settings.base import DEFAULT_USER, DEFAULT_PASS


class MyRemoteUserBackend (RemoteUserBackend):
    # Create a User object if not already in the database?
    create_unknown_user = False

    def get_user (self, user_id):
        #somehow_create_an_instance_of (MyUser, user_id)
        user = User()
        return user

    def authenticate (self, **credentials):
        user = User() if credentials.get('password') == DEFAULT_PASS and credentials.get('username') == DEFAULT_USER\
            else None
        return user


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    try:
        print(response.data.pop('detail'))
    except KeyError:
        pass
    if response is not None:
        response.data['error_code'] = response.status_code
        response.data['error_msg'] = response.status_text
        response.data['success'] = False

    return response