from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models.signals import post_save

'''
    1. we create a new User model base on Abstract User
    2. we create a new User Manager base on Base User Manager
    3. in progress create signal for creating userr Profile
'''

class UserManager(auth_models.BaseUserManager):
    
    def create_user(self, first_name: str, last_name: str, email: str, password:str = None, is_staff = False, is_superuser=False) -> "User": # password as default is None
        
        # validation

        if not email: 
            raise ValueError('User must have and an email')
        if not first_name:
            raise ValueError('User must have and a First Name')
        if not last_name:
            raise ValueError('User must have and a Last Name')

        # creating user

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save() # we save user to db

        return user
    
    def create_superuser(self, first_name: str, last_name: str, email: str, password:str ) -> "User":
        
        # we call function create_user from above
        
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        ) 
        user.save()

        return user


class User(auth_models.AbstractUser):
    ''' we dont need first_name and last_name because there are in Abstractuser '''
    first_name = models.CharField(verbose_name="First Name", max_length=255) # verbose_name: A human-readable name for the object, singular
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None # because we dont want username

    # we can add here whatever we want like mobile number, description etc

    objects= UserManager () # the User Manager that we created


    USERNAME_FIELD = "email" # we set email as login field
    REQUIRED_FIELDS= ['first_name', 'last_name']

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ''' 
        we can also one to one field like here
        https://www.youtube.com/watch?v=Kc1Q_ayAeQk
    '''

    description= models.TextField(max_length=255, default='', blank=True)

    def __str__(self):
        return str(self.user)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("Profile created")

post_save.connect(create_user_profile, User)