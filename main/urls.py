from django.urls import path
from .views import index, signup, login_


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_, name='login'),
    path('sign-up/', signup, name='signup'),
]
