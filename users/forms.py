
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UsersRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

