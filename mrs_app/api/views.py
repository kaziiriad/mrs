# from django.contrib.auth import authenticate, login, logout
# from .utils import get_tokens_for_user

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import generics
from rest_framework import filters

from .serializers import MovieSerializer, RatingSerializer
from ..models import Movie, Rating

from django.shortcuts import get_object_or_404
from django.db.models import Avg


# class LoginView(APIView):
#     def post(self, request):
#         if 'email' not in request.data or 'password' not in request.data:
#             return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             auth_data = get_tokens_for_user(request.user)
#             return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
#         return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

      
# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    
class MovieDetailView(APIView):
    def get(self, request):
        movie_name = request.query_params.get('name', None)
        if movie_name is None:
            return Response({"message": "Movie name not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            movie = Movie.objects.get(name__iexact=movie_name)
            serializer = MovieSerializer(movie)
            average_rating = movie.get_average_rating() # type: ignore
            return Response({"movie_details": serializer.data, "average_rating": average_rating}, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)


class RatingViewSet(ModelViewSet):    
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    # def get_queryset(self):
        
    #     pass
