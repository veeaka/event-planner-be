import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from users.models import User

pytestmark = (
    pytest.mark.django_db
)  # Ensures tests run in a transactional database environment


@pytest.fixture
def api_client():
    """Fixture to create an API client for tests."""
    return APIClient()


@pytest.fixture
def create_user():
    """Fixture to create a user for login tests."""
    user = User.objects.create_user(
        email="testuser@example.com", password="securepassword", name="Test User"
    )
    return user


class TestSignupView:
    def test_signup_successful(self, api_client):
        """Test user signup with valid data."""
        data = {
            "email": "newuser@example.com",
            "password": "newsecurepassword",
            "name": "New User",
        }
        response = api_client.post("/register/", data)
        assert response.status_code == 201
        assert response.data["message"] == "Signup successful"
        assert "token" in response.data

        # Verify user is created in the database
        user = User.objects.get(email=data["email"])
        assert user is not None
        assert user.name == data["name"]

    def test_signup_existing_email(self, api_client, create_user):
        """Test user signup with an already existing email."""
        data = {
            "email": "testuser@example.com",  # Already exists
            "password": "newsecurepassword",
            "name": "Test User",
        }
        response = api_client.post("/register/", data)
        assert response.status_code == 400
        assert "email" in response.data  # Validation error for duplicate email


class TestLoginView:
    def test_login_successful(self, api_client, create_user):
        """Test user login with valid credentials."""
        data = {
            "email": "testuser@example.com",
            "password": "securepassword",
        }
        response = api_client.post("/login/", data)
        assert response.status_code == 200
        assert response.data["message"] == "Login successful"
        assert response.data["email"] == create_user.email
        assert "token" in response.data

        # Verify token is created
        token = Token.objects.get(user=create_user)
        assert response.data["token"] == token.key

    def test_login_invalid_credentials(self, api_client, create_user):
        """Test user login with invalid credentials."""
        data = {
            "email": "testuser@example.com",
            "password": "wrongpassword",
        }
        response = api_client.post("/login/", data)
        assert response.status_code == 400
        assert response.data["error"] == "Invalid email or password"

    def test_login_nonexistent_user(self, api_client):
        """Test user login with a non-existent user."""
        data = {
            "email": "nonexistent@example.com",
            "password": "randompassword",
        }
        response = api_client.post("/login/", data)
        assert response.status_code == 400
        assert response.data["error"] == "Invalid email or password"
