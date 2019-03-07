from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods


def home(request):
    wheels = Wheel.objects.all()
    nav = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shops = Shop.objects.all()
    mainshows = Mainshow.objects.all()
    home_list = {
        'wheels':wheels,
        'nav':nav,
        'mustbuys':mustbuys,
        'shophead':shops[0],
        'shoptabs':shops[1:3],
        'shopclass_list':shops[3:7],
        'shopcommends':shops[7:],
        'mainshows':mainshows,

    }
    return render(request,'home/home.html',context=home_list)


def market(request,type=1):
    foodtypes = Foodtypes.objects.all()
    goods_all = Goods.objects.all()[0:10]
    # typenames = foodtypes.filter(typesort=type)[0]
    # name_list = typenames.childtypenames.split('#')



    food_list = {
        'foodtypes':foodtypes,
        # 'name_list':name_list,
        'goods_all':goods_all,
    }
    return render(request, 'market/market.html',context=food_list)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')