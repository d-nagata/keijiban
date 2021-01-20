from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class SignUpForm(UserCreationForm):
   class Meta:
       model = UserModel
       fields = ('username', 'email', 'password1', 'password2')

   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
           field.widget.attrs['class'] = 'input'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['username'].widget.attrs['class'] = 'input'
       self.fields['password'].widget.attrs['class'] = 'input'

class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = UserModel
        fields = ('last_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
