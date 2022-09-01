from rest_framework import views, response, exceptions, permissions
from rest_framework.decorators import api_view

from . import serializer as user_serializer
from knox.auth import AuthToken

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

