from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Projects,Review,RATE_CHOICES,Profile

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

class CreateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','github','instagram','linkedin']
        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            # 'profile_photo':forms.TextInput(attrs={'class':'form-control'}),
            'github':forms.TextInput(attrs={'class':'form-control'}),
            'instagram':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control'}),
            
        }
      
             
        
class RatingsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False)
    rate_usability = forms.ChoiceField(choices=RATE_CHOICES,required=True,widget=forms.Select())
    rate_content = forms.ChoiceField(choices=RATE_CHOICES,required=True,widget=forms.Select())
    rate_design= forms.ChoiceField(choices=RATE_CHOICES,required=True,widget=forms.Select())
    
    class Meta:
        model = Review
        fields = ['body','rate_design', 'rate_usability', 'rate_content']    
        
        
        