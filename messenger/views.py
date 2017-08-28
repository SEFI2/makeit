from django.shortcuts import render
from django.db.models import Q



# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import Message

from django.contrib.auth.models import User


@login_required
def MessengerView(request , username):
    if request.method == 'POST':
        message = request.POST.get("message", "")
        to_user = User.objects.get(username=username)
        Message.send_message(request.user , to_user, message)
    current_user_messages = Message.objects.filter(current_user=request.user).filter(Q(to_user__username=username) | Q(from_user__username=username))
    return render(request, 'messenger/messages.html' , {"messages":current_user_messages} )


