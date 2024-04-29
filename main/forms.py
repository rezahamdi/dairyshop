from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import forms as auth_forms


class LoginForm(auth_forms.AuthenticationForm):
    """
     This form use for login in our website 
    """
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus':'True',
                'class':'form-input'
                 }))
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-input'
                  }))

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password'].label = 'رمز عبور'

  


class CustomerRegistrationForm(auth_forms.UserCreationForm):
    """
     This form use for create an user in our db
    """
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تایید رمز عبور'
        self.fields['password1'].widget.attrs.update(
            {
              'class':'form-input'  
            })
        self.fields['password2'].widget.attrs.update(
            {
              'class':'form-input'  
            })
    
    # Set error when two pass are't same
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('پسوردها باهم تطابق ندارد')
        return password2


    class Meta:
        model= User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
            )
        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'autofocus':'True',
                    'class':'form-input'
                     }),
            'email' : forms.EmailInput(
                attrs={
                    'class':'form-input'
                      }),
            }
        labels ={
            'username':'نام کاربری',
            'email':'ایمیل',
            }


    
