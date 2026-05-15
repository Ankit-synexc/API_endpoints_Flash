# **API Endpoints Flash**

A comprehensive backend ecosystem featuring modular **FastAPI** REST services and **Machine Learning** integration. This repository demonstrates clean architecture, asynchronous database operations with MongoDB, and predictive modeling.

## **Project Modules**

1. **API\_1**: Core FastAPI application with in-memory storage. Features Health, Math, Echo, and User CRUD services.  
2. **Crud\_mongo\_db\_week2**: Advanced User service using **MongoDB** and **Beanie ODM**. Includes endpoints for Iris flower classification using a pre-trained model.  
3. **Iris\_classifier\_source\_code**: Scikit-learn implementation of an Iris flower classifier (KNN/Random Forest). This is the "training ground" for the models used in the API.

## **Tech Stack**

* **Language**: Python 3.10+  
* **Framework**: FastAPI  
* **Database**: MongoDB (Async via PyMongo & Beanie)  
* **ML**: Scikit-Learn, Joblib, Matplotlib, Seaborn  
* **Validation**: Pydantic V2  
* **Documentation**: Swagger UI & ReDoc

## **Getting Started**

### **1\. Prerequisites**

* Python 3.10 or higher installed.  
* MongoDB installed locally or an Atlas connection string.  
* Virtual Environment tool (venv).

### **2\. Installation**

Clone the repository and install all required dependencies:

git clone \[https://github.com/ankit-synexc/api\_endpoints\_flash.git\](https://github.com/ankit-synexc/api\_endpoints\_flash.git)  
cd api\_endpoints\_flash  
pip install \-r requirements.txt

### **3\. Running the ML Module (Model Training)**

Before using prediction endpoints in the API, you must train the model or explore the training logic:

cd Iris\_classifier\_source\_code  
\# Launch jupyter to run the training cells  
jupyter notebook iris\_classifier.ipynb

*Note: Executing the notebook saves iris\_Knn\_classifier.joblib, which is used by the API for live predictions.*

### **4\. Running the API Services**

#### **Module A: Core API (API\_1)**

In-memory storage version (no database required).

cd API\_1  
uvicorn main:app \--reload \--port 8000

* **Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

#### **Module B: MongoDB & ML User Service (Crud\_mongo\_db\_week2)**

1. Ensure MongoDB is running.  
2. Run the service:

cd Crud\_mongo\_db\_week2  
uvicorn main:app \--reload \--port 8001

* **Docs**: [http://localhost:8001/docs](http://localhost:8001/docs)

## **API Endpoints Summary**

| Method | Endpoint | Module | Description |
| :---- | :---- | :---- | :---- |
| GET | /health | API\_1 | System uptime and status. |
| POST | /echo | API\_1 | Returns sent payload. |
| GET | /math | API\_1 | Params: operation, a, b. |
| POST | /users | Mongo | Register user in MongoDB. |
| POST | /iris/predict | Mongo | Predict Iris species using trained model. |

## **Architecture Design**

The project follows a **Separation of Concerns** model:

* **Routers**: Handles path definitions and HTTP verbs.  
* **Controllers**: Validates input and orchestrates service calls.  
* **Services**: Contains the actual business, database, or ML prediction logic.  
* **Models/Schemas**: Pydantic classes for strict data typing.