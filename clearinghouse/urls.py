from django.urls import path
from .views import *

app_name = 'clearinghouse'

urlpatterns = [
    path('', index_view, name='index'),
]
