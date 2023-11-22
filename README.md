# Bibliotia
Joint project of an ecommers website for the sale of books. 

## Prerequisites
  - Python
  - Git
  - PostgreSQL
  - Visual Studio Code


## PostgreSQL Installation
  - Linux: 
    - Update the package index
      ```bash
      sudo apt update
      ```
    
    - Install PostgreSQL
      ```bash
      sudo apt install postgresql postgresql-contrib
      ```
      
  - Windows:
    
    - Download and install PostgreSQL from https://www.postgresql.org/download/windows/
      

## Basic Installation

  - Copy repository:
  ```bash
  git clone https://github.com/nicolasOyarce/bibliotia.git
  ```
  - Create virtual enviroment:
  ```bash
  pip install virtualenv
  virtualenv venv
  ```

  - Start the virtual environment:
    
      - Linux:
        ```bash
        source venv/bin/activate
        ```

      - Windows:
        ```bash
        venv/Scripts/activate
        ```
        
  - Once inside the virtual environment use the following command:
    ```bash
    pip install -r requirements.txt
    ```

## Database Configuration
  Start the PostgreSQL service from the "Service Manager".

  1. Access the PostgreSQL console.
      ```bash
      # Access to the PostgreSQL console
      psql -U postgres
      ```

  2. Creates a database for the project.
      ```sql
      CREATE DATABASE bibliotia;
      ```
    
  3. Creates a user and assigns permissions.
      ```sql
      CREATE USER user_name WITH PASSWORD 'your_password';
      ALTER ROLE username SET client_encoding TO 'utf8';
      ALTER ROLE username SET default_transaction_isolation TO 'read committed';
      ALTER ROLE username SET timezone TO 'UTC';
      GRANT ALL PRIVILEGES ON DATABASE your_database_name TO user_name;
      ```

4. Configured in the settings.py file
    ```python
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'bibliotia',
            'USER': 'username',
            'PASSWORD': 'your_password',
            'HOST': '127.0.0.1',
            'DATABASE_PORT': '5432',
        }}
    ```
