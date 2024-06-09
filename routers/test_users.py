
from fastapi.testclient import TestClient
from routers.users import is_valid_email

from main import app

client = TestClient(app)

def test_create_user_with_form_data_success():
    response = client.post(
        "/users/create-user-formdata",
        data={"username": "test_user", "email": "test@example.com"},
    )
    assert response.status_code == 200
    assert response.json() == {"username": "test_user", "email": "test@example.com"}

def test_create_user_with_form_data_missing_username():
    response = client.post(
        "/users/create-user-formdata",
        data={"email": "test@example.com"},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "username"],
                "msg": "Field required",
                "type": "missing",
                "input": None
            }
        ]
    }

def test_create_user_with_form_data_missing_email():
    response = client.post(
        "/users/create-user-formdata",
        data={"username": "test_user"},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "email"],
                "msg": "Field required",
                "type": "missing",
                "input":None
            }
        ]
    }

def test_create_user_with_form_data_invalid_email():
    response = client.post(
        "/users/create-user-formdata",
        data={"username": "test_user", "email": "invalid_email"},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Invalid email"
    }



def test_is_valid_email():
    """
    Tests the `is_valid_email` function with various email addresses.
    """

    assert is_valid_email("test@example.com") == True
    assert is_valid_email("test.user@example.com") == True
    assert is_valid_email("test_user@example.co.uk") == True
    assert is_valid_email("test-user@example.net") == True
    assert is_valid_email("test.user+alias@example.com") == True

    assert is_valid_email("invalid_email") == False
    assert is_valid_email("test@example") == False
    assert is_valid_email("test@example.") == False
    assert is_valid_email("test@example.c") == False
    