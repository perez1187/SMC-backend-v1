from rest_framework import views, response, exceptions, permissions, generics, viewsets
from rest_framework.decorators import api_view

from . import serializer as user_serializer
from knox.auth import AuthToken

# sending email
from django.core.mail import send_mail, EmailMessage

from django.urls import reverse

@api_view(['POST'])
def login_api(request):
    serializer = user_serializer.AuthTokenSerializer(data=request.data)
    #now we check if data are validate
    
    # this is my "pay around"
    # print('to printuje', request, '. data to ', request.data)
    # print(serializer)
    
    serializer.is_valid(raise_exception=True)
    #if this is succesfull:
    user= serializer.validated_data['user']

    created, token = AuthToken.objects.create(user) # insteaf create we can stay with _,

    return response.Response ({
        'user_info': {
            'id': user.id,
            'email': user.email,
            'First Name': user.first_name,
            'last_name': user.last_name,            
        },
        'token': token
    }
    )
@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return response.Response ({
            'user_info': {
            'id': user.id,
            'First Name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        },        
        })
    # if user is not authenticated
    return response.Response ({'error': 'you dont have acces, login'}, status=400)


@api_view(['POST'])
def register_api(request):
    serializer = user_serializer.RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    created, token = AuthToken.objects.create(user) # insteaf create we can stay with _,

    # with emaill add security-> send email only when user create

    ''' sending email manualy'''
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'info@sharpmind.club',
    #     ['o.perez1187@gmail.com'],
    #     fail_silently=False,
    # )
    ''' sending email with a templete'''
    msg = EmailMessage(
        from_email='info@sharpmind.club',
        to=['o.perez1187@gmail.com'],
    )
    # content
    title_mail = 'Perez'
    title_chess = 'my GM!'
    verify_my_email = "VERIFY!"
    my_site = "http://127.0.0.1:8000/"
    absurl = "http://127.0.0.1:8000/email-verify/?token="+str(token)


    msg.template_id = "d-c50d4fd610f944299e859d66d9d6201f"
    msg.dynamic_template_data = {
        "title": title_mail,
        "title_chess":title_chess,
        "verify_my_email":verify_my_email,
        "my_site":my_site,
        "verification_url":absurl,
    }
    # msg.send(fail_silently=False)


    return response.Response ({
        'user_info': {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 
        'token': token
        }
        )




# this class doesnt work
class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        # token = request.query_params['token']
        print(' ten token wolasz', token)



# this clas is not active:
class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 

        # data= serializer.validated_data

        # print('printuje: ',data)

        user = serializer.save()

        return response.Response ({
            'user_info': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, 
            'token': "token soon"
            }
            )

