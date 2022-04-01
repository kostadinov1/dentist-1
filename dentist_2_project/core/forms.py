from django import forms

from dentist_2_project.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from dentist_2_project.core.models import Appointment, Review


class AppointmentForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Appointment
        exclude = ('user',)
        widgets={
            'message': forms.TextInput(attrs={'rows': 4})
        }


class DeleteAppointmentForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()


    def save(self):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Appointment
        exclude = ('user',)


class ReviewForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Review
        exclude = ('user',)


class EditReviewForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Review
        exclude = ('user',)


class DeleteReviewForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Review
        exclude = ('user',)
