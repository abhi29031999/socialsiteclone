
from django.urls import reverse
from django.db import models
from django.utils.text import slugify#used to remove alphanumeric,hyphin,underscore so that if someone has a username with spaces it can replace it with underscores and change tolowercase
# from accounts.models import User

#import misaka
#helps with links and markdown text

from django.contrib.auth import get_user_model#return current;y active user model
User = get_user_model()#allows us to call things from the current user

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag

from django.template.defaultfilters import register
@register.filter(name='has_group')
def has_group(user,name):
    return user.groups.filter(name=name).exists()
#this helped us to grab group member by its get_related_name

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")#all the members of that group

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = self.description#misaka.html()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:#The Django Meta class is a special thing through out Django which is used to transfer information about the model or other object to the Django framework
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)#related to user through user_groups

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")# lists that must be unique when considered together.
