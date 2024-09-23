## ℹ️ Project overview
This project is a package and mail management system developed using Django and MySQL. It features JWT authentication, role-based access control, and tools for managing delivery requests and handling office-specific operations. The system aims to streamline package and mail logistics, offering users centralized control.

## 👨‍💻 Technologies
- Python as the core programming language.
- Django REST Framework as the Python framework used to create the project API, featuring custom user authentication, custom role-based permissions...
- MySQL as the project's DBMS.

## 📦 Project boilerplate
- The **`venv`** folder is used to create a virtual environment in Python, which is an isolated environment that allows you to manage dependencies for your project without affecting the global Python installation. This ensures that each project can have its own set of dependencies.
    
    After cloning the repository, the virtual environment folder must be created to install the backend dependencies.
    
    1. create a virtual environment
        
        ```bash
        cd back-end
        python -m venv venv
        ```
        
    2. activate the virtual environment (in cmd and not powershell)
        
        ```bash
        venv\Scripts\activate
        ```
        
    3. install the dependencies
        
        ```bash
        pip install -r requirements.txt
        ```
        
- After setting up the **`venv`** folder, create a MySQL database with the name poste-maroc, then run migrations
    
    ```bash
    cd core
    py manage.py migrate
    ```
    
- Next, run the following commands to populate the database
    ```bash
    py manage.py shell
    ```
    enter this command:
    ```bash
    exec(open('core/seeders.py').read())
    ```

- Finally, you can run your backend project server
    
    ```bash
    py manage.py runserver
    ```

## 📋 API documentation
### User management

- login
    ```bash
        POST
        http://127.0.0.1:8000/api/login/

        body: {
            "email": "email@example.com",
            "password": "pwd"
        }
    ```

- logout
    ```bash
        POST
        http://127.0.0.1:8000/api/logout/

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "refresh": "refresh token"
        }
    ```

- refresh token
    ```bash
        POST
        http://127.0.0.1:8000/api/token/refresh/

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "refresh": "refresh token"
        }
    ```


- register
    ```bash
        POST
        http://127.0.0.1:8000/api/register/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "cin": "cin",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "pwd",
            "role": "admin|manager|agent",
            "status": "actif|démissionné|décédé|retraite",
            "office": "office ID"
        }
    ```

- get authenticated user information
    ```bash
        GET
        http://127.0.0.1:8000/api/user/

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get all staff list
    ```bash
        GET
        http://127.0.0.1:8000/api/staff/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get staff members list of an office manager
    ```bash
            GET
            http://127.0.0.1:8000/api/office-staff/

            permission: IsManager

            headers: {
                "access": `Bearer ${accessToken}`
            }
    ```

- update staff information
    ```bash
        PATCH
        http://127.0.0.1:8000/api/staff/update/:id/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "cin"?: "cin",
            "first_name"?: "first_name",
            "last_name"?: "last_name",
            "email"?: "email@example.com",
            "password"?: "pwd",
            "role"?: "admin|manager|agent",
            "status"?: "actif|démissionné|décédé|retraite",
            "office"?: "office ID"
        }
    ```

- get client information
    ```bash
        POST
        http://127.0.0.1:8000/api/client/

        permission: IsAgent

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "cin": "cin",
        }
    ```

- update client information
    ```bash
        PATCH
        http://127.0.0.1:8000/api/client/:id/

        permission: IsAgent

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "cin": "cin",
            "first_name"?: "first_name",
            "last_name"?: "last_name",
            "phone_number"?: "0000000000"
        }
    ```

### Office management

- create an office
    ```bash
        POST
        http://127.0.0.1:8000/api/office/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "name": "office name",
            "address": "office address",
            "city": "office city",
        }
    ```

- update an office
    ```bash
        PATCH
        http://127.0.0.1:8000/api/office/:id/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "name"?: "office name",
            "address"?: "office address",
            "city"?: "office city",
        }
    ```

- get office list
    ```bash
        GET
        http://127.0.0.1:8000/api/offices/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get own office information
    ```bash
        GET
        http://127.0.0.1:8000/api/office-info/

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

### Product management

- get product information
    ```bash
        GET
        http://127.0.0.1:8000/api/products/

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- update product info
    ```bash
        PATCH
        http://127.0.0.1:8000/api/product/:id/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "name"?: "product name",
            "code"?: "product code",
            "prefix"?: "product prefix",
        }
    ```

### Weight range management

- get all weight ranges list
    ```bash
        GET
        http://127.0.0.1:8000/api/weight-ranges/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- update a weight range
    ```bash
        PATCH
        http://127.0.0.1:8000/api/weight-ranges/:id/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "min_weight"?: 000,
            "max_weight"?: 000,
            "price"?: 000,
            "product"?: "product id",
            "status"?: "disabled|activated"
        }
    ```

- get active weight ranges list
    ```bash
        GET
        http://127.0.0.1:8000/api/active-weight-ranges/

        permission: IsAgent|IsManager

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get all product weight ranges
    ```bash
        GET
        http://127.0.0.1:8000/api/product-weight-ranges/:id/

        permission: IsAdmin

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get all product active weight ranges
    ```bash
        GET
        http://127.0.0.1:8000/api/active-product-weight-ranges/:id/

        permission: IsAgent|IsManager

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get a weight price
  ```bash
        GET
        http://127.0.0.1:8000/api/range-price/

        permission: IsAgent

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "weight": 000,
            "product": "product ID"
        }
    ```

### Sending request management

- create a sending request
    ```bash
        POST
        http://127.0.0.1:8000/api/send-request/

        permission: IsAgent

        headers: {
            "access": `Bearer ${accessToken}`
        }

        body: {
            "cin": "cin",
            "first_name"?: "first_name",
            "last_name"?: "last_name",
            "phone_number"?: "0000000000",
            "product": "product ID"
            "range": "range ID",
            "amount": 000,
            "sms": True|False,
            "weight": "request weight",
            "destination": "request destination",
        }
    ```

- cancel a request
    ```bash
        PATCH
        http://127.0.0.1:8000/api/cancel-request/:id/

        permission: IsManager

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get sending requests list of an office
    ```bash
        GET
        http://127.0.0.1:8000/api/requests-list/

        permission: IsAgent|IsManager

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- print a sending request receipt
    ```bash
        GET
        http://127.0.0.1:8000/api/receipt-print/:id/

        permission: IsAgent|IsManager

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get own transactions
    ```bash
        GET
        http://127.0.0.1:8000/api/transactions/

        permission: IsAgent

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get agent transactions
    ```bash
        GET
        http://127.0.0.1:8000/api/transactions/:id/

        permission: IsManager

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```

- get all transactions data (aggregated with agents)
    ```bash
        GET
        http://127.0.0.1:8000/api/transactions-dashboard/

        permission: IsManager

        headers: {
            "access": `Bearer ${accessToken}`
        }
    ```