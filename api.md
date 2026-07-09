# Task Management REST API Documentation

## Base URL

```
http://127.0.0.1:5000
```

---

# Authentication

## Register User

**Endpoint**

```
POST /api/auth/register
```

### Request Body

```json
{
    "username": "john",
    "email": "john@example.com",
    "password": "123456"
}
```

### Success Response

```json
{
    "message": "User registered successfully"
}
```

---

## Login User

**Endpoint**

```
POST /api/auth/login
```

### Request Body

```json
{
    "email": "john@example.com",
    "password": "123456"
}
```

### Success Response

```json
{
    "access_token": "<JWT Token>"
}
```

---

# Tasks

## Create Task

**Endpoint**

```
POST /api/tasks/
```

### Authorization

Bearer Token Required

### Request Body

```json
{
    "title": "Complete API",
    "description": "Finish Week 9",
    "status": "Pending",
    "priority": "High"
}
```

### Response

```json
{
    "message": "Task created successfully"
}
```

---

## Get Tasks

**Endpoint**

```
GET /api/tasks/
```

### Authorization

Bearer Token Required

### Response

```json
[
    {
        "id": 1,
        "title": "Complete API",
        "description": "Finish Week 9",
        "status": "Pending",
        "priority": "High"
    }
]
```

---

## Update Task

**Endpoint**

```
PUT /api/tasks/<task_id>
```

### Authorization

Bearer Token Required

### Request Body

```json
{
    "title": "Updated Task",
    "status": "Completed"
}
```

### Response

```json
{
    "message": "Task updated successfully"
}
```

---

## Delete Task

**Endpoint**

```
DELETE /api/tasks/<task_id>
```

### Authorization

Bearer Token Required

### Response

```json
{
    "message": "Task deleted successfully"
}
```