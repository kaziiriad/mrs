from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import *

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)


urlpatterns = [
    # path('login', LoginView.as_view(), name='login'),
    # path('logout', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    # path('token-refresh/',
    #      jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
