cd drood && \
env SECRET_KEY=`heroku config:get SECRET_KEY --app=drood` \
    AWS_SECRET_ACCESS_KEY=`heroku config:get AWS_SECRET_ACCESS_KEY --app=drood` \
    AWS_ACCESS_KEY_ID=`heroku config:get AWS_ACCESS_KEY_ID --app=drood` \
    AWS_STORAGE_BUCKET_NAME=`heroku config:get AWS_STORAGE_BUCKET_NAME --app=drood` \
    STATIC_ROOT='/vagrant/drood/assets' \
    /usr/bin/python manage.py collectstatic --settings=drood.settings.heroku
cd ..