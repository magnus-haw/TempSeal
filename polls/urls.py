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
    url(r'^post/$',views.post_new,name='post_new'),
    url(r'^post_food/$',views.post_new_food,name='post_new_food'),
#    url(r'^post/thanks/$',views.thanks,name='thanks'),
    url(r'^$', views.IndexView.as_view(template_name='polls/map.html'), name='index'),
    url(r'^(?P<building_name>\w+)/$', views.plot_building, name='results'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Building, properties=('name','temp')), name='data'),
]
