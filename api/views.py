from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse,Http404
from api.models import Post,AdmitCards,Result,Emails,Test,AptitudeTest,Blogs, UserBlog,ReasoningTest,EnglishTest
from api.serializers import PostSerialiazers
from api.serializers import AdmitCardsSerialiazers
from api.serializers import ResultSerialiazers
from api.serializers import EmailsSerialiazers
from api.serializers import TestSerialiazers
from api.serializers import AptitudeTestSerialiazers,EnglishTestSerialiazers,ReasoningTestSerialiazers
from api.serializers import BlogsSerialiazers, UserBlogSerializers

# from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny, IsAuthenticated

# from api.serializers import UserSerializer, UserSerializerWithToken


from api.filters import (
    PostFilter,AdmitCardsFilter,ResultFilter,BlogsFilter
)



# from api.filters import PostFilter

# Create your views here.

class PostViewList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = PostFilter

class PostViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers

class AdmitCardsViewList(generics.ListCreateAPIView):
    queryset = AdmitCards.objects.all()
    serializer_class = AdmitCardsSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = AdmitCardsFilter

class EmailsViewList(generics.ListCreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerialiazers

class AdmitCardsViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdmitCards.objects.all()
    serializer_class = AdmitCardsSerialiazers

class ResultViewList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = ResultFilter

class ResultViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerialiazers

class TestViewList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerialiazers

# class AptitudeTestViewList(generics.ListCreateAPIView):
#     queryset = AptitudeTest.objects.all()
#     serializer_class = AptitudeTestSerialiazers


        






# class BlogsViewList(generics.ListAPIView):
#     model = Blogs
#     permission_classes = (IsAuthenticated,)
#     serializer_class = BlogsSerialiazers
#     filter_backends = (DjangoFilterBackend,)
#     filter_class = BlogsFilter

#     def get_queryset(self):
#         return Blogs.objects.all()






# @api_view(['GET'])
# def current_user(request):
   
    
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)


# class UserList(APIView):
    
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AptitudeTestViewList(generics.ListAPIView):
    model = AptitudeTest
    permission_classes = (AllowAny,)
    serializer_class = AptitudeTestSerialiazers

    def get_queryset(self):
        return AptitudeTest.objects.all()
    

class AptitudeTestViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AptitudeTest.objects.all()
    serializer_class = AptitudeTestSerialiazers

    
class EnglishTestViewList(generics.ListAPIView):
    model = EnglishTest
    permission_classes = (AllowAny,)
    serializer_class = EnglishTestSerialiazers

    def get_queryset(self):
        return EnglishTest.objects.all()
    

class EnglishTestViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnglishTest.objects.all()
    serializer_class = EnglishTestSerialiazers

    
class ReasoningTestViewList(generics.ListAPIView):
    model = ReasoningTest
    permission_classes = (AllowAny,)
    serializer_class = ReasoningTestSerialiazers

    def get_queryset(self):
        return ReasoningTest.objects.all()
    

class ReasoningTestViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReasoningTest.objects.all()
    serializer_class = ReasoningTestSerialiazers

class BlogsViewList(generics.ListAPIView):
    model = Blogs
    permission_classes = (AllowAny,)
    serializer_class = BlogsSerialiazers

    def get_queryset(self):
        return Blogs.objects.all()
    

class BlogsViewDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        blog_data = {}
        blog_data['blog'] = pk
        blog_data['profile'] = request.user.id
        try:
            UserBlog.objects.get(blog=pk)
            return Response({
                'message': 'Already Exist'
            }, status=status.HTTP_403_FORBIDDEN)
        except:
            userblog_serialiazer = UserBlogSerializers(data=blog_data)
            if userblog_serialiazer.is_valid():
                userblog_serialiazer.save()
        return Response({'data': userblog_serialiazer.data}, status=status.HTTP_200_OK)



class UserBlogsList(generics.ListAPIView):
    model = UserBlog
    permission_classes = (IsAuthenticated,)
    serializer_class = UserBlogSerializers

    def get_queryset(self):
        user = self.request.user
        return UserBlog.objects.filter(profile=user)