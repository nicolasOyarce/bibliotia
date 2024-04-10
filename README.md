[![freeCodeCamp Social Banner](https://cdn.freecodecamp.org/platform/universal/fcc_banner_new.png)](https://www.freecodecamp.org/)
# Bibliotia
This project consists of a web platform for the sale of reading comprehension books and was developed as a work for the university.

The frontend and backend were created with Django, the database in Postgres and the deploy in AWS. The web interface design was taken from free templates available on the internet.

The platform is focused on parents with school-age children. It has a catalog of books by academic levels, shopping cart, payment system, inventory control and user registration with email confirmation.

The project seeks to facilitate the acquisition of educational reading material so that parents can support their children's learning.

At the technical level it uses Django, Postgres, AWS, with code documentation and good programming practices. Although the design is not original because it was taken from free web templates, the goal was to put into practice the knowledge of web development acquired during the course.

> [!NOTE]  
> It is worth mentioning that the project is not currently uploaded to AWS, but at the time it was presented and evaluated, it was running and operating on AWS..

## Table of Contents

  - [Installation](#installation)
  - [Use](#use)
  - [License](#license)
  - [Contact](#contact)

## Main Technologies
  <a href="https://skillicons.dev" align="center">
    <img src="https://skillicons.dev/icons?i=django,git,aws,bootstrap,css,cloudflare,github,html,js,md,postgresql,py,vscode&perline=14" />
  </a>

## Installation

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
      

## Use
## License
## Contact
