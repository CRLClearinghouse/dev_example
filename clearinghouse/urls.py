from django.urls import path
from .views import *

app_name = 'clearinghouse'

urlpatterns = [
    path('', index_view, name='index'),
    path('setup', setup_view, name='setup'),
    path('import', import_view, name='import'),
]
