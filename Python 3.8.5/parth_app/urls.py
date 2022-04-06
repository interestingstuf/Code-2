from django.urls import path
from django.urls.resolvers import URLPattern
from parth_app import views
urlpatterns = [
path("", views.home2, name="abc"),
path("page2/", views.home1, name="cde"),
path("videos/", views.page1, name="Atharava")



] 


