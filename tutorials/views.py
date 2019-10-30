from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from .forms import TutorialForm, ApproveForm
from .models import Tutorial

from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

def tutorialList(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/list.html', { 'tutorials' : tutorials})

@login_required(login_url='/login/')
def uploadTutorial(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            f1 = form.save(commit=False)
            f1.upload_user = request.user
            f1.save()
            form.save_m2m()
            return redirect('tutorial_list')
    else:
        form = TutorialForm()
    return render(request, 'tutorial/upload.html', {'form' : form})

@login_required(login_url='/login/')
def deleteTutorial(request, pk):
    if request.method == 'POST':
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial.delete()
    return redirect('tutorial_list')

@login_required(login_url='/login/')
def approveTutorial(request, pk):
    if request.method == 'POST':
        question = Tutorial.objects.get(pk=pk)
        question.approved_user = str(request.user)
        form = ApproveForm(request.POST,instance=question)
        if form.is_valid():
                form.save()
        return  render(request, 'tutorial/approve.html', {'form': form})
        #return HttpResponse('H')
    else:
        return redirect('tutorial_list')


