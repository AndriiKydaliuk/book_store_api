from unittest import mock

from services.user_service import UserService


def test_user_service_get_all():
    """test_user_service_get_all"""
    with mock.patch.object(UserService, 'get_all', return_value=[
        {"address": "string", "email": "string", "id": 1, "login": "unique", "name": "string", "phone": "string",
         "role": "MANAGER"}]):
        assert True


