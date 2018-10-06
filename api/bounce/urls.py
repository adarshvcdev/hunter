# from django.urls import path
# from .views import ListScripView
# from bounce import views

# urlpatterns = [
#     # path('scrips/', ListScripView.as_view(), name="scrips-all"),
#     url(r'^scrips/$', views.scrip_list),
#     url(r'^scrips/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

from django.conf.urls import url
# from .views import ListScripView
from bounce import views

urlpatterns = [
    # path('scrips/', ListScripView.as_view(), name="scrips-all"),
    url(r'^api/scrips/$', views.scrip_list),
    url(r'^api/scrips/(?P<pk>[0-9]+)/$', views.scrip_detail)
]