from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.decorators.cache import cache_page

from geonode.urls import *

urlpatterns = patterns('',
   #Third Party Apps
   #Zinnia
   url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
   url(r'^blog/comments/', include('django_comments.urls')),
   url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
   (r'^tinymce/', include('tinymce.urls')),

   #Django-Helpdesk
   (r'^helpdesk/', include('helpdesk.urls')),
   
   #Django-leaflet-storage
   # Commented URLs are placeholders for uMAP map gallery and user maps display
   #url(r'^$', views.home, name="home"),
   #url(r'^showcase/$', cache_page(24 * 60 * 60)(views.showcase), name='maps_showcase'),
   #url(r'^search/$', views.search, name="search"),
   #url(r'^about/$', views.about, name="about"),
   #url(r'^user/(?P<username>[-_\w]+)/$', views.user_maps, name='user_maps'),   
   (r'^geojson/', include('leaflet_storage.urls')),

   #Geonode Project
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
   # python-social-auth
   url(r'', include('social.apps.django_app.urls', namespace='social')),
   #url(r'^account/signup/', TemplateView.as_view(template_name='signup.html'), name='socialauth'),
) + urlpatterns

