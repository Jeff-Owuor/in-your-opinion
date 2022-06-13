from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Projects,Review,RATE_CHOICES

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        
class UploadProjectForm(forms.ModelForm):
    
    class Meta:
            model = Projects
            fields = '__all__'
            exclude = ['user','score']
            
            
            
class RateForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False)
    rate_design = forms.ChoiceField(choices=RATE_CHOICES,required=True,widget=forms.Select())
    
    class Meta:
        model = Review
        fields = ('body','rate_design')