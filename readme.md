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
 
#### cmd to create superuser

```bash
docker-compose exec web python manage.py createsuperuser
```


## command to run tests cases locally
```bash
pytest
```


## API Details

### Registration
```bash

Endpoints
1. User Authentication
Signup

    Endpoint: /api/signup/
    Method: POST
    Authentication: Not required
    Request Body:

{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "securepassword123"
}

Response:

    {
      "message": "Signup successful",
      "user_id": 1,
      "email": "johndoe@example.com",
      "token": "your_auth_token"
    }

Login

    Endpoint: /api/login/
    Method: POST
    Authentication: Not required
    Request Body:

{
  "email": "johndoe@example.com",
  "password": "securepassword123"
}

Response:

    {
      "message": "Login successful",
      "user_id": 1,
      "email": "johndoe@example.com",
      "token": "your_auth_token"
    }

2. Events
List Events

    Endpoint: /api/events/

    Method: GET

    Authentication: Required

    Query Parameters:
        type (optional): Filter events by type.
            past: Past events
            upcoming: Upcoming events
            Leave empty for all events.

    Response:

    [
      {
        "id": 1,
        "title": "Event Title",
        "description": "Event Description",
        "date": "11 Nov 23",
        "time": "11:20 AM",
        "location": "New York"
      },
      {
        "id": 2,
        "title": "Another Event",
        "description": "Event Description",
        "date": "12 Nov 23",
        "time": "1:00 PM",
        "location": "Los Angeles"
      }
    ]

Create Event

    Endpoint: /api/events/
    Method: POST
    Authentication: Required
    Request Body:

{
  "title": "New Event",
  "description": "Details of the new event",
  "date": "2024-02-14",
  "time": "10:30:00",
  "location": "London"
}

Response:

    {
      "id": 1,
      "title": "New Event",
      "description": "Details of the new event",
      "date": "14 Feb 24",
      "time": "10:30 AM",
      "location": "London"
    }

Retrieve Event

    Endpoint: /api/events/<id>/
    Method: GET
    Authentication: Required
    Response:

    {
      "id": 1,
      "title": "New Event",
      "description": "Details of the new event",
      "date": "14 Feb 24",
      "time": "10:30 AM",
      "location": "London"
    }

Update Event

    Endpoint: /api/events/<id>/
    Method: PUT
    Authentication: Required
    Request Body:

{
  "title": "Updated Event",
  "description": "Updated details of the event",
  "date": "2024-03-10",
  "time": "14:00:00",
  "location": "Paris"
}

Response:

    {
      "id": 1,
      "title": "Updated Event",
      "description": "Updated details of the event",
      "date": "10 Mar 24",
      "time": "02:00 PM",
      "location": "Paris"
    }

Partial Update Event

    Endpoint: /api/events/<id>/
    Method: PATCH
    Authentication: Required
    Request Body:

{
  "title": "Partially Updated Event"
}

Response:

    {
      "id": 1,
      "title": "Partially Updated Event",
      "description": "Updated details of the event",
      "date": "10 Mar 24",
      "time": "02:00 PM",
      "location": "Paris"
    }

Delete Event

    Endpoint: /api/events/<id>/
    Method: DELETE
    Authentication: Required
    Response:

{
  "message": "Event deleted successfully"
}

```