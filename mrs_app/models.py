from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password):
        user = self.create_user(
            email,
            name=name,
            phone=phone,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.email


GENRE_CHOICE = [
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Romantic', 'Romantic'),
    ('Crime', 'Crime'),
    ('Thriller', 'Thriller'),
    
]
RATING_CHOICE = [
    ("U", "Universal"),
    ("R", "Restricted"),
    ("PG", "Parental Guidence"),

]
class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICE, blank=True, null=True)
    rating = models.CharField(max_length=50, choices=RATING_CHOICE, null=True)
    release_date = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} - {self.release_date}'
    
    def get_average_rating(self):
        ratings = 0.0
        
        for r in self.num_rating.all(): # type: ignore
            ratings += float(r.rating)
        
        average_rating = ratings / self.num_rating.all().count() # type: ignore
        return average_rating

class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, related_name='num_rating', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f'{self.rating}/5.0 rating for {self.movie_id.name}'

    