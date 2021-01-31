from django.urls import path
from workers import views

urlpatterns = [
    path('', views.WorkersList.as_view(), name='worker_list'),
    path('view/<int:pk>/', views.WorkerDetail.as_view(), name='worker_view'),
    path('new/', views.WorkerCreate.as_view(), name='worker_new'),
    path('edit/<int:pk>/', views.WorkerUpdate.as_view(), name='worker_edit'),
    path('delete/<int:pk>/', views.WorkerDelete.as_view(), name='worker_delete'),
] 
