from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url("^$", "puppet.views.home"),
    url("^drive", "puppet.views.drive"),
    url("", include("django_socketio.urls")),
)
