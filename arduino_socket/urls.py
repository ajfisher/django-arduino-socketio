from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url("^$", "light.views.home"),
    url("^drive", include('light.urls')),
    url("^axis", include('axis.urls')),
    url("^asteroids", include('asteroids.urls')),
    url("", include("django_socketio.urls")),
)
