from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

red_asterisk = mark_safe(' <font color="red">*</font>')


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text='20 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email_address = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email_address',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
