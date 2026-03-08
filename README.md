# API-Creation

Learning how to build REST APIs using **Python Flask** and test them using **Postman**.

This project demonstrates basic API concepts such as:

* Creating a Flask server
* Building API routes (endpoints)
* Using **path parameters**
* Using **query parameters**
* Handling **POST requests**
* Returning **JSON responses**
* Testing APIs with **Postman**

---

# Tech Stack

* Python
* Flask
* Postman

---

# Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/S-kipper/API-Creation.git
cd API-Creation
```

### 2. Install dependencies

```bash
pip install flask
```

### 3. Run the server

```bash
python main.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

# API Endpoints

## 1. Get User

Returns user information using a **path parameter**.

**Endpoint**

```
GET /get-user/<user_id>
```

Example request:

```
http://127.0.0.1:5000/get-user/10
```

Example response:

```json
{
  "user_id": "10",
  "name": "Aditya",
  "email": "adi@example.com"
}
```

### Optional Query Parameter

You can add extra information using query parameters.

Example:

```
http://127.0.0.1:5000/get-user/10?extra=developer
```

Response:

```json
{
  "user_id": "10",
  "name": "Aditya",
  "email": "adi@example.com",
  "extra": "developer"
}
```

---

## 2. Create User

Creates a user using a **POST request**.

**Endpoint**

```
POST /create-user
```

Example JSON Body:

```json
{
  "name": "Aditya",
  "email": "adi@example.com"
}
```

Example Response:

```json
{
  "name": "Aditya",
  "email": "adi@example.com"
}
```

Status Code:

```
201 Created
```

---

# Testing the API

The API was tested using **Postman**.

Steps:

1. Open Postman
2. Select the request type (**GET or POST**)
3. Enter the API URL
4. Send the request
5. View the JSON response

---

# Future Improvements

* Add input validation
* Connect to a database
* Add PUT and DELETE endpoints
* Implement authentication

