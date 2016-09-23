from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic.dates import DateDetailView, YearArchiveView, DayArchiveView, MonthArchiveView

from .models import Article, Tag
from .forms import ArticleForm

# Create your views here.
class HomePageView(TemplateView):
    template_name= "article/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

class AllArticlesView(ListView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name = "article/ArticleList.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(AllArticlesView, self).get_context_data(**kwargs)
        context['title'] = "All our articles"
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

    def get_context_data(self, **kwargs):
        context = super(ArticleYearList, self).get_context_data(**kwargs)
        context['title'] = "Articles for " + self.kwargs['year']
        return context


class ArticleMonthList(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name= "article/ArticleList.html"
    paginate_by=20

    def get_context_data(self, **kwargs):
        context = super(ArticleMonthList, self).get_context_data(**kwargs)
        context['title'] = "Articles for {}, {}".format(self.kwargs['month'],
                                                        self.kwargs['year'])
        return context


class ArticleDayList(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    template_name= "article/ArticleList.html"
    paginate_by=20

    def get_context_data(self, **kwargs):
        context = super(ArticleDayList, self).get_context_data(**kwargs)
        context['title'] = "Articles for {} {}, {}".format(self.kwargs['day'],
                                                           self.kwargs['month'],
                                                           self.kwargs['year'])
        return context


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


class TagArticleListView(ListView):
    model = Article
    make_object_list = True
    template_name = "article/ArticleList.html"

    def get_queryset(self):
        queryset = Article.objects.filter(tags__in=self.kwargs['pk'])
        return queryset

class TagListView(ListView):
    model = Tag
    make_object_list = True
    queryset = Tag.objects.all()
    template_name = "article/TagList.html"