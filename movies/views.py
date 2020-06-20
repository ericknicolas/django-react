from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User

from .serializers import MovieSerializer, RatingSerializer
from .models import Movie, Rating

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
        
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                
                serializer = RatingSerializer(rating, many=False)
                response = {'message':'rating updated', 'result':serializer.data}
                return Response(data=response, status=status.HTTP_200_OK)

            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)

                serializer = RatingSerializer(rating, many=False)
                response = {'message':'rating created', 'result':serializer.data}
                return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {'message':'you need to provide stars'}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
