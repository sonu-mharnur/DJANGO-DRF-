from django.urls import path
from . import views
from .views import studentAPI
from .views import RegisterUser

urlpatterns = [

    

    # path('', views.home, name='home'),
    # path('student/', views.post_student, name='home'),
    # path('updata/<id>', views.update_student, name='home'),
    # path('delete/', views.delete_student, name='home'),
    path('get-book/', views.get_book, name='home'),
    path('student/', views.studentAPI.as_view(), name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    
]