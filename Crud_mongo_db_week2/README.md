# **User Management API (MongoDB Implementation)**

A high-performance, asynchronous RESTful service built with FastAPI and Beanie ODM for robust user data management.

## **Overview**

This project implements a standardized User CRUD (Create, Read, Update, Delete) system. It is specifically engineered to handle asynchronous data operations using MongoDB as the primary data store, ensuring low latency and high concurrency handling.

## **Technical Architecture**

The application implements a layered architectural pattern to ensure scalability and maintainability:

1. **Routers**: Interface layer defining HTTP endpoints and request routing.  
2. **Controllers**: Orchestration layer handling request validation and response serialization.  
3. **Services**: Logic layer encapsulating database interactions and business rules.  
4. **Models**: Data layer utilizing Beanie Documents and Pydantic schemas for strict type safety.  
5. **Configuration**: Centralized management of environment variables and database initialization.

### **Technology Stack**

* **Runtime**: Python 3.10+  
* **Web Framework**: FastAPI  
* **Database ODM**: Beanie (Object Document Mapper)  
* **Database Driver**: Motor (Asynchronous MongoDB)  
* **Data Validation**: Pydantic V2  
* **Server**: Uvicorn (ASGI)

## **API Endpoints**

| Method | Endpoint | Description |
| :---- | :---- | :---- |
| POST | /users | Register a new user profile with a unique email. |
| GET | /users | Retrieve a collection of all registered users. |
| GET | /users/{id} | Fetch detailed information for a specific user ID. |
| PATCH | /users/{id} | Update specific fields of an existing user profile. |
| DELETE | /users/{id} | Permanently remove a user record from the database. |
| GET | /health | System diagnostics and status check. |

## **Installation and Setup**

### **Prerequisites**

* Python 3.10 or higher  
* Access to a MongoDB instance (Local or Atlas)

### **Environment Configuration**

Create a .env file in the project root with the following configuration:

MONGO\_URL=mongodb://localhost:27017  
DB\_NAME=user\_crud\_db

### **Deployment Instructions**

1. **Initialize Virtual Environment**:  
   python \-m venv .venv  
   source .venv/bin/activate  \# Windows: .venv\\Scripts\\activate

2. **Install Dependencies**:  
   pip install \-r requirements.txt

3. **Launch the Application**:  
   uvicorn main:app --reload

## **Development Standards**

The project adheres to the following development principles:

* **Asynchronous I/O**: All database operations are non-blocking to maximize throughput.  
* **Schema Enforcement**: Strict validation of incoming payloads and outgoing responses using Pydantic.  
* **Serialization**: Automatic conversion of MongoDB ObjectIDs to strings for JSON compatibility.  
* **Error Handling**: Centralized exception management for consistent API error responses.

