from django.contrib import admin
from projects.models import Project, Technology

# Register your models here.

class TechnologyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project)
admin.site.register(Technology, TechnologyAdmin)