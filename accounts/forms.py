from allauth.account.forms import SignupForm
from django import forms
from django.forms.widgets import NumberInput
from .models import User
from .utils.validators import age_validator
from django.contrib.auth.forms import PasswordResetForm


class AccountUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(validators=[age_validator],
                                    widget=NumberInput(
                                        attrs={'type': 'date',
                                               }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'date_of_birth', 'avatar']


class AccountRegisterForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
            }
        )
    )
    date_of_birth = forms.DateField(
        validators=[age_validator],
        widget=NumberInput(
            attrs={'type': 'date',
                   }))

    field_order = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password1', 'password2']

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(AccountRegisterForm, self).save(request)

        # Add your own processing here.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.save()

        # You must return the original result.
        return user


class AccountPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(AccountPasswordResetForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-Mail address."
            self.add_error('email', msg)
        return email
