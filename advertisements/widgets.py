from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Posts

class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Posts


admin.site.register(Posts)