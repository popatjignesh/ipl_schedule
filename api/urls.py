from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api import views
from rest_framework.authtoken import views as tokenView


urlpatterns = patterns('',
	url(r'^register/', views.register.as_view(), name='register'),
	url(r'^login/', tokenView.obtain_auth_token),

	url(r'^team/add/', views.team.as_view(), name='team-add'),
	url(r'^team/all/', views.team.as_view(), name='team-all'),

	url(r'^team/detail/(?P<pk>[0-9]+)/', views.team_detail.as_view(), name='team-detail'),
	url(r'^team/delete/(?P<pk>[0-9]+)/', views.team_detail.as_view(), name='team-detail'),
	url(r'^team/update/(?P<pk>[0-9]+)/', views.team_detail.as_view(), name='team-detail'),

	url(r'^venue/add/', views.venue.as_view(), name='venue-add'),
	url(r'^venue/all/', views.venue.as_view(), name='venue-all'),	

	url(r'^venue/detail/(?P<pk>[0-9]+)/', views.venue_detail.as_view(), name='venue-detail'),
	url(r'^venue/delete/(?P<pk>[0-9]+)/', views.venue_detail.as_view(), name='venue-detail'),
	url(r'^venue/update/(?P<pk>[0-9]+)/', views.venue_detail.as_view(), name='venue-detail'),

	url(r'^match/filter/', views.match.as_view(), name='match-filter'),

	url(r'^match/add/', views.match.as_view(), name='match-add'),
	url(r'^match/all/', views.match.as_view(), name='match-all'),

	url(r'^match/today/', views.match_today.as_view(), name='match-today'),
	url(r'^match/nextweek/', views.match_nextweek.as_view(), name='match-nextweek'),

	url(r'^match/detail/(?P<pk>[0-9]+)/', views.match_detail.as_view(), name='match-detail'),
	url(r'^match/delete/(?P<pk>[0-9]+)/', views.match_detail.as_view(), name='match-detail'),
	url(r'^match/update/(?P<pk>[0-9]+)/', views.match_detail.as_view(), name='match-detail'),

	url(r'^favourite/add/', views.favourite.as_view(), name='favourite'),
	url(r'^favourite/all/', views.favourite.as_view(), name='favourite'),

	url(r'^favourite/detail/(?P<pk>[0-9]+)/', views.favourite_detail.as_view(), name='favourite-detail'),
	url(r'^favourite/delete/(?P<pk>[0-9]+)/', views.favourite_detail.as_view(), name='favourite-detail'),
	url(r'^favourite/update/(?P<pk>[0-9]+)/', views.favourite_detail.as_view(), name='favourite-detail'),
)


