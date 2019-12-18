from PIL import ImageFont, Image
from PIL.ImageDraw import ImageDraw
from django.utils.six import BytesIO

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from adminApp.models import Admin_user
from netcotss import settings


def login(request):
    return render(request, 'login.html')


import re


@csrf_exempt
def checklogin(request):
    imgCode = request.POST.get('imgCode')
    verify_code = request.session.get('verify_code')
    data = {
        'msg': 'ok',
        'status': 201,
    }
    b = re.match(imgCode, verify_code, re.I)
    print(b)
    if b:
        super_number = request.POST.get('super_number')
        admins = Admin_user.objects.filter(super_number=super_number)
        if admins.count() > 0:
            password = request.POST.get('password')
            admin = admins.first()
            if password == admin.password:
                data['status'] = 200
                return JsonResponse(data=data)
            else:
                data['msg'] = '密码不正确'
                return JsonResponse(data=data)
        else:
            data['msg'] = '超级用户不存在'
            return JsonResponse(data=data)
    data['msg'] = '验证码错误'
    return JsonResponse(data=data)


# //获取验证码的方法

def get_code(request):
    #
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    code = ""
    for i in range(4):
        code += random.choice(source)
    return code


def home(request):
    super_number = request.GET.get('super_number')

    return render(request, 'index.html', context=locals())
