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
    ├── django/               # Django project source files
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

### Step 2: Configure environment variables
Create a `.env` file in the root directory and define the necessary environment variables:

```bash
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
```

### Step 3: Build and run the Docker containers
To build and start the application, run:

```bash
docker-compose up --build
```

This command will:
- Set up the PostgreSQL database
- Launch the Django web application
- Start the NGINX reverse proxy

### Step 4: Apply Django database migrations
Run the following command to apply migrations and initialize the database schema:

```bash
docker-compose exec web python manage.py migrate
```

### Step 5: Create a Django superuser (optional)
To create an admin user for accessing the Django admin panel, run:

```bash
docker-compose exec web python manage.py createsuperuser
```

### Step 6: Access the application
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
- `/django/` - Contains the Django project code.
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
