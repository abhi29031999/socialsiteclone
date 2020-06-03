from django.contrib.auth import get_user_model
#Instead of referring to User directly, you should reference the user model using django.contrib.auth.get_user_model(). This method will return the currently active User model – the custom User model if one is specified, or User otherwise.

from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()
    #setting up labels copied from reference
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)#__init__ is a constructor
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
