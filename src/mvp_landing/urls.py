from django.conf.urls import patterns, include, url

from django.conf import settings #! import settings
from django.conf.urls.static import static #! import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mvp_landing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'signups.views.home', name='home'),
)

if settings.DEBUG: #! If you are in DEBUG mode, then append the below to the urlpatterns variable
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)