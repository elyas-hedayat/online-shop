from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import ValidationError

from .models import User


class CreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("phone_number",)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] and cleaned_data["password_confirm"]:
            if cleaned_data["password"] != cleaned_data["password_confirm"]:
                raise ValidationError("passwords arent matches")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text='you can change password using <a href="../password/">this form</a>.'
    )

    class Meta:
        model = User
        fields = (
            "phone_number",
            "status",
        )
