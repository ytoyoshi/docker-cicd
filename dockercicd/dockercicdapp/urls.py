from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view,home_view, logout_user, signup, logout_confirmation_view, message_list, message_create, message_delete, MessageDetailAPIView

urlpatterns = [
    path('', login_view.as_view(), name='login'),
    path('login/', login_view.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('logout_confirmation/', logout_confirmation_view, name='logout_confirmation'),
    path('signup/', signup, name='signup'),
    path('home/', home_view, name='home'),
    path('message/', message_list, name='message'),
    path('message/create/', message_create, name='message_create'),
    path('message/delete/<int:pk>/', message_delete, name='message_delete'),
    path('api/getMessage/<int:pk>/', MessageDetailAPIView.as_view(), name='message_detail_api'),
]