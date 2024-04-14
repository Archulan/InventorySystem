
# Inventory System API Documentation

This document provides instructions on how to interact with the Inventory System APIs, developed using Django and Django REST Framework. It includes details on how to perform CRUD operations on items, batches, and item types, and how to use the API gateway for combined data submissions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework
- drf-yasg for API documentation

### Installing

First, clone the repository:

```bash
git clone https://github.com/Archulan/InventorySystem
cd InventorySystem
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

### Items

- **GET /api/items/**: Retrieve all items.
- **POST /api/items/**: Create a new item.
- **GET /api/items/{id}/**: Retrieve an item by ID.
- **PUT /api/items/{id}/**: Update an item by ID.
- **DELETE /api/items/{id}/**: Delete an item by ID.

### Batches

- **GET /api/batches/**: Retrieve all batches.
- **POST /api/batches/**: Create a new batch.
- **GET /api/batches/{id}/**: Retrieve a batch by ID.
- **PUT /api/batches/{id}/**: Update a batch by ID.
- **DELETE /api/batches/{id}/**: Delete a batch by ID.

### Item Types

- **GET /api/itemtypes/**: Retrieve all item types.
- **POST /api/itemtypes/**: Create a new item type.
- **GET /api/itemtypes/{id}/**: Retrieve an item type by ID.
- **PUT /api/itemtypes/{id}/**: Update an item type by ID.
- **DELETE /api/itemtypes/{id}/**: Delete an item type by ID.

### API Gateway for Combined Data Submission

- **POST /api/submit-data/**: Submit combined data for items, batches, and item types.

#### Example Payload for Combined Data Submission

```json
{
    "item_types": [
        {"type_name": "Electronics", "description": "All electronic devices"}
    ],
    "items": [
        {"name": "Smartphone", "description": "High-end mobile device", "quantity": 100, "item_type": 1}
    ],
    "batches": [
        {"batch_code": "SP1000", "date_received": "2024-04-13", "quantity": 100, "item": 1}
    ]
}
```

### Using Swagger API Documentation

Navigate to `http://127.0.0.1:8000/swagger/` to view the Swagger UI where you can interact with the API directly from your browser.


