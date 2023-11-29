from .import views
from django.urls import path, include

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('contact/',views.contact, name='contact'),
    path('studentlogin/',views.studentlogin, name='studentlogin'),
    # path('student/',views.student, name='student'),
]
