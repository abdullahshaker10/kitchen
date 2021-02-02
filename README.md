# kitchen

# Motivations 
it is a Django Project for manageing Kitchen using: 
- Django. 
- Django Rest Framework. 

## Getting Started
### Pre-requisites and Local Development
Developers using this project should already have Python3, Django and pipenv installed in their local machines.
#### PIP Dependencies
run this command in the root of the project that will create virtual environment and install dependencies. 
```bash
pipenv install
``` 
to activate the virtual env run this. 
```bash
pipenv shell
```   
To run the Migrations, execute this commands in the root folder:  
```bash
python manage.py makemigrations
```
```bash 
python manage.py migrate
```   
To run the server, execute this command in the root folder:
```bash 
python manage.py runserver
``` 

## Auth
- to sign up fpr create new users and chose thier type.
```/accounts/signup/```

- to login 
```/accounts/login/```

- to get auth token for specific user so we can use it in the headers of APIS

```$ curl -X POST http://127.0.0.1:8000/api-token-auth/ username=vitor password=123```

### create admin users
```bash 
python manage.py createsuperuser
``` 
## API Reference

### Endpoints

#### POST '/orders/api/create'
(requires authenticated Waiter permission)

```$ curl -X POST http://127.0.0.1:8000/orders/api/create```

   - Create new Order.  
   - Request Arguments: None.
   - Request Headers: authentication token.
   - Request Body: (json)
     - string title
     - string description
     - int client(which is client'id)
   - Return an order object which assigned to current user who is waiter user.
     ```
      {
       "id": 1,
       "title": "title1",
       "description": "desc",
       "status": "New",
       "created_at": "2021-02-02T00:04:22.436398Z",
       "client": 2,
       "waiter": 1,
       "assigned_to": null
       }
     ```
     
#### GET '/orders/api'
(requires authenticated user)

```$ curl -X GET http://127.0.0.1:8000/orders/api```

   - List all Orders. 
   - Request Headers: authentication token.
   - Request Arguments: client's id.
   - Return an list of orders objects for specific client.
     ```
     [
     {
        "id": 1,
        "title": "title1",
        "description": "desc",
        "status": "Preparing",
        "created_at": "2021-02-02T00:04:22.436398Z",
        "client": 2,
        "waiter": 2,
        "assigned_to": 3,
        "progress": [
            {
                "id": 5,
                "progress_note": "note",
                "created_at": "2021-02-02T14:03:11.289926Z",
                "order": 22,
                "created_by": 1
            },
          ]
     },
     {
        "id": 12,
        "title": "title1",
        "description": "desc",
        "status": "New",
        "created_at": "2021-02-02T00:04:22.436398Z",
        "client": 2,
        "waiter": 1,
        "assigned_to": 1,
        "progress" : []
        
     },
 
     ```
#### GET '/orders/api/details'
(requires authenticated user)

```$ curl -X GET http://127.0.0.1:8000/orders/api/details```

   - Get Order's details. 
   - Request Headers: authentication token.
   - Request Arguments: order's id.
   - Return an order object with it's progress ojects.

   ```
   {
    "id": 22,
    "client": 2,
    "title": "title1",
    "description": "desc",
    "status": "Canceled",
    "waiter": 1,
    "assigned_to": 2,
    "created_at": "2021-02-02T00:28:07.248825Z",
    "progress": [
        {
            "id": 5,
            "progress_note": "note",
            "created_at": "2021-02-02T14:03:11.289926Z",
            "order": 22,
            "created_by": 1
        },
        {
            "id": 6,
            "progress_note": "note",
            "created_at": "2021-02-02T14:03:20.827035Z",
            "order": 22,
            "created_by": 1
        },

        ]
      }
 
  ```
#### PATCH '/orders/api/update'
(requires authenticated Assistant and Chief user)

```$ curl -X PATCH http://127.0.0.1:8000/orders/api/update/2```
   - assign specific Order and the state is updted based on prev state and current user role. 
   - Request Headers: authentication token.
   - Return updated order and assigned to current user.
     ```
     {
       "id": 2,
       "title": "title1",
       "description": "desc",
       "status": "Preparing",
       "created_at": "2021-02-02T00:28:07.248825Z",
       "client": 2,
       "waiter": 1,
       "assigned_to": 1
     }
 
     ```
#### POST '/orders/progress/api/create'
(requires authenticated Assistant and Chief user)

```$ curl -X POST http://127.0.0.1:8000/orders/progress/api/create```
   - create new progress object for specific user and specific user. 
   - Request Headers: authentication token.
   - Request Bode: 
     - int order
     - string prgress_note
   - Return updated order and assigned to current user.
     ```
     {
       "id": 2,
       "title": "title1",
       "description": "desc",
       "status": "Preparing",
       "created_at": "2021-02-02T00:28:07.248825Z",
       "client": 2,
       "waiter": 1,
       "assigned_to": 1
     }
 
     ```
#### GET '/orders/progress/api'
(requires authenticated Chief user)

```$ curl -X GET http://127.0.0.1:8000/orders/progress/api```
   - list progress objects for specific order. 
   - Request Headers: authentication token.
   - Request Arguments order's id
   - Return list of progresses objects of specific order.
     ```
     [
     {
        "id": 5,
        "progress_note": "note",
        "created_at": "2021-02-02T14:03:11.289926Z",
        "order": 22,
        "created_by": 1
     },
     {
        "id": 6,
        "progress_note": "note",
        "created_at": "2021-02-02T14:03:20.827035Z",
        "order": 22,
        "created_by": 1
     },
     ```
#### PATCH '/users/api/update'
(requires authenticated Chief user)


```$ curl -X PATCH http://127.0.0.1:8000/users/api/update```
   - Update user object for activate and deactivate. 
   - Request Headers: authentication token.
   - Request Arguments user's id
   - Request body:
     - bool active
   - Return updated user instance.
   
   ```
     {
       "id": 2,
       "username": "sh",
       "email": "sh@gmail.com",
       "is_active": false
    }
   ```

