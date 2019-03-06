from rest_framework import serializers
from .models import Post
from .models import ImportantDates
from .models import ApplicationFee
from .models import Eligibility
from .models import AgeLimit
from .models import VacancyDetail
from .models import AdmitCards
from .models import Result,SaveUserBlog,SaveUserJob
from .models import Emails,Question,Test,AptitudeTest,Blogs, UserBlog,RQuestion,ReasoningTest,RTest,EnglishTest,ETest,EQuestion
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

class ImportantDatesSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = ImportantDates
        fields = ('id','text','content')


class ApplicationFeeSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = ApplicationFee
        fields = ('id','text','content')

class EligibilitySerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = Eligibility
        fields = ('id','text','content')

class AgeLimitSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = AgeLimit
        fields = ('id','text','content')

class VacancyDetailSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = VacancyDetail
        fields = ('id','text','content')


class PostSerialiazers(serializers.ModelSerializer):
    importantdates_set = ImportantDatesSerialiazers(many=True)
    applicationfee_set =  ApplicationFeeSerialiazers(many=True)
    eligibility_set =  EligibilitySerialiazers(many=True)
    agelimit_set =  AgeLimitSerialiazers(many=True)
    vacancydetail_set =  VacancyDetailSerialiazers(many=True)
    def create(self,validated_data):        
        # job_like_status = validated_data.get("job_like_status")
        post_title = validated_data.get("post_title")
        post_by = validated_data.get("post_by")
        published_date = validated_data.get("published_date")
        last_date = validated_data.get("last_date")
        apply = validated_data.get("apply")
        notification = validated_data.get("notification")
        syllabus = validated_data.get("syllabus")
        o_website = validated_data.get("o_website")
        extra_info = validated_data.get("extra_info")
        short_description = validated_data.get("short_description")
        state = validated_data.get("state")
        qualification = validated_data.get("qualification")
        category = validated_data.get("category")
        new_obj = Post.objects.create(post_title=post_title,post_by=post_by,published_date=published_date,last_date=last_date,
        short_description=short_description,state=state,qualification=qualification,
        category=category,apply=apply,notification=notification,
        syllabus=syllabus,o_website=o_website,extra_info=extra_info
        )
        all_importantdates = validated_data.get('importantdates_set')
        if all_importantdates:
            for each_importantdates in all_importantdates:
                text = each_importantdates.get('text')
                content = each_importantdates.get('content')
                new_obj.importantdates_set.create(text=text, content=content)
        all_applicationfee = validated_data.get('applicationfee_set')
        if all_applicationfee:
            for each_applicationfee in all_applicationfee:
                text = each_applicationfee.get('text')
                content = each_applicationfee.get('content')
                new_obj.applicationfee_set.create(text=text, content=content)
        all_eligibility = validated_data.get('eligibility_set')
        if all_eligibility:
            for each_eligibility in all_eligibility:
                text = each_eligibility.get('text')
                content = each_eligibility.get('content')
                new_obj.eligibility_set.create(text=text, content=content)

        all_agelimit = validated_data.get('agelimit_set')
        if all_agelimit:
            for each_agelimit in all_agelimit:
                text = each_agelimit.get('text')
                content = each_agelimit.get('content')
                new_obj.agelimit_set.create(text=text, content=content)
        all_vacancydetail = validated_data.get('vacancydetail_set')
        if all_vacancydetail:
            for each_vacancydetail in all_vacancydetail:
                text = each_vacancydetail.get('text')
                content = each_vacancydetail.get('content')
                new_obj.vacancydetail_set.create(text=text, content=content)
        return new_obj

    def update(self,instance,validated_data):
        # instance.job_like_status = validated_data.get("job_like_status",instance.job_like_status)
        instance.post_title = validated_data.get("post_title",instance.post_title)
        instance.post_by = validated_data.get("post_by",instance.post_by)
        instance.published_date = validated_data.get("published_date",instance.published_date)
        instance.last_date = validated_data.get("last_date",instance.last_date)
        instance.short_description = validated_data.get("short_description",instance.short_description)
        instance.apply = validated_data.get("apply",instance.apply)
        instance.notification = validated_data.get("notification",instance.notification)
        instance.syllabus = validated_data.get("syllabus",instance.syllabus)
        instance.extra_info = validated_data.get("extra_info",instance.extra_info)
        instance.o_website = validated_data.get("o_website",instance.o_website)
        instance.state = validated_data.get("state",instance.state)
        instance.qualification = validated_data.get("qualification",instance.qualification)
        instance.category = validated_data.get("category",instance.category)
        all_importantdates = validated_data.get("importantdates_set")
        if all_importantdates:
            instance.importantdates_set.all().delete()
            for each_importantdates in all_importantdates:
                instance.importantdates_set.create(text=each_importantdates.get('text'),
                                          content=each_importantdates.get('content')
                                          )

        all_applicationfee = validated_data.get("applicationfee_set")
        if all_applicationfee:
            instance.applicationfee_set.all().delete()
            for each_applicationfee in all_applicationfee:
                instance.applicationfee_set.create(text=each_applicationfee.get('text'),
                                          content=each_applicationfee.get('content')
                                          )
        all_eligibility = validated_data.get("eligibility_set")
        if all_eligibility:
            instance.eligibility_set.all().delete()
            for each_eligibility in all_eligibility:
                instance.eligibility_set.create(text=each_eligibility.get('text'),
                                          content=each_eligibility.get('content')
                                          )
        all_agelimit = validated_data.get("agelimit_set")
        if all_agelimit:
            instance.agelimit_set.all().delete()
            for each_agelimit in all_agelimit:
                instance.agelimit_set.create(text=each_agelimit.get('text'),
                                          content=each_agelimit.get('content')
                                          )
        all_vacancydetail = validated_data.get("vacancydetail_set")
        if all_vacancydetail:
            instance.vacancydetail_set.all().delete()
            for each_vacancydetail in all_vacancydetail:
                instance.vacancydetail_set.create(text=each_vacancydetail.get('text'),
                                          content=each_vacancydetail.get('content')
                                          )

        instance.save()
        return instance

    class  Meta:
        model = Post
        fields = ('id','post_title', 'post_by' ,'short_description', 'published_date','last_date','importantdates_set','state','qualification','category','applicationfee_set','eligibility_set','agelimit_set','vacancydetail_set','apply','notification','extra_info','o_website','syllabus')

