# MarkFlow - Online Markdown Editor API

A Django REST API for managing Markdown documents with tagging support.

## Setup Instructions

1. Clone the repository
2. Build and run with Docker:
```bash
docker compose up --build
```

## API Documentation

### Authentication

#### Get JWT Token
- **POST** `/api/token/`
- **Payload**: 
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
- **Response**: JWT access and refresh tokens

#### Refresh Token
- **POST** `/api/token/refresh/`
- **Payload**:
```json
{
    "refresh": "your_refresh_token"
}
```

### Documents

#### List/Create Documents
- **GET** `/api/documents/`
  - Query Parameters:
    - `ordering`: created, -created, updated, -updated
    - `tags`: Filter by tag ID
- **POST** `/api/documents/`
  - Payload:
```json
{
    "title": "My Document",
    "content": "# Markdown Content",
    "tags": [{"name": "work"}, {"name": "important"}]
}
```

#### Retrieve/Update/Delete Document
- **GET** `/api/documents/<id>/`
- **PATCH** `/api/documents/<id>/`
  - Payload: Same as POST, fields optional
- **DELETE** `/api/documents/<id>/`

### Tags

#### List/Create Tags
- **GET** `/api/tags/`
- **POST** `/api/tags/`
  - Payload:
```json
{
    "name": "work"
}
```

## Authentication

All endpoints except token generation require JWT authentication.
Add the following header to your requests:
```
Authorization: Bearer <your_access_token>
``` 