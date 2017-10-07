from django.conf.urls import include,url
from django.contrib import admin
from djgeojson.views import GeoJSONLayerView
from django.views.generic import TemplateView
admin.autodiscover()

from .models import Building
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^post/$',views.post_new,name='post_new'),
    url(r'^post/thanks/$',views.thanks,name='thanks'),
    url(r'^$', TemplateView.as_view(template_name='polls/map.html'), name='index'),
    url(r'^(?P<building_name>\w+)/results/$', views.plot_building, name='results'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Building, properties=('name')), name='data'),
]
