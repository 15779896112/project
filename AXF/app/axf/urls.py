from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^home/', views.home,name='home'),
    url(r'^market/(\w+)/(\w+)',views.market,name='markets'),
    url(r'^market/',views.market,name='market'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^register/',views.register,name='register'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^login/',views.login,name='login'),
    url(r'^fileup/',views.fileup,name='fileup'),
    url(r'^verifycode/',views.verifycode,name='verifycode'),
    url(r'^checketel/', views.checketel, name='checketel'),
    url(r'^addcart/',views.addcart,name='addcart'),

]