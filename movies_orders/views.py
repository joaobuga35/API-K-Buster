from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies_orders.permissions import AuthenticatedPermission
from movies_orders.serializers import MovieOrderSerializer
from movies.models import Movie

# Create your views here.


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthenticatedPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        return Response("Oi")

    def post(self, request: Request, movie_id: int) -> Response:
        movie_obj = get_object_or_404(Movie, pk=movie_id)
        self.check_object_permissions(request, movie_obj)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie_obj, user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        ...
