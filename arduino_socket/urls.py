from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url("^$", "light.views.home"),
    url("^light", include('light.urls')),
    url("^axis", include('axis.urls')),
    url("", include("django_socketio.urls")),
)
