"""Blog admin"""

# django
from django.contrib import admin

# blog models
from blog.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""

    list_display = ('pk', 'title', 'created_on')

    list_display_links = ('pk','title')

    search_fields = ('title', 'categories__name__contains')

    list_filter = ('created_on', 'last_modified')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

