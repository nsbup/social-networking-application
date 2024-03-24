from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateUserAPIView.as_view(), name='get_post_users'),
    # # path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    # path('search', views.ListCreateMovieAPIView.as_view(), name='get_search_friend'),
    path('friend-request-list', views.FriendRequestListAPIView.as_view(), name='get_friend_request_list'),
    path('friend-list', views.FriendsListAPIView.as_view(), name='get_friend_list'),
    path('friend-request-post', views.CreateFriendRequestAPIView.as_view(), name='post_friend_request'),
    path('friend-request-accept', views.AcceptRequestAPIView.as_view(), name='post_friend_request_accept'),
    path('friend-request-reject/<int:pk>', views.RejectRequestAPIView.as_view(), name='post_friend_request_reject'),
    path('user-detail/<int:pk>/highlight/',views.SnippetHighlight.as_view(),name='user-detail'),
]