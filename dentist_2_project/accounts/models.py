from django.contrib.auth import models as auth_models
from django.db import models
from dentist_2_project.accounts.managers import AppUsersManager

'''
1 - create the model extending abstract user and permissions mixin
2 - define fields desired - 'email', 'is_staff', 'date_joined', 'objects'
3 - define AUTH_USER_MODEL = '$appname.$classname' in settings.py
4 - create user manager (add objects field = class in manager.py and invoke it) - create managers.py in the app desired
5 - manager inherits BaseUserManager then go to UserManager copy paste the first 3 methods (create_user methods) and
    modify 'username' to become 'email' variable and delete some stuff -> check managers.py folder
'''


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False,)
    is_staff = models.BooleanField(default=False,)
    date_joined = models.DateTimeField(auto_now_add=True,)
    objects = AppUsersManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    GENDERS = (('Male', 'Male'), ('Female', 'Female'), ('LGBT+', 'LGBT+'), ('Prefer Not to Tell', 'Prefer Not to Tell'),)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField()
    gender = models.CharField(max_length=30, choices=GENDERS)
    phone = models.CharField(max_length=10)
    image = models.ImageField()
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
