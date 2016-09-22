from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='landing_page'),

    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/(?P<slug>[-\w]+)/$',
        views.ArticleDetail.as_view(),
        name='article-detail'),

    url(r'^(?P<year>[0-9]{4})/$',
        views.ArticleYearList.as_view(),
        name='article_year_list'),

    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',
        views.ArticleMonthList.as_view(),
        name='article_month_list'),

    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$',
        views.ArticleDayList.as_view(),
        name='article_day_list'),
    ]