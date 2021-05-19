# iraitechsite

The solutions folder contains code to the given  problems

Kindly use "python manage.py runserver 127.0.0.1:9000" to run the code at specified endpoint

1. **API: Register to site**
    1. **Method:** POST
    2. **Endpoint:** /register/
    3. **Request:**
        1. email
        2. phone
        3. password
    4. **Status:**
        - 200_OK if the request is successful
        - 400_BAD_REQUEST if any of the request fields are missing
    5. **Sample Postman request:**
        - https://www.getpostman.com/collections/efa4b9f2107e3ebbd872
2. **API: Can login as a user**
    1. **Method:** POST
    2. **Endpoint:** /login/
    3. **Request:**
        1. email
        2. phone
        3. password
    4. **Response:**
        - User id
        - details
    5. **Status:**
        - 200_OK if the request is successful
        - 400_BAD_REQUEST if any of the request fields are missing
    6. **Sample Postman request:**
        - https://www.getpostman.com/collections/efa4b9f2107e3ebbd872

3. **Template: Solve problems**
    1. **Endpoint:** /api/v1/calculate/
    2. **Input:**
        - x and n for problem 1
        - x, y, a, b for problem 3
    3. **Output:**
        - result
