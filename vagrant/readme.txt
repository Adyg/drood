Redis
=====
Have a look at: http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/

1. Check it's installed:

    $> redis-server --version

2. Check it's up:

    $> redis-cli ping

3. Connect to the redis server cli:
    
    $> redis-cli

4. Test the setup:
    $> /usr/local/bin/celery --app=drood.celery:app worker --loglevel=INFO

