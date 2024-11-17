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

### This will:

####    Build the Docker images.
####    Start the Django backend, React frontend, and PostgreSQL database.

### 4. Access the Application
####    Backend: http://localhost:8000
####    Admin Panel: http://localhost:8000/admin

### 5. Stop the Development Server

#### To stop all running containers, use:
```bash
sudo docker-compose down
```