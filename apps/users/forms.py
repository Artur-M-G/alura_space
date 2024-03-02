from django import forms

class LoginForms(forms.Form):
    username_login = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

class SingUpForms(forms.Form):
    username_singup = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=256,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
    password_confirm = forms.CharField(
        label='Confirm password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat your password'
            }
        )
    )

    def clean_username_singup(self):
        username = self.cleaned_data.get("username_singup")
        if username:
            username = username.strip()
            if " " in username:
                raise forms.ValidationError("Spaces are not allowed in this field")
            else:
                return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords are not the same")