class AdmitCardsSerialiazers(serializers.ModelSerializer):

    def update(self,instance,validated_data):
        instance.post_title = validated_data.get("post_title",instance.post_title)
        instance.post_by = validated_data.get("post_by",instance.post_by)
        instance.apply_link = validated_data.get("apply_link",instance.apply_link)
        instance.img_link = validated_data.get("img_link",instance.img_link)

        instance.save()
        return instance


    class  Meta:
        model = AdmitCards
        fields = ('id','post_title','post_by','apply_link','img_link')

class ResultSerialiazers(serializers.ModelSerializer):

    def update(self,instance,validated_data):
        instance.post_title = validated_data.get("post_title",instance.post_title)
        instance.post_by = validated_data.get("post_by",instance.post_by)
        instance.view_link = validated_data.get("view_link",instance.view_link)
        instance.img_link = validated_data.get("img_link",instance.img_link)

        instance.save()
        return instance


    class  Meta:
        model = Result
        fields = ('id','post_title','post_by','view_link','img_link')

class EmailsSerialiazers(serializers.ModelSerializer):

    def update(self,instance,validated_data):
        instance.email = validated_data.get("email",instance.email)

        instance.save()
        return instance


    class  Meta:
        model = Emails
        fields = ('id','email')

class QuestionSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = Question
        fields = ('question_num','question','question_img_link','a1','a2','a3','a4','a5')

class EQuestionSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = Question
        fields = ('question_num','question','a1','a2','a3','a4','a5')
        
class RQuestionSerialiazers(serializers.ModelSerializer):
    class  Meta:
        model = Question
        fields = ('question_num','question','question_img_link','a1','a2','a3','a4','a5')


