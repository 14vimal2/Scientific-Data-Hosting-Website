from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, ),
    path('data/', views.data_page, name='data_page'),
    path('get_dataset/', views.get_dataset, name='data_table'),
    path('download/', views.send_file, name='download'),
    path('docs/', views.docs_page, name='docs_page'),
    path('*/*', views.home_page, name='home_page')
]