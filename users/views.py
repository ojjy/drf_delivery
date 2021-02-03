from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.http import  JsonResponse, HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.views.generic import CreateView

# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token


from rest_framework import viewsets
from .serializers import UserSerializer

# from notice.models import Notice
# from tracking.models import Tracking
# Create your views here.


def index_view(request):
    return render(request, 'login.html')


def login_view(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            print(login(request, user))
        else:
            print("인증실패")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("index")
    else:
        return render(request, 'login.html', {'error' : '계정 활성화 오류'})

def signup_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            user.is_active = True
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return redirect("login")

        return render(request, 'index.html')

class SinupView(CreateView):
    model = User
    template_name = "signup_cbv.html"
    form_class = SignUpForm
    success_url = "login"

    def form_valid(self, form):
        self.object = form.save()
        print("form_valid function call")
        messages.success(self.request, "회원가입 성공, 이메일 인증 필요")
        return redirect(self.get_success_url())

###############################################################

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



def app_login(request):
    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        id = request.POST.get('userid', '')
        pw = request.POST.get('userpw', '')
        print("id = " + id + " pw = " + pw)
        result = authenticate(username=id, password=pw)
        if result:
            print("로그인 성공!")
            return JsonResponse({'code': '0000', 'msg': '로그인성공입니다.'}, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '로그인실패입니다.'}, status=200)
    else:
        return JsonResponse({'code': '1001', 'msg': '로그인화면'}, status=200)

