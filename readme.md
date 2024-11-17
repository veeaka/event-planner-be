## Steps to Start the Development Server

### 1. Clone the Repository
```bash
git clone git@github.com:veeaka/event-planner-be.git
cd event_planner
```

### 3. Start the Development Server

#### Run the following command to start the services (frontend, backend, and database):
```bash
sudo docker-compose up --build
```

### run the following command to create database on docker postgres
```bash
sudo docker exec -it event_planner_db_1 psql -U postgres

create database event_planner_db
```
### This will:

####    Build the Docker images.
####    Start the Django backend and PostgreSQL database.

### 4. Access the Application
####    Backend: http://localhost:8000
####    Admin Panel: http://localhost:8000/admin

### 5. Stop the Development Server

#### To stop all running containers, use:
```bash
sudo docker-compose down
```

### additionally 
#### cmd to create superuser

```bash
docker-compose exec web python manage.py createsuperuser
```