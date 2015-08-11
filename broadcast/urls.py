from django.conf.urls import url

from broadcast import views

urlpatterns = [
    # ex: /broadcast/login
    url(r'^$', views.login, name='index'),
    # ex: /broadcast/login
    url(r'^login/$', views.login, name='login'),
    # ex: /broadcast/00110001/
    url(r'^success/$', views.check, name='check'),
    # ex: /broadcast/new_apply
    url(r'^new_apply/$', views.new_apply_html, name='new_apply_html'),

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
