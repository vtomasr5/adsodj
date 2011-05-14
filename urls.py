from django.conf.urls.defaults import *

import web.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^adsodj/', include('adsodj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Web project
    (r'^base', web.views.base),
    (r'^.*', web.views.index), # ha d'estar sa darrera!
)
