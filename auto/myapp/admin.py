from django.contrib import admin
from . models import Login,Team,Normal,News

# Register your models here.
admin.site.register(Login)
admin.site.register(Team)
admin.site.register(Normal)
admin.site.register(News)