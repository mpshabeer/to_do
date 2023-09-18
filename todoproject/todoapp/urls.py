
from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('detail/<int:pk>/',views.DetailListView.as_view(),name="detail"),
    path('updateof/<int:pk>/', views.TaskUpdate.as_view(), name="updateof"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview',views.TaskListView.as_view(),name='listview'),

    path('DeleteView/<int:pk>/', views.DeleteView.as_view(), name='DeleteView'),

        ]