class TestSerialiazers(serializers.ModelSerializer):
    question_set = QuestionSerialiazers(many=True)
    def create(self,validated_data):
        test_title = validated_data.get("test_title")
        test_description = validated_data.get("test_description")
        test_category = validated_data.get("test_category")
        num_of_questions = validated_data.get("num_of_questions")
        time_for_test = validated_data.get("time_for_test")
        new_obj = Post.objects.create(num_of_questions=num_of_questions,time_for_test=time_for_test,test_title=test_title,
        test_description=test_description,test_category=test_category)

        all_questions = validated_data.get('question_set')
        if all_questions:
            for each_questions in all_questions:
                question = each_questions.get('question')
                question_num = each_questions.get('question_num')
                question_img_link = each_questions.get('question_img_link')
                a1 = each_questions.get('a1')
                a2 = each_questions.get('a2')
                a3 = each_questions.get('a3')
                a4 = each_questions.get('a4')
                a5 = each_questions.get('a5')
                new_obj.question_set.create(question_img_link=question_img_link,question_num=question_num,question=question, a1=a1, a2=a2,  a3=a3, a4=a4, a5=a5)

        return new_obj

    def update(self,instance,validated_data):
        instance.test_title = validated_data.get("test_title",instance.test_title)
        instance.test_description = validated_data.get("test_description",instance.test_description)
        instance.test_category = validated_data.get("test_category",instance.test_category)
        instance.num_of_questions = validated_data.get("num_of_questions",instance.num_of_questions)
        instance.time_for_test = validated_data.get("time_for_test",instance.time_for_test)

        all_questions = validated_data.get("question_set")
        if all_questions:
            instance.question_set.all().delete()
            for each_questions in all_questions:
                instance.question_set.create(question_num=each_questions.get('question_num'),
                                          question=each_questions.get('question'),
                                          question_img_link=each_questions.get('question_img_link'),
                                          a1=each_questions.get('a1'),
                                          a2=each_questions.get('a2'),
                                          a3=each_questions.get('a3'),
                                          a4=each_questions.get('a4'),
                                          a5=each_questions.get('a5'),
                                          )

        instance.save()
        return instance

    class  Meta:
        model = Test
        fields = ('id', 'num_of_questions', 'time_for_test','test_title','test_description','test_category','question_set')
     

class RTestSerialiazers(serializers.ModelSerializer):
    question_set = RQuestionSerialiazers(many=True)
    def create(self,validated_data):
        test_title = validated_data.get("test_title")
        test_description = validated_data.get("test_description")
        test_category = validated_data.get("test_category")
        num_of_questions = validated_data.get("num_of_questions")
        time_for_test = validated_data.get("time_for_test")
        new_obj = Post.objects.create(num_of_questions=num_of_questions,time_for_test=time_for_test,test_title=test_title,
        test_description=test_description,test_category=test_category)

        all_questions = validated_data.get('question_set')
        if all_questions:
            for each_questions in all_questions:
                question = each_questions.get('question')
                question_num = each_questions.get('question_num')
                question_img_link = each_questions.get('question_img_link')
                a1 = each_questions.get('a1')
                a2 = each_questions.get('a2')
                a3 = each_questions.get('a3')
                a4 = each_questions.get('a4')
                a5 = each_questions.get('a5')
                new_obj.question_set.create(question_img_link=question_img_link,question_num=question_num,question=question, a1=a1, a2=a2,  a3=a3, a4=a4, a5=a5)

        return new_obj

    def update(self,instance,validated_data):
        instance.test_title = validated_data.get("test_title",instance.test_title)
        instance.test_description = validated_data.get("test_description",instance.test_description)
        instance.test_category = validated_data.get("test_category",instance.test_category)
        instance.num_of_questions = validated_data.get("num_of_questions",instance.num_of_questions)
        instance.time_for_test = validated_data.get("time_for_test",instance.time_for_test)

        all_questions = validated_data.get("question_set")
        if all_questions:
            instance.question_set.all().delete()
            for each_questions in all_questions:
                instance.question_set.create(question_num=each_questions.get('question_num'),
                                          question=each_questions.get('question'),
                                          question_img_link=each_questions.get('question_img_link'),
                                          a1=each_questions.get('a1'),
                                          a2=each_questions.get('a2'),
                                          a3=each_questions.get('a3'),
                                          a4=each_questions.get('a4'),
                                          a5=each_questions.get('a5'),
                                          )

        instance.save()
        return instance

    class  Meta:
        model = RTest
        fields = ('id', 'num_of_questions', 'time_for_test','test_title','test_description','test_category','question_set')
     

