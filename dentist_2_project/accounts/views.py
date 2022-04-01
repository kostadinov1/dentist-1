from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import CreateView, UpdateView, DeleteView

from dentist_2_project.accounts.forms import UserRegistrationForm, CreateProfileForm, EditProfileForm, DeleteProfileForm
from dentist_2_project.accounts.models import Profile
from dentist_2_project.core.models import Review, Appointment

UserModel = get_user_model()


def build_profile_view(request):
    profile = Profile.objects.get(pk=request.user.id)
    user = request.user
    reviews = Review.objects.filter(user_id=request.user)
    appointments = Appointment.objects.filter(user_id=request.user)

    context = {
        'profile': profile,
        'user': user,
        'reviews': reviews,
        'appointments': appointments
    }

    return render(request, 'auth/profile-view.html', context)


class CreateUserProfileView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('show index')
    form_class = CreateProfileForm
    template_name = 'auth/profile-create.html'
    success_url = reverse_lazy('show index')
    success_message = 'New new user profile has been created'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'auth/profile-edit.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('show profile view')


class DeleteProfileView(DeleteView):
    model = Profile
    form_class = DeleteProfileForm
    template_name = 'auth/profile-delete.html'


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('show index')

    # to log us in straight after registration
    def form_valid(self, form):   # *args, **kwargs to be more extensible
        result = super().form_valid(form)
        # user -> self.object
        # req -> self.request
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    # this method needs to be overrided
    def get_success_url(self):
        return reverse_lazy('show index')


def build_logout(request):
    logout(request)
    messages.info(request, 'LOG OUT SUCCESSFUL')
    return redirect('show index')


class ChangePasswordView(PasswordChangeView):
    pass
