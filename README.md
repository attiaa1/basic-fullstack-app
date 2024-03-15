# Full Stack Application

## Backend (Python and Flask) LAST UPDATED: 3/14/2023

Utilizes route decorators with their respective functions and request/response calls such as POST, PATCH, and DELETE to create an API which stores a Python object with the below parameters in JSON format. The scripts also leverage HTTP Response status codes and try/except blocks to correct user-inputted error.

```py
    class Contact(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(50), unique=False, nullable=False)
        last_name = db.Column(db.String(50), unique=False, nullable=False)
        email = db.Column(db.String(100), unique=True, nullable=False)
```

Thus this backend API can handle a person and their first name, last name, and email, and is scalable.

How to run this part of the application:
```bash 
    cd ~basic-fullstack-app/backend/
    python3 main.py
```

## Frontend (JS and React)

Coming soon