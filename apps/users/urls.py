from django.urls import path
from apps.users.views import (
    UserBlockView,
    UserListCreateView,
    UserToAdminView,
    UserToUserView,
    UserUnBlockView,
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('<int:pk>/to_admin/', UserToAdminView.as_view(), name='user_to_admin'),
    path('<int:pk>/to_user/', UserToUserView.as_view(), name='user_to_user'),
    path('<int:pk>/block/', UserBlockView.as_view(), name='user_block'),
    path('<int:pk>/unblock/', UserUnBlockView.as_view(), name='user_unblock'),
]