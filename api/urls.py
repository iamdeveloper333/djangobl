from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
     path('PostApi/', views.PostViewList.as_view()),
     path('PostApi/<int:pk>', views.PostViewDetails.as_view()),
     path('AdmitCardsApi/', views.AdmitCardsViewList.as_view()),
     path('AdmitCardsApi/<int:pk>', views.AdmitCardsViewDetails.as_view()),
     path('ResultApi/', views.ResultViewList.as_view()),
     path('EmailsApi/', views.EmailsViewList.as_view()),
     path('TestApi/', views.TestViewList.as_view()),
     path('AptitudeTestApi/', views.AptitudeTestViewList.as_view()),  
     path('AptitudeTestApi/<int:pk>', views.AptitudeTestViewDetails.as_view()), 
     path('EnglishTestApi/', views.EnglishTestViewList.as_view()),  
     path('EnglishTestApi/<int:pk>', views.EnglishTestViewDetails.as_view()), 
     path('ReasoningTestApi/', views.ReasoningTestViewList.as_view()),  
     path('ReasoningTestApi/<int:pk>', views.ReasoningTestViewDetails.as_view()),   
     path('ResultApi/<int:pk>', views.ResultViewDetails.as_view()),
     path('BlogsApi/', views.BlogsViewList.as_view()),
     path('UserBlogsApi/', views.UserBlogsList.as_view()),
     path('SaveBlogsApi/', views.SaveBlogList.as_view()),
     path('BlogsApi/<int:pk>', views.BlogsViewDetails.as_view()),
     path('SaveJobApi/<int:pk>', views.SaveJobsViewDetails.as_view()),
     path('SaveJobsListApi/', views.SaveJobList.as_view()),
     # path('current_user/', views.current_user),
     # path('users/', views.UserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)



