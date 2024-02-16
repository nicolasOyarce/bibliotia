# Bibliotia
Este proyecto consiste en una plataforma web para la venta de libros de comprensión lectora y fue desarrollado como trabajo final para la universidad.

El frontend y backend fueron creados con Django, la base de datos en Postgres y el deploy en AWS. El diseño de la interfaz web fue tomado de plantillas gratuitas disponibles en internet.

La plataforma está enfocada en padres de familia con hijos en edad escolar. Cuenta con un catálogo de libros por niveles académicos, carrito de compras, sistema de pago, control de inventario y registro de usuarios con confirmación por email.

El proyecto busca facilitar la adquisición de material educativo de lectura para que los padres puedan apoyar el aprendizaje de sus hijos.

A nivel técnico utiliza Django, Postgres, AWS, con documentación del código y buenas prácticas de programación. Si bien el diseño no es original porque fue tomado de plantillas web gratuitas, el objetivo era poner en práctica los conocimientos de desarrollo web adquiridos durante la carrera.

## Tecnologias principales
  - Python
  - Django
  - CSS
  - HTML
  - Git
  - Visual Studio Code
  - PostgreSQL
  - AWS


<!--## PostgreSQL Installation
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
    
    - Download and install PostgreSQL from https://www.postgresql.org/download/windows/-->
      

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

<!--## Database Configuration
  Start the PostgreSQL service from the "Service Manager".

  1. Access the PostgreSQL console or its executable.
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
      ALTER DATABASE database OWNER TO user;
      ```
      
  4. Create the ".env" file in the base directory.<br>
      ![image](https://github.com/nicolasOyarce/bibliotia/assets/101960895/27e20064-fbe6-4987-8f15-1d00203ece48)

  5. Once the file has been created copy and change the data.
     ```.env
      DB_NAME=bibliotia
      DB_USER=your_username
      DB_PASS=your_password
      DB_HOST=localhost
      DB_PORT=5432
     ```-->
      


  
