from django.urls import path

from .views import (
    index, 
    show, 
    create, 
    update,
    delete
)

app_name = 'todo'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', show, name='show'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]