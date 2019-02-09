import django_filters
from django_filters import rest_framework as filters
from api.models import (
    Post,AdmitCards,Result,Blogs
)


class PostFilter(filters.FilterSet):
    post_title = django_filters.CharFilter(lookup_expr='icontains')
    state = django_filters.CharFilter(lookup_expr='icontains')
    qualification = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = []

class AdmitCardsFilter(filters.FilterSet):
    post_title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = AdmitCards
        fields = []

class ResultFilter(filters.FilterSet):
    post_title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Result
        fields = []

class BlogsFilter(filters.FilterSet):
    blog_title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blogs
        fields = []
