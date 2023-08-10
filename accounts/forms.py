from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, validators=[validate_password])
    password_confirm = forms.CharField(label='Повторите пароль', strip=False,)
    email = forms.CharField(label='Email', required=True)
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    image = forms.ImageField(label='Фото', required=False)

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        image = cleaned_data.get('image')
        if password_confirm and password and password != password_confirm:
            raise ValidationError('Пароли не совпадают!')
        if not first_name and not last_name:
            raise ValidationError('Должно быть заполнено хотя бы одно из этих полей!')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'password', 'password_confirm', 'email', 'image']


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']