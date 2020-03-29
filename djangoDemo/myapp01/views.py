from django.shortcuts import render, redirect  # render 请求转发  redirect 响应重定向

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
        request.session['userAccount'] = userAcc
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


# 测试请求转发  一个可访问应用的转发
def testRender(request):
    print('session中存储的数据', request.session.get('userAccount'))
    context = dict()
    context['name'] = 'wn001'
    context['hobby'] = ['吃', '爬山']
    # 请求转发给客户端传递数据
    return render(request, 'testRender.html', context=context)

# 响应重定向 新发起请求  可以是如何可访问的url


def testRdirect(request):
    return redirect('http://www.baidu.com')
