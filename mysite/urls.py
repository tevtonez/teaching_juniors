from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from polls import views as polls_views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^polls/', include('polls.urls')),

    url(r'^$', polls_views.IndexView.as_view(), name='home'),
    url(r'^polls_template/$', polls_views.pollsIndexView.as_view(), name='polls_template'),

    # logging users in/out
    url(r'^login/$', auth_views.login, {'template_name': 'polls/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    #signup users
    url(r'signup/$', polls_views.SignUpView.as_view(),name = 'signup'),

]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
