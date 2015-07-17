from django.conf.urls import patterns, include, url
from blog import settings
from blogBase.views import RegistrationView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blogBase.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/register/$', 'registration.backends.simple.views.RegistrationView', name='register'),
    url(r'^accounts/register/$', RegistrationView.as_view(success_url=settings.LOGIN_REDIRECT_URL), name='register'),
    url(r'^users/(?P<username>[\w]+)\W*/$', 'blogBase.views.user_view', name='user_view'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^calendar/', include('calendarium.urls')),
    # url(r'^users/$', UserViewProfile.as_view(), name='user'),
)
