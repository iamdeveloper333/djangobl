from django.contrib import admin
from .models import Post
from .models import ImportantDates
from .models import ApplicationFee
from .models import Eligibility
from .models import AgeLimit,SaveUserBlog,SaveUserJob
from .models import VacancyDetail,AdmitCards,Result,Emails,Test,Question,AptitudeTest,Blogs,ReasoningTest,RQuestion,RTest,EnglishTest,EQuestion,ETest

admin.site.register(Post)
admin.site.register(ImportantDates)
admin.site.register(ApplicationFee)
admin.site.register(Eligibility)
admin.site.register(AgeLimit)
admin.site.register(VacancyDetail)
admin.site.register(AdmitCards)
admin.site.register(Result)
admin.site.register(Emails)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(AptitudeTest)
admin.site.register(ETest)
admin.site.register(EQuestion)
admin.site.register(EnglishTest)
admin.site.register(RQuestion)
admin.site.register(ReasoningTest)
admin.site.register(RTest)
admin.site.register(Blogs)
admin.site.register(SaveUserBlog)
admin.site.register(SaveUserJob)