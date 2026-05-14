# **API Endpoints Flash**

A robust, modular, and production-ready sample RESTful API built with **FastAPI**.

This repository demonstrates best practices in designing Python backend applications. It utilizes a layered architecture (Routers → Controllers → Services → Models) to ensure strict separation of concerns, making the codebase highly scalable, testable, and easy to maintain.

## **Table of Contents**

* [Features](#bookmark=id.hh6q2uq6i4wf)  
* [Architecture](#bookmark=id.tyxhjt7d3ek0)  
* [Project Structure](#bookmark=id.t34k6ocv7dy5)  
* [Getting Started](#bookmark=id.k6b5fiz72bm)  
  * [Prerequisites](#bookmark=id.wvstixvqq9ap)  
  * [Installation](#bookmark=id.76frgvbb9s9f)  
  * [Running the Server](#bookmark=id.3lhcka1q1c8)  
* [API Documentation](#bookmark=id.g0b5rpcbjowe)  
* [Endpoints Overview](#bookmark=id.lsbbehph40xe)

## **Features**

* **Health Check**: Server heartbeat, uptime tracking, and UTC timestamping.  
* **Echo Service**: Payload reflection for testing client-server communication.  
* **Math Engine**: Dynamic simple arithmetic operation handling (Add, Subtract, Multiply, Divide) with strict zero-division validation.  
* **User Management (CRUD)**: Fully functional user registry (Create, Read, Update, Delete) utilizing an in-memory data store.  
* **Data Validation**: Strict payload and query parameter validation powered by Pydantic V2.  
* **Auto-generated Docs**: Out-of-the-box Swagger UI and ReDoc integration.

## **Architecture**

The application strictly follows a layered architectural pattern to separate business logic from HTTP transport layers:

1. **Routers (/routers)**: Handle HTTP requests, define paths, verbs, and dependency injections.  
2. **Controllers (/controllers)**: Act as the middle-man, unwrapping HTTP payloads and passing them to the service layer.  
3. **Services (/services)**: Contain the core business logic, calculations, and data manipulation.  
4. **Models (/models)**: Define Pydantic schemas for strict request/response data validation.

## **Project Structure**

.  
├── config/  
│   └── settings.py          \# Environment variables and BaseSettings  
├── controllers/  
│   ├── echo\_controller.py   \# Middle-layer connecting routers to echo services  
│   ├── health\_controller.py \# Middle-layer for health services  
│   ├── math\_controller.py   \# Middle-layer for math services  
│   └── user\_controller.py   \# Middle-layer for user services  
├── models/  
│   ├── echo\_schema.py       \# Validation schemas for Echo requests/responses  
│   ├── health\_schema.py     \# Validation schemas for Health responses  
│   ├── math\_schema.py       \# Validation schemas for Math operations  
│   └── user\_schema.py       \# Validation schemas for User CRUD  
├── routers/  
│   ├── api\_routes.py        \# Central router aggregator  
│   ├── echo.py              \# Routes for /echo  
│   ├── health.py            \# Routes for /health  
│   ├── math.py              \# Routes for /math  
│   └── user.py              \# Routes for /users  
├── services/  
│   ├── echo\_services.py     \# Core logic for Echo  
│   ├── health\_services.py   \# Core logic for Health and uptime tracking  
│   ├── math\_services.py     \# Core logic and error handling for Math  
│   └── user\_services.py     \# In-memory DB and core logic for Users  
├── utils/  
│   └── helpers.py           \# Reusable utilities (UTC time, UUIDs, Uptime)  
├── main.py                  \# FastAPI application entry point  
└── requirements.txt         \# Project dependencies

## **Getting Started**

### **Prerequisites**

Ensure you have the following installed on your local machine:

* **Python 3.10** or higher  
* **Git**

### **Installation**

1. **Clone the repository:**  
   git clone \[https://github.com/yourusername/API\_endpoints\_Flash.git\](https://github.com/yourusername/API\_endpoints\_Flash.git)  
   cd API\_endpoints\_Flash

2. **Create and activate a virtual environment:**  
   python \-m venv .venv

   \# On macOS/Linux:  
   source .venv/bin/activate  

   \# On Windows:  
   .venv\\Scripts\\activate

3. **Install the dependencies:**  
   pip install \-r requirements.txt

### **Running the Server**

You can start the development server using Uvicorn (FastAPI's lightning-fast ASGI server):

uvicorn main:app \--host 0.0.0.0 \--port 8000 \--reload

*Alternatively, you can run it directly via Python: python main.py*

The API will now be accessible at http://localhost:8000.

## **API Documentation**

FastAPI automatically generates interactive API documentation. Once the server is running, you can explore the endpoints, view schemas, and test requests directly from your browser:

* **Swagger UI (Interactive):** http://localhost:8000/docs  
* **ReDoc (Detailed):** http://localhost:8000/redoc

## **Endpoints Overview**

Here is a brief overview of the available endpoints. Visit the **Swagger UI** for detailed payload requirements.

### **Health & System**

* GET /health : Returns server uptime, status, and UTC timestamp.

### **Echo**

* POST /echo : Reflects the provided message and optional data back to the client.

### **Math Operations**

* GET /math?operation={op}\&a={float}\&b={float} : Performs add, subtract, multiply, or divide.

### **User Management**

* GET /users : Retrieve a paginated list of all active users.  
* POST /users : Register a new user.  
* GET /users/{user\_id} : Fetch specific user details.  
* PUT /users/{user\_id} : Update user information.  
* DELETE /users/{user\_id} : Remove a user from the system.