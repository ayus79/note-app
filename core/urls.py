from django.urls import path, include
from . import views
from core.admin import *

admin.site.site_header = 'Notes Admin Portal'

urlpatterns = [
    path('', views.homepage, name='index'),
    path('add/', views.add, name='add'),
    path('updatepage/<str:id>', views.updatepage, name='updatepage'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
]
