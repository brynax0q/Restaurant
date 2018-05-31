"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from demo.views import IndexView, ReservationView, CancelReservationView, ChangeTableView, WalkInView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^reservation/$', ReservationView.as_view(), name="reservation"),
    url(r'^cancel_reservation/$', CancelReservationView.as_view(), name="cancel_reservation"),
    url(r'^change_table/$', ChangeTableView.as_view(), name="change_table"),
    url(r'^walk_in/$', WalkInView.as_view(), name="walk_in"),
]
