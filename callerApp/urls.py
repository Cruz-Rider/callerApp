from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.APIRoot.as_view(), name='api-root'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('users/', views.RegisteredUserView.as_view(), name='user'),
    path('contacts/', views.ContactListCreateView.as_view(), name='contacts'),
    path('search/', views.SearchView.as_view(), name='search'),
]

urlpatterns += router.urls