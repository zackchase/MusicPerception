from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from scaleID.views import home, post_data

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musicPerception.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('home', home),
    url('postdata', post_data),
)
