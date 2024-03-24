from authentication import serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView,UpdateAPIView,GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Friends,Requests
from .permissions import IsOwnerOrReadOnly
from .serializers import FriendsListSerializer, FriendsSerializer,RequestsSerializer
from .filters import UserFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework import renderers


from .serializers import UserSerializer
from .pagination import CustomPagination

from django.contrib.auth.models import User

class ListCreateUserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('keyword')
        if keyword:
            if '@' in keyword:
                queryset = queryset.filter(email__iexact=keyword)
            else:
                queryset = queryset.filter(username__icontains=keyword)
        return queryset

class CreateFriendRequestAPIView(ListCreateAPIView):
    serializer_class = RequestsSerializer
    queryset = Requests.objects.all()
    permission_classes = [IsAuthenticated]
    # pagination_class = CustomPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        

        if serializer.is_valid:
            serializer.save()


class AcceptRequestAPIView(ListCreateAPIView):
    serializer_class = FriendsSerializer
    queryset = Friends.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.validated_data['status'] = 'Accept'
        if serializer.is_valid:
            serializer.save()

class RejectRequestAPIView(
    UpdateAPIView):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        print("perform_update::")
        serializer.validated_data['status'] = 'REJECTED'
        if serializer.is_valid:
            instance = serializer.save()




class FriendsListAPIView(ListCreateAPIView):
    serializer_class = FriendsSerializer
    # queryset = Friends.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    def get_queryset(self):
        print(self.request.headers)
        source_user = self.request.data.get('source_user')
        queryset = Friends.objects.filter(source_user=source_user)
        return queryset
    
    
class FriendRequestListAPIView(ListCreateAPIView):
    serializer_class = RequestsSerializer
    # queryset = Friends.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    def get_queryset(self):
        source_user = self.request.data.get('source_user')
        print("source_user",source_user)
        queryset = Requests.objects.filter(source_user=source_user,status = "PENDING")
        return queryset
    

class SnippetHighlight(GenericAPIView):
    queryset = User.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.username)