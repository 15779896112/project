import hashlib
import io
import os

import random
import time

from PIL import Image, ImageDraw, ImageFont
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from app import settings
from app.settings import BASE_DIR
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User, Cart, Order, OrderGoods

global random_str


def home(request):
    wheels = Wheel.objects.all()
    nav = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shops = Shop.objects.all()
    mainshows = Mainshow.objects.all()
    home_list = {
        'wheels': wheels,
        'nav': nav,
        'mustbuys': mustbuys,
        'shophead': shops[0],
        'shoptabs': shops[1:3],
        'shopclass_list': shops[3:7],
        'shopcommends': shops[7:],
        'mainshows': mainshows,

    }
    return render(request, 'home/home.html', context=home_list)


def market(request, childcid='0', sortid='0'):
    foodtypes = Foodtypes.objects.all()
    index = int(request.COOKIES.get('index', 0))
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
        'foodtypes': foodtypes,
        'goods_all': goods_all,
        'name_list': name_list,
        'childcid': childcid,

    }
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        carts = user.cart_set.all()
        food_list['carts'] = carts



    return render(request, 'market/market.html', context=food_list)


def cart(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        carts = user.cart_set.filter(num__gt=0)
        data = {
            'carts':carts
        }
    else:
        return redirect('axf:login')
    return render(request, 'cart/cart.html',context=data)


def mine(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    str = {


    }
    if userid:
        user = User.objects.get(pk=userid)
        orders = user.order_set.all()
        str['user'] = user
        str['a'] = orders.filter(status=0).count()





    return render(request, 'mine/mine.html', context=str)


def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return temp


def register(request):
    if request.method == 'GET':
        return render(request, 'mine/registe.html')
    elif request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.password = generate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.tel = request.POST.get('emal')
        user.save()
        token = generate_token()
        cache.set(token, user.id, 60 * 60 * 24 * 3)

        request.session['token'] = token
        return redirect('axf:mine')


def login(request):
    if request.method == 'GET':

        return render(request, 'mine/login.html')
    elif request.method == 'POST':

        username = request.POST.get('username')
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            if generate_password(request.POST.get('password')) == user.password:
                token = generate_token()
                cache.set(token, user.id, 60 * 60 * 24 * 3)
                request.session['token'] = token


                back = request.COOKIES.get('back')
                path = 'axf:' + back
                return redirect(path)

            else:
                return render(request, 'mine/login.html', context={'err2': '密码错误'})
        else:
            return render(request, 'mine/login.html', context={'err1': '账号不存在'})


def logout(request):
    request.session.flush()

    return redirect('axf:mine')


def fileup(request):
    if request.method == 'GET':
        return render(request, 'mine/fileup.html')
    elif request.method == 'POST':
        token = request.session.get('token')
        userid = cache.get(token)
        user = User.objects.filter(pk=userid).first()

        file = request.FILES['file']
        file.name = str(time.time()) + str(file.name)
        filepath = os.path.join(settings.MDEIA_ROOT, file.name)
        with open(filepath, 'wb') as fp:
            for info in file.chunks():
                fp.write(info)
        user.img = file.name
        user.save()
        return redirect('axf:mine')
    else:
        return HttpResponse('文件上传失败')


# def verifycode(request):
#
#     width = 120
#     height = 40
#
#     bgcolor = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
#
#     image = Image.new('RGB', (width, height), bgcolor)
#     draw = ImageDraw.Draw(image)
#
#     temp = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     global random_str
#     random_str = ''
#     for i in range(0, 4):
#         random_str += temp[random.randrange(0, len(temp))]
#
#     font = ImageFont.truetype('/home/wzh/Desktop/wzh/project/AXF/app/static/mine/fonts/Fangsong.ttf', 30)
#
#
#     font_color_1 = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
#     font_color_2 = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
#     font_color_3 = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
#     font_color_4 = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
#
#
#     draw.text((10, 5), random_str[0], fill=font_color_1, font=font)
#     draw.text((40, 5), random_str[1], fill=font_color_1, font=font)
#     draw.text((70, 5), random_str[2], fill=font_color_1, font=font)
#     draw.text((100, 5), random_str[3], fill=font_color_1, font=font)
#
#     line_color_1 = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
#
#     for i in range(5):
#         x1 = random.randint(0, width)
#         x2 = random.randint(0, width)
#         y1 = random.randint(0, height)
#         y2 = random.randint(0, height)
#         draw.line((x1, y1, x2, y2), fill=line_color_1)
#
#     random_str = random_str.lower()
#     del draw
#
#
#     buff = io.BytesIO()
#     image.save(buff, 'png')
#
#     return HttpResponse(buff.getvalue(), 'image/png')


def checketel(request):
    username = request.GET.get('username')
    print(username)
    users = User.objects.filter(username=username)
    if users.exists():
        data = {
            "status": 0
        }
    else:
        data = {
            "status": 1
        }

    return JsonResponse(data)


def addcart(request):
    productid = request.GET.get('productid')
    token = request.session.get('token')
    userid = cache.get(token)
    users =  User.objects.filter(pk=userid)

    if users.exists():
        user = users.first()
        productid = request.GET.get('productid')
        goods = Goods.objects.filter(productid=productid).first()
        carts =Cart.objects.filter(user=user).filter(goods=goods)
        data = {
            'value': 1
        }

        if carts.exists():
            cart = carts.first()
            cart.num = cart.num +1
            cart.save()
            data['num'] = cart.num
        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.num = 1
            cart.save()
            data['num'] = cart.num

    else:
        data = {
            'value':0,
            'num':0
        }
    return JsonResponse(data)






def delcart(request):
    productid = request.GET.get('productid')
    token = request.session.get('token')
    userid = cache.get(token)
    users =  User.objects.filter(pk=userid)


    user = users.first()

    productid = request.GET.get('productid')

    goods = Goods.objects.filter(productid=productid).first()
    carts =Cart.objects.filter(user=user).filter(goods=goods)
    data = {
        'value': 1
    }
    cart = carts.first()
    cart.num = cart.num -1
    print(cart.num)
    cart.save()
    data['num'] = cart.num




    return JsonResponse(data)


def changecartselect(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    data = {
        'status':1,
        'value':cart.isselect,
    }
    return JsonResponse(data)


def allselect(request):
    isall = request.GET.get('isall')
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.all()
    if isall == 'true':
        isall = True
    else:
        isall = False
    for cart in carts:
        cart.isselect = isall
        cart.save()
    response_data = {
        'status': 1
    }
    return JsonResponse(response_data)


def total(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.filter(isselect=True)
    sum = 0
    for cart in carts:
        sum += cart.num*cart.goods.price
    response_data = {
        'sum': sum
    }

    return JsonResponse(response_data)

def create_identifier():
    identifier = str(int(time.time()))+str((random.randrange(1000,10000)))
    return identifier

def cerateorder(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.filter(isselect='True')
    if carts.exists():
        order = Order()
        order.user = user
        order.identifier = create_identifier()

        order.save()
        for cart in carts:
            ordergoods = OrderGoods()
            ordergoods.order = order
            ordergoods.goods = cart.goods
            ordergoods.num = cart.num
            ordergoods.save()
            cart.delete()
        return render(request, 'order/orderdetail.html', context={'order': order})
    return redirect('axf:cart')


def showallorder(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    orders = user.order_set.all()

    return render(request, 'order/showallorder.html', context={'orders': orders})


def goodsdetail(request,identifier):
    order = Order.objects.filter(identifier=identifier).first()

    return render(request, 'order/orderdetail.html', context={'order': order})

