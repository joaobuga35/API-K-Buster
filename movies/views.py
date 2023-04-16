from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import EmployeePermission
from movies.serializers import MovieSerializer
from movies.models import Movie

# Create your views here.


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [EmployeePermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        ...

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        ...
