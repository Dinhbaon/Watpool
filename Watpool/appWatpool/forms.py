from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


from appWatpool import Account

class Register(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add @uwaterloo.ca Email")

    class Meta: 
        model = Account
        fields = ('email, password1, password2')
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try: 
            Account = Account.objects.get(email=email)
        except Exception: 
            return email
        raise forms.ValidationError(f"Email {email} is already in use")
    