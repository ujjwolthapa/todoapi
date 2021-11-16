from django.urls import path
from .import views

urlpatterns=[
    path('',views.getRoutes,name="getroute"),
    path('notes/',views.getNotes,name="getnotes"),
    path('notes/create/',views.createNote),
    path('notes/<str:pk>/update',views.updateNote),
    path('notes/<str:pk>/delete',views.deleteNote),
    path('notes/<str:pk>/',views.getNote,name="getnote"),
    


]