from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'SisCaf.views.home', name='home'),
    # url(r'^SisCaf/', include('SisCaf.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'login.views.index'),
    url(r'^login/entrar/$', 'login.views.entrar'),
    url(r'^login/cadastro/$', 'login.views.cadastro'),
    url(r'^login/cadastrar/$', 'login.views.cadastrar'),
    url(r'^login/pesquisar/$', 'login.views.pesquisar'),
    url(r'^login/pesquisa/$', 'login.views.pesquisa'),
)
