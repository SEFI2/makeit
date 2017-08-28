from django.contrib import admin
from .models import Blog , BlogComment, BlogActivity , BlogCommentActivity


# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogActivity)
admin.site.register(BlogCommentActivity)

