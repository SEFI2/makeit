

from django.db.models import Q
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Message(models.Model):
    from_user = models.ForeignKey(User , related_name='+')
    to_user = models.ForeignKey(User , related_name='+')
    current_user = models.ForeignKey(User , related_name='+')

    message = models.CharField(max_length=1000 , blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
        ordering = ('date', )
        db_table = 'messages_message'
    def __str__(self):
        return self.message

    @staticmethod
    def get_all_messages(self , user):
        return Message.objects.filter(Q(from_user=user) | Q(to_user=user))




    @staticmethod
    def send_message(from_user, to_user, message):
        message = message[:1000]
        Message(from_user=from_user,to_user=to_user,message=message,current_user=from_user,is_read=True).save()
        Message(from_user=from_user, to_user=to_user, message=message, current_user=to_user, is_read=False).save()


