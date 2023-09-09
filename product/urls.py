from django.urls import path 
from .views import *
from . import views
app_name='product'

urlpatterns = [
    path('',views.home,name='home'),
    
    # api
    path('product/list',ProuctsAPiList.as_view(),name='ProuctsAPiList'),
    # http://127.0.0.1:8923/product/list/filter?gender=Men
    # http://127.0.0.1:8923/product/list/filter?gender=Women
    path('product/list/filter',ProuctsAPiList_by_filter.as_view(),name='ProuctsAPiList_by_filter'),
    path('product/list/<int:pk>',ProuctsAPiDetail.as_view(),name='ProuctsAPiDetail'),
]
