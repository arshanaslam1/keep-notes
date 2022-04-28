from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms.widgets import NumberInput
from .models import User
from .utils.validators import age_validator
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class AccountUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        validators=[age_validator])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth']


class AccountRegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(validators=[age_validator],
                                    widget=NumberInput(
        attrs={'type': 'date',
               }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password1', 'password2']


class AccountPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(AccountPasswordResetForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-Mail address."
            self.add_error('email', msg)
        return email

