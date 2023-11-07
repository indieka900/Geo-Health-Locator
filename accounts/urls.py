from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('community-member/', views.create_community_member, name='register-community-member'),
    path('user-reqistration/', views.create_user, name='register-user'),
]
