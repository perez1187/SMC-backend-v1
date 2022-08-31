from rest_framework import views, response, exceptions, permissions
from rest_framework.decorators import api_view

from . import serializer as user_serializer

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

