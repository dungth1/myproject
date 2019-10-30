from django import forms


from .models import Tutorial

class TutorialForm(forms.ModelForm):

    class Meta:
        model = Tutorial

     #   fields = ['title', 'category', 'feature_image', 'attachment']

        fields = ['dept', 'category','phuongan', 'attachment','approve_status']

class ApproveForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['approve_status']