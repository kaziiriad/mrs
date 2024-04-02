import json
from mrs_app.models import Movie, Rating, User

def populate_user():
    with open('populate/users.json') as f:
        users = json.load(f)

    for user in users:

        new_user = User.objects.create(
            name=user['name'],
            phone=user['phone'],
            password=user['password'],
            email=user['email'],
        )
        new_user.save()

    print('Users Successfully populated')

def populate_movie():
    with open('populate/movies.json') as f:
        movies = json.load(f)
    
    for movie in movies:

        new_movie = Movie.objects.create(
            name=movie['name'],
            genre=movie['genre'],
            rating=movie['rating'],
            release_date=movie['release_date'],
        )
        new_movie.save()
    
    print('movies Successfully populated')

def populate_rating():
    with open('populate/ratings.json') as f:
        ratings = json.load(f)

    for _rating in ratings:
        user = User.objects.get(id=_rating['user_id'])
        movie = Movie.objects.get(id=_rating['movie_id'])
        new_rating = Rating.objects.create(
            user_id=user,
            movie_id=movie,
            rating=_rating['rating:'],
        )
        new_rating.save()
    
    print('ratings Successfully populated')

