from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from dentist_2_project.accounts.models import Profile
from dentist_2_project.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin

UserModel = get_user_model()


class CreateProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'dob': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Date Of Birth'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Phone Number'
                }
            )
        }


class EditProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'dob': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Date Of Birth'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Phone Number'
                }
            )
        }


class DeleteProfileForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    def __init__(self,user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('user',)


class UserRegistrationForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = UserModel
        fields = ('email',)

        # def clean_first_name(self):
        #    return self.cleaned_data['first_name']

        # if you want to have user with profile together
        # def save(self, commit=True):
        #     user = super().save(commit=commit)
        #     profile = Profile(**self.cleaned_data(), user=user,)
        #     if commit:
        #         profile.save()
        #     return user
