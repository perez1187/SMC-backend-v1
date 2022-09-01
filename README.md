# SMC-backend-v1

app User

models.py
    1. custom User model(name: User) base on Abstract User
        - email instead of username
    2. a new User Manager base on Base User Manager
        - function create user and createsuperuser

serializer.py
    1. RegisterSerializer (for create an account)
    2. AuthTokenSerializer (for login)

views.py
    1. login_api for login 
    2. get_user_data
    3. register_api for register new user

    inactive:
    RegisterApi

admin@gmail.com
admin
rest 1234