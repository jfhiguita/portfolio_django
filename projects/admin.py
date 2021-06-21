"""Project admin"""

# django
from django.contrib import admin

# functions to be implemented
from projects.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project admin"""

    list_display = ('pk', 'title', 'technology')

    list_display_links = ('pk', 'title',)

    fieldsets = (
        ('Project', {
            'fields': (
                ('title', 'description'),
                ('technology'),
            ),
        }),
    )
    readonly_fields = ('image',)