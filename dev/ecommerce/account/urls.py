from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    
    # Email verification

    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),

    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),

    path('email-verification-success', views.email_verification_success, name='email-verification-success'),

    path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),

    # Login

    path('my-login/', views.my_login, name='my-login'),

    # path('my-logout/', views.my_logout, name='my-logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
]