from django.urls import path
from . import views

urlpatterns = [
    path('', views.ComputerListView.as_view(), name='computer_list'),
    path('<int:pk>/', views.ComputerDetailView.as_view(), name='computer_detail'),
    path('new/', views.ComputerCreateView.as_view(), name='computer_create'),
    path('<int:pk>/update/', views.ComputerUpdateView.as_view(), name='computer_update'),
    path('<int:pk>/delete/', views.ComputerDeleteView.as_view(), name='computer_delete'),
]