import hashlib
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def single_user(db) -> User:
    return User.objects.create_user(email="test@test.com", password="this_is_not_a_password")


def test_create_superuser(db):
    user = User.objects.create_superuser(email="test@test.com", password="this_is_not_a_password")
    assert user.is_superuser is True
    assert user.is_active is True
    assert isinstance(user, User)


def test_create_user(db):
    user = User.objects.create_user(email="test@test.com", password="this_is_not_a_password")
    assert user.is_superuser is False
    assert user.is_active is True
    assert isinstance(user, User)


def test_user_hash(db, single_user):
    user = User.objects.get(email="test@test.com")
    assert user.hash == hashlib.sha256("{email}-{date_joined}-{salt}".format(
        email=user.email,
        date_joined=user.date_joined,
        salt=user.salt
    ).encode()).hexdigest()
