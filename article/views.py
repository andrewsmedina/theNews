from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.dates import DateDetailView, YearArchiveView, DayArchiveView, MonthArchiveView

from .models import Article


# Create your views here.
class HomePageView(TemplateView):
    template_name="home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

class ArticleDetail(DateDetailView):
    model=Article
    date_field="pub_date"
    template_name="ArticleDetail.html"


class ArticleYearList(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name="ArticleList.html"
    paginate_by=20


class ArticleMonthList(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name="ArticleList.html"
    paginate_by=20


class ArticleDayList(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name="ArticleList.html"
    paginate_by=20