
# User Authentication API

This is a robust User Authentication API built using Django and Django REST Framework. It allows for user registration, login, profile retrieval, password reset functionality, and includes features such as JWT authentication for secure communication.

## Features

- **User Registration**: Allows users to register by providing their email, name, and password.
- **Login & Authentication**: Uses JWT (JSON Web Token) for secure login and session management.
- **Profile Management**: Users can retrieve their profile details after successful authentication.
- **Password Reset**: Allows users to reset their password through a token-based email verification system.
- **Rate Limiting**: Implements rate limiting for login attempts to prevent brute force attacks.

## Technologies Used

- **Django**: Backend framework for building the API.
- **Django REST Framework**: Toolkit for building Web APIs.
- **Django Simple JWT**: JWT authentication for secure login and token management.
- **Django Ratelimit**: Rate limiting for login API to prevent abuse.
- **SQLite/PostgreSQL**: Database for storing user data (choose based on your environment).
- **Python 3.x**: Programming language used.

## Installation

### Prerequisites

- Python 3.x installed.
- Virtual environment (recommended).
- Django 3.x or later.
- Django REST Framework.
- Django Simple JWT.

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate into your project directory**:
    ```bash
    cd your-repository
    ```

3. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

The API should now be running at `http://127.0.0.1:8000`.

## API Endpoints

### 1. **User Registration**

- **URL**: `/register/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "email": "user@example.com",
        "password": "StrongPassword123!",
        "name": "John Doe"
    }
    ```
- **Response**:
    ```json
    {
        "message": "User created successfully"
    }
    ```

### 2. **User Login**

- **URL**: `/login/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "email": "user@example.com",
        "password": "StrongPassword123!"
    }
    ```
- **Response**:
    ```json
    {
        "access": "JWT-ACCESS-TOKEN",
        "refresh": "JWT-REFRESH-TOKEN"
    }
    ```

### 3. **User Profile**

- **URL**: `/profile/`
- **Method**: `GET`
- **Authentication**: Bearer token required in the Authorization header.
- **Response**:
    ```json
    {
        "id": 1,
        "email": "user@example.com",
        "name": "John Doe"
    }
    ```

### 4. **Password Reset Request**

- **URL**: `/reset_request/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "email": "user@example.com"
    }
    ```
- **Response**:
    ```json
    {
        "message": "Password reset link sent"
    }
    ```

### 5. **Password Reset Confirmation**

- **URL**: `/reset_confirm/{uid}/{token}/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "password": "NewPassword123!"
    }
    ```
- **Response**:
    ```json
    {
        "message": "Password has been reset successfully"
    }
    ```

## Running Tests

To run the test suite for the project, use the following command:

```bash
python manage.py test


/project-structure
  ├── /drf
  │    ├── /migrations
  │    ├── /serializers.py
  │    ├── /views.py
  │    ├── /urls.py
  │    ├── /tests.py
  ├── /drf
  │    ├── /settings.py
  │    ├── /urls.py
  ├── requirements.txt
  ├── manage.py
  ├── README.md


Contributing
We welcome contributions! If you'd like to contribute to this project, please follow these steps:

Fork this repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.


License
This project is licensed under the MIT License - see the LICENSE file for details.
