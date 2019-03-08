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


def market(request,childcid='0',sortid='0'):
    foodtypes = Foodtypes.objects.all()
    index = int(request.COOKIES.get('index',0))
    typeid = foodtypes[index].typeid
    # goods_all = Goods.objects.filter(categoryid = typeid)
    namestr_list = foodtypes[index].childtypenames.split('#')
    print(sortid)
    if childcid == '0':
        goods_all = Goods.objects.filter(categoryid=typeid)
    else:
        goods_all = Goods.objects.filter(childcid=childcid)
    name_list = []
    if sortid == '1':
        goods_all = goods_all.order_by('-productnum')
    if sortid == '2':
        goods_all = goods_all.order_by('price')
    if sortid == '3':
        goods_all = goods_all.order_by('-price')

    for name in namestr_list:
        name_dicy = {}
        lis = name.split(':')
        name_dicy['sname'] = lis[0]
        name_dicy['id'] = lis[1]
        name_list.append(name_dicy)







    food_list = {
        'foodtypes':foodtypes,
        'goods_all':goods_all,
        'name_list':name_list,
        'childcid':childcid,

    }
    return render(request, 'market/market.html',context=food_list)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):

    return render(request, 'mine/mine.html')