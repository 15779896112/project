from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^home/', views.home,name='home'),
    url(r'^market/(\w+)/(\w+)',views.market,name='markets'),
    url(r'^market/',views.market,name='market'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^mine/',views.mine,name='mine'),



]