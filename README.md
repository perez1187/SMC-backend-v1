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

https://simpleit.rocks/python/django/adding-email-to-django-the-easiest-way/

signals:
https://www.youtube.com/watch?v=Kc1Q_ayAeQk

confirm email:
user create an account
auto login, token into cookies
send email with address +  for example id
if user is a create user than in models is_viried True

we need to also check if he is already virified to not double check