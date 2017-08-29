from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _
import markdown
from django.core.urlresolvers import reverse


from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ("-create_date",)
    def get_content(self):
        return markdown.markdown(self.content)





    def up_votes(self):
        return BlogActivity.objects.filter(blog=self).filter(activity_type='U').count()
    def down_votes(self):
        return BlogActivity.objects.filter(blog=self).filter(activity_type='D').count()


    def __str__(self):
        return self.title
    def get_comments(self):
        return BlogComment.objects.filter(blog=self)

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = _("Blog Comments")
        verbose_name = _("Blog Comment")
        ordering = ("-date" , )

    def up_votes(self):
        return BlogCommentActivity.objects.filter(blog_comment=self).filter(activity_type='U').count()
    def down_votes(self):
        return BlogCommentActivity.objects.filter(blog_comment=self).filter(activity_type='D').count()


    def __str__(self):
        return '{0} - {1}'.format(self.user.username , self.blog.title)

    def get_comment(self):
        return self.comment




class Activities:
    FAVORITE = 'F'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE , 'Favorite'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE , 'Down Vote'),
    )

class BlogActivity(models.Model):
    blog = models.ForeignKey(Blog)
    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=Activities.ACTIVITY_TYPES)

    class Meta:
        verbose_name_plural = _("Blog Activity")
        verbose_name = _("Blog Activities")


class BlogCommentActivity(models.Model):
    blog_comment = models.ForeignKey(BlogComment)
    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=Activities.ACTIVITY_TYPES)

    class Meta:
        verbose_name_plural = _("Blog Comment Activity")
        verbose_name = _("Blog Comment Activities")
