from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse,Http404
from api.models import SaveUserJob,SaveUserBlog,Post,AdmitCards,Result,Emails,Test,AptitudeTest,Blogs, UserBlog,ReasoningTest,EnglishTest
from api.serializers import PostSerialiazers
from api.serializers import AdmitCardsSerialiazers
from api.serializers import ResultSerialiazers
from api.serializers import EmailsSerialiazers
from api.serializers import TestSerialiazers
from api.serializers import AptitudeTestSerialiazers,EnglishTestSerialiazers,ReasoningTestSerialiazers
# ,UserSaveJobSerializers
from api.serializers import BlogsSerialiazers, UserBlogSerializers,SaveUserBlogSerializers,SaveUserJobSerializers

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
    model = Post
    permission_classes = (AllowAny,)
    serializer_class = PostSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = PostFilter

    def get_queryset(self):
        return Post.objects.all()

class PostViewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerialiazers

class AdmitCardsViewList(generics.ListCreateAPIView):
    model = AdmitCards
    permission_classes = (AllowAny,)
    serializer_class = AdmitCardsSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = AdmitCardsFilter

    def get_queryset(self):
        return AdmitCards.objects.all()

class EmailsViewList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Emails.objects.all()
    serializer_class = EmailsSerialiazers

class AdmitCardsViewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = AdmitCards.objects.all()
    serializer_class = AdmitCardsSerialiazers

class ResultViewList(generics.ListCreateAPIView):
    model = Result
    permission_classes = (AllowAny,)
    serializer_class = ResultSerialiazers
    filter_backends = (DjangoFilterBackend,)
    filter_class = ResultFilter
    def get_queryset(self):
        return Result.objects.all()

class ResultViewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Result.objects.all()
    serializer_class = ResultSerialiazers

class TestViewList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
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






   
class AptitudeTestViewList(generics.ListAPIView):
    model = AptitudeTest
    permission_classes = (AllowAny,)
    serializer_class = AptitudeTestSerialiazers

    def get_queryset(self):
        return AptitudeTest.objects.all()
    

class AptitudeTestViewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = AptitudeTest.objects.all()
    serializer_class = AptitudeTestSerialiazers

    
class EnglishTestViewList(generics.ListAPIView):
    model = EnglishTest
    permission_classes = (AllowAny,)
    serializer_class = EnglishTestSerialiazers

    def get_queryset(self):
        return EnglishTest.objects.all()
    

class EnglishTestViewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = EnglishTest.objects.all()
    serializer_class = EnglishTestSerialiazers

    
class ReasoningTestViewList(generics.ListAPIView):
    model = ReasoningTest
    permission_classes = (AllowAny,)
    serializer_class = ReasoningTestSerialiazers

    def get_queryset(self):
        return ReasoningTest.objects.all()
    

class ReasoningTestViewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = ReasoningTest.objects.all()
    serializer_class = ReasoningTestSerialiazers

class BlogsViewList(generics.ListAPIView):
    model = Blogs
    permission_classes = (AllowAny,)
    serializer_class = BlogsSerialiazers

    def get_queryset(self):
        return Blogs.objects.all()


class SaveJobsViewDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        job_data = {}
        job_data['job'] = pk
        job_data['profile'] = request.user.id
        try:
            SaveUserJob.objects.filter(profile=request.user.id).get(job=pk)
            return Response({
                'message': 'Already Exist'
            }, status=status.HTTP_403_FORBIDDEN)
        except:        
            serializer = SaveUserJobSerializers(data=job_data)
            if serializer.is_valid():
                serializer.save() 
                print(SaveUserJob.objects.all())
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogsViewDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        blog_data = {}
        blog_data['blog'] = pk
        blog_data['profile'] = request.user.id
        try:
            SaveUserBlog.objects.filter(profile=request.user.id).get(blog=pk)
            return Response({
                'message': 'Already Exist'
            }, status=status.HTTP_403_FORBIDDEN)
        except:        
            serializer = SaveUserBlogSerializers(data=blog_data)
            if serializer.is_valid():
                serializer.save() 
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserBlogsList(generics.ListAPIView):
    model = UserBlog
    permission_classes = (IsAuthenticated,)
    serializer_class = UserBlogSerializers

    def get_queryset(self):
        user = self.request.user
        return UserBlog.objects.filter(profile=user)


class SaveBlogList(generics.ListAPIView):
    model = SaveUserBlog
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveUserBlogSerializers

    def get_queryset(self):
        user = self.request.user
        return SaveUserBlog.objects.filter(profile=user)

class SaveJobList(generics.ListAPIView):
    model = SaveUserJob
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveUserJobSerializers

    def get_queryset(self):
        user = self.request.user
        return SaveUserJob.objects.filter(profile=user)



# class SaveJobViewDetails(APIView):
#     permission_classes = (IsAuthenticated,)    
#     def put(self, request, pk):
       
#         job_data = {}
#         job_data['job'] = pk        
#         job_data['profile'] = request.user.id
#         print('job_data',job_data['job'] ,job_data['profile'] )
#         try:
#             UserSaveJob.objects.get(job=pk)
            
#             return Response({
#                 'message': 'Already Exist'
#             }, status=status.HTTP_403_FORBIDDEN)
#         except:
#             print('inside user1')
#             userjob_serialiazer = UserSaveJobSerializers(data=job_data)
#             if userjob_serialiazer.is_valid():
#                 userjob_serialiazer.save()
#         return Response({'data': userjob_serialiazer.data}, status=status.HTTP_200_OK)




# class UserSaveJobList(generics.ListAPIView):
#     model = UserSaveJob
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSaveJobSerializers

#     def get_queryset(self):
#         user = self.request.user
#         return UserSaveJob.objects.filter(profile=user)