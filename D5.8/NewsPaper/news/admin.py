from django.contrib import admin

from .models import Author, Category, PostCategory, Post, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
# admin.site.register(Post)
admin.site.register(Comment)


class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'post'
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]


admin.site.register(Post, PostAdmin)