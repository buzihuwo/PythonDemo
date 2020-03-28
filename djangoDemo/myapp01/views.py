from django.shortcuts import render  # 请求转发

# Create your views here.
'''
定义视图函数
'''


def test(request):
    print('12345')
    return render(request, 'test.html')


'''
页面访问
pageName 页面名称 模板名
'''


def topage(request, pageName):
    return render(request, '%s.html' % pageName)


'''
 登录操作
'''


def login(request):
    # 获取提交参数  get
    userAcc = request.GET.get('userAcc', None)
    userPass = request.GET.get('userPass', None)
    if userAcc == 'admin' and userPass == '123456':
        print('账号密码存在')
        return render(request, 'test.html')
    return render(request, 'login.html')

# 注册


def register(request):
    userAcc = request.POST.get('userAcc', None)
    userPass = request.POST.get('userPass', None)
    address = request.POST.getlist('address', None)
    print(userAcc, userPass)
    print(address)
    return render(request, 'login.html')
