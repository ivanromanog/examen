from django.urls import path
from apps import views

urlpatterns=[
    path('', views.index),
    path('main', views.index),
    path('create', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('addItem', views.addItem),
    path('createItem', views.createItem),
    path('delete/<num>', views.deleteItem),
    path('addList/<num>', views.addList),
    path('removeList/<num>', views.removeList),
    path('wish_items/<num>', views.itemView),
]