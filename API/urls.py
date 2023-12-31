from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/<str:pk>/update', views.updateNote),
    path('notes/<str:pk>/delete', views.deleteNotes),
    path('notes/create/', views.createNotes),
    path('notes/<str:pk>', views.getnotes),
]