class ETestSerialiazers(serializers.ModelSerializer):
    question_set = EQuestionSerialiazers(many=True)
    def create(self,validated_data):
        test_title = validated_data.get("test_title")
        test_description = validated_data.get("test_description")
        test_category = validated_data.get("test_category")
        num_of_questions = validated_data.get("num_of_questions")
        time_for_test = validated_data.get("time_for_test")
        new_obj = ETest.objects.create(num_of_questions=num_of_questions,time_for_test=time_for_test,test_title=test_title,
        test_description=test_description,test_category=test_category)

        all_questions = validated_data.get('question_set')
        if all_questions:
            for each_questions in all_questions:
                question = each_questions.get('question')
                question_num = each_questions.get('question_num')
                a1 = each_questions.get('a1')
                a2 = each_questions.get('a2')
                a3 = each_questions.get('a3')
                a4 = each_questions.get('a4')
                a5 = each_questions.get('a5')
                new_obj.question_set.create(question_num=question_num,question=question, a1=a1, a2=a2,  a3=a3, a4=a4, a5=a5)

        return new_obj

    def update(self,instance,validated_data):
        instance.test_title = validated_data.get("test_title",instance.test_title)
        instance.test_description = validated_data.get("test_description",instance.test_description)
        instance.test_category = validated_data.get("test_category",instance.test_category)
        instance.num_of_questions = validated_data.get("num_of_questions",instance.num_of_questions)
        instance.time_for_test = validated_data.get("time_for_test",instance.time_for_test)

        all_questions = validated_data.get("question_set")
        if all_questions:
            instance.question_set.all().delete()
            for each_questions in all_questions:
                instance.question_set.create(question_num=each_questions.get('question_num'),
                                          question=each_questions.get('question'),
                                          a1=each_questions.get('a1'),
                                          a2=each_questions.get('a2'),
                                          a3=each_questions.get('a3'),
                                          a4=each_questions.get('a4'),
                                          a5=each_questions.get('a5'),
                                          )

        instance.save()
        return instance

    class  Meta:
        model = ETest
        fields = ('id', 'num_of_questions', 'time_for_test','test_title','test_description','test_category','question_set')
     


class AptitudeTestSerialiazers(serializers.ModelSerializer):
    test_set= TestSerialiazers(many=True)
    class  Meta:
        model = AptitudeTest
        fields = ('id','category_title','category_description','test_set')


class EnglishTestSerialiazers(serializers.ModelSerializer):
    test_set= ETestSerialiazers(many=True)
    class  Meta:
        model = EnglishTest
        fields = ('id','category_title','category_description','test_set')


class ReasoningTestSerialiazers(serializers.ModelSerializer):
    test_set= RTestSerialiazers(many=True)
    class  Meta:
        model = ReasoningTest
        fields = ('id','category_title','category_description','test_set')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


# class UserSerializerWithToken(serializers.ModelSerializer):

#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)

#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
#         return token

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

#     class Meta:
#         model = User
#         fields = ('token', 'username', 'password')



class BlogsSerialiazers(serializers.ModelSerializer):
    def update(self,instance,validated_data):
        instance.blog_title = validated_data.get("blog_title",instance.blog_title)
        instance.blog_content = validated_data.get("blog_content",instance.blog_content)
        instance.blog_by = validated_data.get("blog_by",instance.blog_by)
        instance.blog_view_link = validated_data.get("blog_view_link",instance.blog_view_link)
        instance.blog_img_link = validated_data.get("blog_img_link",instance.blog_img_link)
        instance.blog_created = validated_data.get("blog_created",instance.blog_created)
        instance.blog_like_status = validated_data.get("blog_like_status",instance.blog_like_status)

        instance.save()
        return instance

    class  Meta:
        model = Blogs
        fields = ('id', 'blog_content', 'blog_by','blog_title','blog_view_link','blog_img_link','blog_created','blog_like_status')


class UserBlogSerializers(serializers.ModelSerializer):
    profile = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all())
    blog = serializers.SlugRelatedField(slug_field='id', queryset=Blogs.objects.all())

    class Meta:
        model = UserBlog
        fields = ('id', 'profile', 'blog')

# class UserSaveJobSerializers(serializers.ModelSerializer):
#     profile = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all())
#     job = serializers.SlugRelatedField(slug_field='id', queryset=Blogs.objects.all())

#     class Meta:
#         model = UserBlog
#         fields = ('id', 'profile', 'job')



class SaveUserBlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaveUserBlog
        fields = ('id', 'profile', 'blog')


class SaveUserJobSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaveUserJob
        fields = ('id', 'profile', 'job')

