from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic.dates import DateDetailView, YearArchiveView, DayArchiveView, MonthArchiveView

from .models import Article
from .forms import ArticleForm

# Create your views here.
class HomePageView(TemplateView):
    template_name= "article/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

class ArticleDetail(DateDetailView):
    model=Article
    date_field="pub_date"
    template_name= "article/ArticleDetail.html"


class ArticleYearList(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name= "article/ArticleList.html"
    paginate_by=20


class ArticleMonthList(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name= "article/ArticleList.html"
    paginate_by=20


class ArticleDayList(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name= "article/ArticleList.html"
    paginate_by=20


class NewArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/EditArticle.html"

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        return super(NewArticleView, self).form_valid(form)


class UpdateArticleView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/EditArticle.html"