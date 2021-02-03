from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms as django_forms

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):
    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'address', 'detailAddress', 'extraAddress', 'postcode']
        widgets = {
            'email': django_forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '이메일 주소', 'aria-label': 'email',
                       'aria-describedby': 'basic-addon1'}),
            'username': django_forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '사용자 아이디', 'id': 'username',
                       'aria-label': 'sender_address', 'aria-describedby': 'basic-addon1'}),
            'password': django_forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': '비밀번호', 'id': 'password',
                       'aria-label': 'password', 'aria-describedby': 'basic-addon1'}),
            'address': django_forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '주소', 'id': 'address',
                       'aria-label': 'address', 'aria-describedby': 'basic-addon1'}),
            'detailAddress': django_forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '상세주소', 'id': 'detailAddress',
                       'aria-label': 'detailAddress', 'aria-describedby': 'basic-addon1'}),
            'extraAddress': django_forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '참고항목', 'id': 'extraAddress',
                       'aria-label': 'extraAddress', 'aria-describedby': 'basic-addon1'}),
            'postcode': django_forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '우편번호', 'id': 'postcode',
                       'aria-label': 'postcode', 'aria-describedby': 'basic-addon1'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user