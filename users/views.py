from rest_framework.views import APIView, Request, Response, status
from users.serializers import UserSerializer
from users.models import User

# Create your views here.


class UserView(APIView):
    def get(self, request: Request) -> Response:
        ...

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        ...
