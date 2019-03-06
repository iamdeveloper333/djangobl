from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    state =models.CharField(max_length=200,default=None,null=True)
    category = models.CharField(max_length=200,default=None,null=True)
    qualification = models.CharField(max_length=200,default=None,null=True)
    post_title = models.CharField(max_length=200)
    post_by = models.CharField(max_length=200)
    short_description = models.TextField()
    published_date = models.CharField(max_length=200,default=None,null=True)
    last_date = models.CharField(max_length=200,default=None,null=True)
    apply = models.CharField(max_length=200,blank=True,default=None,null=True)
    notification = models.CharField(max_length=200,blank=True,default=None,null=True)
    syllabus = models.CharField(max_length=200,blank=True,default=None,null=True)
    o_website = models.CharField(max_length=200,blank=True,default=None,null=True)
    extra_info = models.CharField(max_length=200,blank=True,default=None,null=True)
    # job_like_status = models.BooleanField(default=False)

    def __str__(self):
        return self.post_title

class Emails(models.Model):
    email = models.EmailField(max_length=70,default=None,blank=True)

    def __str__(self):
        return self.email

class ImportantDates(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class ApplicationFee(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class Eligibility(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class AgeLimit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class VacancyDetail(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default=None,null=True)
    content = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.text

class AdmitCards(models.Model):
    post_title = models.CharField(max_length=200)
    post_by = models.CharField(max_length=200)
    apply_link = models.CharField(max_length=200,default=None,null=True)
    img_link = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.post_title

class Result(models.Model):
    post_title = models.CharField(max_length=200)
    post_by = models.CharField(max_length=200)
    view_link = models.CharField(max_length=200,default=None,null=True)
    img_link = models.CharField(max_length=200,default=None,null=True)

    def __str__(self):
        return self.post_title

class Blogs(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    blog_by = models.CharField(max_length=200)
    blog_view_link = models.CharField(max_length=200,default=None,null=True)
    blog_img_link = models.CharField(max_length=200,default=None,null=True)
    blog_created = models.DateField(null=True, blank=True)
    blog_like_status = models.BooleanField(default=False)

    def __str__(self):
        return self.blog_title


class UserBlog(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class SaveUserBlog(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class SaveUserJob(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class AptitudeTest(models.Model):
    category_title =  models.CharField(max_length=400,default=None,null=True)
    category_description =  models.TextField(default=None,null=True)
    def __str__(self):
        return self.category_title

class Test(models.Model):
    test_title =  models.CharField(max_length=400,default=None,null=True)
    test_category =  models.CharField(max_length=400,default=None,null=True)
    test_description =  models.TextField(default=None,null=True)
    num_of_questions = models.IntegerField(blank=True, null=True, default=0)
    time_for_test = models.IntegerField(blank=True, null=True, default=0)
    all_test = models.ForeignKey(AptitudeTest, on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.test_title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=400,default=None,null=True)
    question_num = models.IntegerField(blank=True, null=True, default=0)
    question_img_link =  models.CharField(max_length=200,default=None,null=True)
    a1 = models.CharField(max_length=400,default=None,null=True)
    a2 = models.CharField(max_length=400,default=None,null=True)
    a3 = models.CharField(max_length=400,default=None,null=True)
    a4 = models.CharField(max_length=400,default=None,null=True)
    a5 = models.CharField(max_length=400,default=None,null=True)

    def __str__(self):
        return self.question


class ReasoningTest(models.Model):
    category_title =  models.CharField(max_length=400,default=None,null=True)
    category_description =  models.TextField(default=None,null=True)
    def __str__(self):
        return self.category_title

class RTest(models.Model):
    test_title =  models.CharField(max_length=400,default=None,null=True)
    test_category =  models.CharField(max_length=400,default=None,null=True)
    test_description =  models.TextField(default=None,null=True)
    num_of_questions = models.IntegerField(blank=True, null=True, default=0)
    time_for_test = models.IntegerField(blank=True, null=True, default=0)
    all_test = models.ForeignKey(ReasoningTest, on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.test_title

class RQuestion(models.Model):
    test = models.ForeignKey(RTest, on_delete=models.CASCADE)
    question = models.CharField(max_length=400,default=None,null=True)
    question_num = models.IntegerField(blank=True, null=True, default=0)
    question_img_link =  models.CharField(max_length=200,default=None,null=True)
    a1 = models.CharField(max_length=400,default=None,null=True)
    a2 = models.CharField(max_length=400,default=None,null=True)
    a3 = models.CharField(max_length=400,default=None,null=True)
    a4 = models.CharField(max_length=400,default=None,null=True)
    a5 = models.CharField(max_length=400,default=None,null=True)

    def __str__(self):
        return self.question

class EnglishTest(models.Model):
    category_title =  models.CharField(max_length=400,default=None,null=True)
    category_description =  models.TextField(default=None,null=True)
    def __str__(self):
        return self.category_title

class ETest(models.Model):
    test_title =  models.CharField(max_length=400,default=None,null=True)
    test_category =  models.CharField(max_length=400,default=None,null=True)
    test_description =  models.TextField(default=None,null=True)
    num_of_questions = models.IntegerField(blank=True, null=True, default=0)
    time_for_test = models.IntegerField(blank=True, null=True, default=0)
    all_test = models.ForeignKey(EnglishTest, on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.test_title

class EQuestion(models.Model):
    test = models.ForeignKey(ETest, on_delete=models.CASCADE)
    question = models.CharField(max_length=400,default=None,null=True)
    question_num = models.IntegerField(blank=True, null=True, default=0)
    a1 = models.CharField(max_length=400,default=None,null=True)
    a2 = models.CharField(max_length=400,default=None,null=True)
    a3 = models.CharField(max_length=400,default=None,null=True)
    a4 = models.CharField(max_length=400,default=None,null=True)
    a5 = models.CharField(max_length=400,default=None,null=True)

    def __str__(self):
        return self.question




