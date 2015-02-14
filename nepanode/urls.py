from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',
   #Third Party Apps
   #Zinnia
   url(r'^pages/', include('zinnia.urls', namespace='zinnia')),
   url(r'^pages/comments/', include('django_comments.urls')),
   url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
   (r'^tinymce/', include('tinymce.urls')),

   #Django-Helpdesk
   (r'forms/', include('helpdesk.urls')),

   #Geonode Project
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
   url(r'', include('social.apps.django_app.urls', namespace='social'))
) + urlpatterns

