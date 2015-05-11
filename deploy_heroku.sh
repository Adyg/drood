git push origin master
#git subtree push --force --prefix drood heroku master
git push heroku `git subtree split --prefix drood master`:master --force