from django.urls import path
from .views import home, redirectview, HomeView,redirecthomeclass

# apps_name = 'insta'

urlpatterns = [
    path('', home, name='home-name'),
    path('redirect/', redirectview, name='redirect-name'),
    path('homeclass/', HomeView.as_view(), name='home-class'),
    path('redirecthomeclass/', redirecthomeclass, name='redirect-home-class'),
]
