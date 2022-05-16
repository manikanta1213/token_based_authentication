TOKEN BASED AUTHENTICATION

This project's purpose is to demonstrate token based authentication using django rest framework.

Steps to run this project:

open the terminal and run the following commands
1. pip install -r requirements.txt
2. python manage.py runserver or py -3 manage.py runserver
3. create admin user using command py -3 manage.py createsuperuser --username 'your username' --email 'your email'
4. login to django admin panel http:127.0.0.1:8000/admin
5. once the user is created. execute the curl command to get the token
        curl --location --request POST 'http://127.0.0.1:8000/get/token' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "username": 
                "<username>",
            "password": 
                "<password>"
        }'
6. Use the token to create data using POST API
        curl --location --request POST 'http://127.0.0.1:8000/api/message/' \
        --header 'Authorization: Token <token>' \
        --header 'Content-Type: application/json' \
        --data-raw '{"body":"Hi, Checking the post method"}'

    It posts the data and the data gets stored in the database. It only allows 10 messages per hour for a user.
    Output:
        {
            "id": 22,
            "message": "Hi, Checking the post method",
            "created_at": "2022-05-16T17:39:15.387416Z",
            "updated_at": "2022-05-16T17:39:15.387416Z",
            "created_by": {
                "id": 1,
                "username": "manikanta",
                "email": "manikanta@mydashllc.com"
            }
        }

7. Functionality of this  project can be extended to get, update, delete.