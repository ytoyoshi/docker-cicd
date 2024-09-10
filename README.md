# Docker-CI/CD Django Project

## Overview
This project demonstrates how to set up a basic CI/CD pipeline using Docker for a Django application. It includes services for a Django web application, PostgreSQL as the database, and NGINX as the reverse proxy. The goal is to automatically release the Django application when changes are pushed to the source code.

## Prerequisites
- [Docker](https://www.docker.com/get-started) (version 20.10 or later)
- [Docker Compose](https://docs.docker.com/compose/) (version 1.29 or later)
- Python 3.10 (for local Django development)
- PostgreSQL (version 16.3)

## Project Structure

```
/docker-cicd
    ├── dockercicd/           # Django project source files
    ├── nginx/                # Nginx configuration
    ├── docker-compose.yml    # Docker Compose configuration
    ├── Dockerfile            # Django application Dockerfile
    └── README.md             # Project documentation
```

## Installation

### Step 1: Clone the repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/ytoyoshi/docker-cicd.git
cd docker-cicd
```

### Step 2: Set up a Python virtual environment

1. **Create the virtual environment:**

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies from `requirements.txt`:**

   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Configure environment variables
Modify the `.env` file located in the root directory of the repository (`https://github.com/ytoyoshi/docker-cicd/tree/main/dockercicd`) to define the necessary environment variables. Ensure the values match the settings defined in `docker-compose.yml`:

```bash
DB_NAME=your_db_name   # Replace with the actual database name
DB_USER=your_db_user   # Replace with the actual database username
DB_PASSWORD=your_db_password   # Replace with the actual database password
DB_HOST=db   # This should match the service name in docker-compose.yml
DB_PORT=5432   # Default PostgreSQL port
```

### Step 4: Build and run the Docker containers
To build and start the application, run:

```bash
docker-compose up --build
```

This command will:
- Set up the PostgreSQL database
- Launch the Django web application
- Start the NGINX reverse proxy

### Step 5: Apply Django database migrations
Run the following command to apply migrations and initialize the database schema:

```bash
docker-compose exec web python manage.py migrate
```

### Step 6: Create a Django superuser (optional)
To create an admin user for accessing the Django admin panel, run:

```bash
docker-compose exec web python manage.py createsuperuser
```

### Step 7: Access the application
You can now access the application and the Django admin panel using the following URLs:

- Web application: `http://localhost`
- Admin panel: `http://localhost/admin`

## CI/CD Pipeline

The project is designed to automatically deploy the Django application whenever new code is pushed to the repository. The CI/CD pipeline is set up using Docker, with the following steps:

1. **Build**: Docker builds the Django application image.
2. **Test**: Automated tests are executed (e.g., Django tests).
3. **Deploy**: The Docker container is restarted, and the new version of the application is deployed.

## Usage

### Running tests
To run tests for the Django application:

```bash
docker-compose exec web python manage.py test
```

### Stopping the application
To stop the Docker containers:

```bash
docker-compose down
```

## Directory Structure
- `/dockercicd/` - Contains the　dockercicd Django project code.
- `/nginx/` - NGINX configuration files for the reverse proxy.
- `docker-compose.yml` - Configuration for Docker services (Django, PostgreSQL, NGINX).
- `Dockerfile` - Instructions to build the Django application Docker image.

## Troubleshooting

### Database connection issues
Ensure that the database credentials in the `.env` file are correct and that the PostgreSQL container is running properly.

### Docker container issues
Use the following command to check logs and diagnose issues with the Docker containers:

```bash
docker-compose logs
```

## Contributing
To contribute to this project, fork the repository and create a pull request with your changes. Be sure to write clear commit messages and test your changes before submission.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
