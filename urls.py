from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_base_project/', include('django_base_project.foo.urls')),

    (r'^admin/', include(admin.site.urls)),
)
