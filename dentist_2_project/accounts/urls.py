from django.urls import path, include

from dentist_2_project.accounts.views import build_profile_view, UserLoginView, UserRegistrationView, \
    ChangePasswordView, build_logout, CreateUserProfileView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('sign-in/', UserLoginView.as_view(), name='show sign in'),
    path('sign-up/', UserRegistrationView.as_view(), name='show sign up'),
    path('logout/', build_logout, name='show logout'),
    path('change-password/', ChangePasswordView.as_view(), name='show change password'),
    path('profile-view/', build_profile_view, name='show profile view'),
    path('profile-create/', CreateUserProfileView.as_view(), name='show profile create'),
    path('profile-edit/<int:pk>', EditProfileView.as_view(), name='show edit profile'),
    path('profile-delete/<int:pk>', DeleteProfileView.as_view(), name='show delete profile')
]