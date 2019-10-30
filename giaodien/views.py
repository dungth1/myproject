from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'giaodien/index.html')
def giaodien(request):
    return render(request,'giaodien/giaodien.html')
def phuongan(request):
    return render(request,'giaodien/phuongan.html')

