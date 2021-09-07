"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from facebook.views import play, play2, profile, event, fail, help, warn, newsfeed, detail_feed, pages, new_feed, remove_feed, edit_feed, page_new, remove_page, edit_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play, name='play'),
    path('play2/', play2, name='play2'),
    path('dogeunchoi/profile/', profile, name='profile'),
    path('event/', event, name='event'),

    path('fail/', fail),
    path('help/', help),
    path('warn/', warn),

    path('', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('pages/', pages),
    path('new/', new_feed, name='new_feed'),

    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),

    path('pages/new/', page_new),
    path('pages/<pk>/remove/', remove_page),
    path('pages/<pk>/edit/', edit_page),
    
]
