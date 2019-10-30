from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexClass(View):
    def get(self,request):
        return render(request,'login/welcome.html')

class LoginClass(View):
    def get(self,request):
        return render( request, 'login/login.html' )

    def post(self, request):
        user_name = request.POST.get( 'tendangnhap' )
        mat_khau = request.POST.get( 'pass_word' )
        user = authenticate( username=user_name, password=mat_khau )
        if user is None:
            return render( request, 'login/thatbai.html' )
        else:
            login( request, user )
            #return render( request, 'login/thanhcong.html',{'user_name':user })
            return render(request, 'login/thanhcong.html',{'user_name':user})

def donvi(request):
        return  render(request,'login/donvi.html')

def thunghiem(request):
    my_name='Tran Huu Dung'
    taisan=('Vang','Bac','Con')
    return  render(request,'login/test.html',{'my_name':my_name,'taisan':taisan})

class PhuonganClass(View):
    def get(self,request):
        return  render(request,'giaodien/phuongan.html')
class Phuongan_didong(View):
    def get(self,request):
        return  render(request,'giaodien/phuongan_didong.html')
class Phuongan_tktu(View):
    def get(self,request):
        return  render(request,'giaodien/phuongan_tktu.html')
class Phuongan_dhml(View):
    def get(self,request):
        return  render(request,'giaodien/phuongan_dhml.html')

class ViewUser(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self,request):
            return HttpResponse('Bạn đã đăng nhập thành công')




@decorators.login_required(login_url='/login/')
def view_data(request):
    return HttpResponse('Xem data')
