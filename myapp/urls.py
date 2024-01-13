# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),  # This corresponds to the Flask @app route('/')
    path('index/', views.register, name='register'),  # This corresponds to the Flask @app route('/form')
    # path('dashboard/get_users/', views.get_users, name='get_users'),  # This corresponds to the Flask @app route('/get_users')
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('get_users/', views.get_users, name='get_users'),
    path('login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='logout'),
    path('restricted/',views.restricted_page, name='restricted_page'),
    path('similar_user/',views.find_similar_users, name='find_similar_users'),
    # path('api/similar-users/<int:user_id>/', views.get_similar_users, name='get_similar_users')
    # path('similar-user/<int:user_id>/', views.view_similar_user_profile, name='view_similar_user_profile')
    path('user/', views.view_similar_user_profile, name='view_similar_user_profile'),
    path('confirm_email/<uuid:token>', views.confirm_email, name='confirm_email'),
    path('update_interests/', views.update_interests, name='update_interests'),
    path('resend_confirmation/', views.resend_confirmation, name='resend_confirmation'),
    path('api/facebook_login/', views.facebook_login, name='facebook_login'),
    path('google_login/', views.google_login, name='google_login')
    
]
