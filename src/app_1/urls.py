from django.urls import path
from .views import hello_view as hello


app_name = 'app_1'

urlpatterns = [
    path('',hello.hello_world,name="hello_view_name"),
    
]
