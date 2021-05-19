# iraitechsite

The solutions folder contains code to the given  problems

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

3. **Template: Solve problem**
    1. **Endpoint:** /api/v1/calculate/
    2. **Input:**
        - x and n values for problem 1
    3. **Output:**
        - result
    4. **Authentication:**:
        - only users with valid csrftoken can access the page.

***Notes:***
- *Please use Postman calls for testing the register and login features*
- *Go to endpoint http://127.0.0.1:9000/api/v1/calculate/ directly to view working frontend template of problem 1 (I have not created frontend templates for other features.)*
