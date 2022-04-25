from django.urls import path

from parth_app import views
urlpatterns = [
path("", views.home2, name="home"),
path("page2/", views.home1, name="cde"),
path("videos/", views.page1, name="Atharava"),
path("msfs/", views.msfspage, name="MS"),
path("xplane/", views.xplanepage, name="XP"),
path("flightgear/", views.flightgearpage, name="FG"),
path("acro/", views.acropage, name="AC"),
path("downloads/", views.downloadpdfs, name="DWN"),
path("pdf1/", views.getpdf, name="PDF1"),
path("upload/", views.uploading1, name="UP1"),
path("contact/", views.uploading1, name="CON"),
path("contactFORM/", views.formshow, name="CONFOR"),
path("displaydata/", views.view1, name="DISDAT"),




]


