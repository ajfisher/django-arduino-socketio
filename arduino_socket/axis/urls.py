from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('axis.views',
    url(r"^/test$", 'devicetest'),
    url(r"^/show$", 'showaxis'),
    url(r"^/usephone$", 'usephone'),
    
)
