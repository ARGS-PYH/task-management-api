# 📌 Task Management API – Documentation

This API allows users to manage their tasks. Users must create an account and log in before they can manage tasks.

---

## 🔹 Base URL
```
http://127.0.0.1:8000/api/
```

---

## 🔹 Authentication
- Use Django REST Framework login at:
  ```
  http://127.0.0.1:8000/api-auth/login/
  ```
- You must be logged in to view or manage tasks.
- New users can register without logging in first.

---

## 🔹 Endpoints

### 👤 User Endpoints
| Method | Endpoint              | Description              |
|--------|------------------------|--------------------------|
| POST   | /users/create/       | Register a new user      |
| GET    | /users/              | List all users (auth required) |
| GET    | /users/<id>/         | Get details of one user (auth required) |

---

### ✅ Task Endpoints
| Method | Endpoint                  | Description                    |
|--------|----------------------------|--------------------------------|
| GET    | /tasks/                  | List all tasks of logged-in user |
| POST   | /tasks/                  | Create a new task              |
| GET    | /tasks/<id>/             | Get details of one task        |
| PUT    | /tasks/<id>/             | Update a task                  |
| DELETE | /tasks/<id>/             | Delete a task                  |
| PATCH  | /tasks/<id>/complete/    | Mark task as complete          |
| PATCH  | /tasks/<id>/incomplete/  | Mark task as incomplete        |

---

### 🔎 Filtering and Sorting

You can filter tasks:
```
/tasks/?status=Completed
/tasks/?priority=High
/tasks/?due_date=2025-09-15
```

You can sort tasks:
```
/tasks/?ordering=due_date
/tasks/?ordering=-priority
```
(- means descending order)

---

## 🔹 Task Model Fields
Each task has these fields:
- **title** (string, required)
- **description** (string, optional)
- **due_date** (date, required, must be in future)
- **priority** (Low, Medium, High)
- **status** (Pending, Completed)
- **completed_at** (date-time when task was completed)

---

