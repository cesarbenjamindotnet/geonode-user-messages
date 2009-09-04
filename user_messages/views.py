from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from user_messages.models import Thread, Message

@login_required
def inbox(request, template_name='user_messages/inbox.html'):
    threads = list(Thread.objects.inbox(request.user))
    threads.sort(key=lambda o: o.latest_message.sent_at, reversed=True)
    return render_to_response(template_name, {'threads': threads}, context_instance=RequestContext(request))

@login_required
def thread_detail(request, thread_id, 
    template_name='user_messages/thread_detail.html'):
    qs = Thread.objects.filter(Q(to_user=request.user) | Q(from_user=request.user))
    thread = get_object_or_404(qs, pk=thread_id)
    if request.user == thread.to_user:
        thread.to_user_unread = False
    else:
        thread.from_user_unread = False
    thread.save()
    return render_to_response(template_name, {'thread': thread}, context_instance=RequestContext(request))
