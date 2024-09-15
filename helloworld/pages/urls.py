from django.urls import path
from .views import homepageview #. means to look with in the same directory.

urlpatterns=[
    path('',homepageview,name="home")
]
# In other words, if the user requests the homepage represented by the empty string "", Django  should use the view called homePageView.
