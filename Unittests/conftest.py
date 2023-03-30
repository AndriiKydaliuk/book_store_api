"""
conftest for unit tests
"""
from unittest import mock
from unittest.mock import mock_open

from services.user_service import UserService
from schemas.schemas import UserSchema
from data_access_objects.user_dao import UserDao

import pytest


@pytest.fixture
def user_dao_fetch_by_id_200():
    """user_dao_fetch_by_id_200"""
    with mock.patch.object(UserDao, 'fetch_by_id', return_value=1) as user_dao_get_user_ok:
        yield user_dao_get_user_ok
