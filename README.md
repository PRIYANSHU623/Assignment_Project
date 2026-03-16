# Django Modular Entity and Mapping API

## Project Overview

This project implements a **modular backend system using Django and Django REST Framework (DRF)** to manage entities and their relationships.

The system manages:

* Vendors
* Products
* Courses
* Certifications

And the mappings between them:

* Vendor → Product
* Product → Course
* Course → Certification

All APIs are implemented using **APIView only** (without ViewSets or GenericAPIView) and documented using **drf-yasg Swagger documentation**.

---

# Technologies Used

* Python
* Django
* Django REST Framework
* drf-yasg (Swagger API documentation)

---

# Project Structure

```
Assignment_Project
│
├── config/
├── vendor/
├── product/
├── course/
├── certification/
├── vendor_product_mapping/
├── product_course_mapping/
├── course_certification_mapping/
│
├── manage.py
├── requirements.txt
└── README.md
```

Each app contains:

```
models.py
serializers.py
views.py
urls.py
admin.py
```

---

# Installation and Setup

### 1 Clone the Repository

```
git clone https://github.com/PRIYANSHU623/Assignment_Project.git
cd Assignment_Project
```

---

### 2 Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate
```

---

### 3 Install Dependencies

```
pip install -r requirements.txt
```

---

### 4 Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 5 Run the Server

```
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

# API Documentation

Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

ReDoc:

```
http://127.0.0.1:8000/redoc/
```

These pages contain **interactive API documentation**.

---

# API Endpoints

## Vendor APIs

```
GET    /api/vendors/
POST   /api/vendors/
GET    /api/vendors/<id>/
PUT    /api/vendors/<id>/
PATCH  /api/vendors/<id>/
DELETE /api/vendors/<id>/
```

---

## Product APIs

```
GET    /api/products/
POST   /api/products/
GET    /api/products/<id>/
PUT    /api/products/<id>/
PATCH  /api/products/<id>/
DELETE /api/products/<id>/
```

---

## Course APIs

```
GET    /api/courses/
POST   /api/courses/
GET    /api/courses/<id>/
PUT    /api/courses/<id>/
PATCH  /api/courses/<id>/
DELETE /api/courses/<id>/
```

---

## Certification APIs

```
GET    /api/certifications/
POST   /api/certifications/
GET    /api/certifications/<id>/
PUT    /api/certifications/<id>/
PATCH  /api/certifications/<id>/
DELETE /api/certifications/<id>/
```

---

## Vendor Product Mapping APIs

```
GET    /api/vendor-product-mappings/
POST   /api/vendor-product-mappings/
GET    /api/vendor-product-mappings/<id>/
PUT    /api/vendor-product-mappings/<id>/
PATCH  /api/vendor-product-mappings/<id>/
DELETE /api/vendor-product-mappings/<id>/
```

---

## Product Course Mapping APIs

```
GET    /api/product-course-mappings/
POST   /api/product-course-mappings/
GET    /api/product-course-mappings/<id>/
PUT    /api/product-course-mappings/<id>/
PATCH  /api/product-course-mappings/<id>/
DELETE /api/product-course-mappings/<id>/
```

---

## Course Certification Mapping APIs

```
GET    /api/course-certification-mappings/
POST   /api/course-certification-mappings/
GET    /api/course-certification-mappings/<id>/
PUT    /api/course-certification-mappings/<id>/
PATCH  /api/course-certification-mappings/<id>/
DELETE /api/course-certification-mappings/<id>/
```

---

# Validation Rules

The project enforces the following validations:

* Required field validation
* Unique `code` for master entities
* Duplicate mapping prevention
* Valid foreign key references
* Only **one primary mapping per parent entity**

Example:

A vendor cannot have two products with `primary_mapping = true`.

---

# Filtering Support

The APIs support query parameter filtering.

Examples:

```
/api/products/?vendor_id=1
/api/courses/?product_id=2
/api/certifications/?course_id=3
```

---

# Author

Priyanshu Maurya
