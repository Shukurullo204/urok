from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('about_us/', about_us_view, name="about_us_url"),
    path('services/', services_view, name="services_url"),
    path('our_team/', our_team_view, name="our_team_url"),
    path('contacts/', contacts_view, name="contacts_url"),

    path('category/<slug:category_slug>/', category_view, name="category_url"),
    path('post/<slug:post_slug>/', post_detail_view, name="post_detail_url"),
    path('search/', search_view, name="search_url")
]








