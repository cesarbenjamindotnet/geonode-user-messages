User messaging
==============

This repo was forked to fix compatibility issues with geonode and django 4.2.x. Geonode 4.3.1 now is fully compatible, so, i have to archive this repo and delete it on Jan 2025.

``user-messages`` is an application for allowing users of your Django site to
send messages to each other.


Quick Start
-----------

Include ``user-messages`` in your requirements file and add
``"user_messages"`` to your INSTALLED APPS setting.

Once you have the ``user-messages`` installed, hook up the URLs::
    
    urlpatterns = patterns("",
        # some cool URLs
        
        (r"^messages/", include("user_messages.urls")),
        
        # some other cool URLs
    )

Now all you need to do is wire up some templates.
