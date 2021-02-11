from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_view, name='create_view'),
    path('data/', views.Retrieve_ListView, name='Retrieve_ListView'),
    path('data/<int:_id>', views.Retrieve_DetailView, name='Retrieve_DetailView'),
    path('data/<int:_id>/delete', views.DeleteView, name='DeleteView'),
    path('data/<int:_id>/update', views.UpdateView, name='UpdateView')

]