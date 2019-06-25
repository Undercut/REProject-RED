
from django.conf.urls import url

from commodity import views

urlpatterns = [

    url(r'commodity/$', views.CommodityView.as_view(), name='commodity'),
    url(r'^commodity/list$', views.CommodityListView.as_view(), name="commodity-list"),
    url(r'^commodity/create$', views.CommodityCreateView.as_view(), name="create"),
    url(r'^commodity/update$', views.CommodityUpdateView.as_view(), name="update"),
    url(r'^commodity/delete$', views.CommodityDeleteView.as_view(), name='delete'),
    url(r'^commodity/enable$', views.CommodityEnableView.as_view(), name='enable'),
    url(r'^commodity/disable$', views.CommodityDisableView.as_view(), name='disable'),
    url(r'^commodity/detail$', views.CommodityDetailView.as_view(), name="detail"),
    url(r'^commodity/uploadimage$', views.UploadImageView.as_view(), name="commodity-uploadimage"),
]
