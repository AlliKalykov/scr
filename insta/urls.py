from django.urls import path
from .views import home, redirectview, HomeView,redirecthomeclass, CountryView, CoutryUpdate

# apps_name = 'insta'

urlpatterns = [
    path('', home, name='home-name'),
    path('redirect/', redirectview, name='redirect-name'),
    path('homeclass/', HomeView.as_view(), name='home-class'),
    path('redirecthomeclass/', redirecthomeclass, name='redirect-home-class'),
    path('country/<int:pk>/', CoutryUpdate.as_view(), name='country-update'),
    path('country/', CountryView.as_view(), name='country'),
]
