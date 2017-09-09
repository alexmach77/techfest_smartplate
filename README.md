##Techfest Munich Github Project

## Set environment

```
conda create -n techfest_munich python=3.6
source activate techfest_munich
```

```
pip install tensorflow
conda install -c anaconda flask gunicorn
conda install scikit-learn
pip freeze > requirements.txt

```
Create Procfile file in root with:

	web: gunicorn app:app

Create Heroku app
https://progblog.io/How-to-deploy-a-Flask-App-to-Heroku/
heroku login
cd root
heroku git:remote -a appname

git add .
git commit -am 
git push heroku master

1. Create github repository

	git init
	git add README.md
	git commit -m "first commit"
	git remote add origin https://github.com/alexmach77/techfest_smartplate.git
	git push -u origin master

2. Install Heroku

		brew install heroku/brew/heroku
		cd root project path
		heroku create
		git remote -v
		git remote rename heroku techfest_munich#rename app
		git push techfest_munich master
