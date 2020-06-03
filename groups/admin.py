from django.contrib import admin

# Register your models here.
from . import models


class GroupMemberInline(admin.TabularInline):#gives us ability to edit models on the same page as parent model
    model = models.GroupMember



admin.site.register(models.Group)
