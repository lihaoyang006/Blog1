from django.contrib import admin
from blog.models import Blog, User


class BlogAdmin(admin.AdminSite):
    index_title = 'Index'
    site_header = 'Blog Admin'
    site_title = 'HappyBlog'

class DisplayBlog(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_time')
    search_fields = ('title',)

class DisplayUser(admin.ModelAdmin):
    list_display = ('nick', 'email', 'type', 'create_time', 'modify_time')
    search_fields = ('nick',)



blog_admin = BlogAdmin(name='blog_admin')
blog_admin.register(Blog, DisplayBlog)
blog_admin.register(User, DisplayUser)
