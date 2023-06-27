# django-otp


# How to work it :
 1. Register a user with username, email, password, phone_number, type=register in body of request and method=POST to http://localhost:8000/home/ url (you can use postman) and you will get otp in your phone number and you will get response 'otp sent' in postman console. (you can check otp in console) or you can check otp in admin panel also.

        example: {
            "username": "test",
            "email": "test@gmail.com",
            "password": "test1234",
            "phone": "1234567890"
            "type": "register"
        }


 2. Verify otp with username, otp, type=otp in body of request and method=POST to http://localhost:8000/home/ url (you can use postman) and you will get response 'otp verified' in postman console.

        example: {
            "username": "test",
            "otp": "1234",
            "type": "otp"
        }



 3. send  login_otp with username, type=login_otp in body of request and method=POST to http://localhost:8000/home/ url (you can use postman) and you will get otp in your phone number and you will get response 'otp sent' in postman console. (you can check otp in console) or you can check otp in admin panel also.

        example: {
            "username": "test",
            "type": "login_otp"
        }
  



 4. Login with username, password, otp, type=login in body of request and method=POST to http://localhost:8000/home/ url (you can use postman) and you will get otp in your phone number and you will get response 'login success' in postman console.

        example: {
            "username": "test",
            "password": "test1234",
            "otp": "1234",
            "type": "login"
        }

