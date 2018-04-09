from django.contrib import admin

from .models import Types
from .models import Posts
from .models import Messages
admin.site.register(Types)
admin.site.register(Posts)
admin.site.register(Messages)