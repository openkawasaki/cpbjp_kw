川崎シビックパワーバトル
===========

pyenv
-----

インストール可能バージョン

    $ pyenv install -l

インストール済みを表示

    $ pyenv versions

インストール

    $ pyenv install 3.6.4
    $ pyenv rehash

virtualenvを作成

    $ $ pyenv virtualenv 3.6.4 cpbjp_kw

ローカル環境設定

    $ pyenv local cpbjp_kw
    $ pyenv exec pip install --upgrade pip

環境をコピーしたい

    $ pip freeze -l
    $ pip freeze > requirements.txt
    $ pip install -r requirements.txt

git
-----

    $ brew install git-flow

    $ git init
    $ git flow init -d

    $ git push --all
    $ git push --set-upstream origin develop

database
-----

データベース一覧

    $ psql -U postgres -l

データベース作成

    $ createdb -U postgres -E UTF8 -T template0 --lc-collate=ja_JP.UTF-8 --lc-ctype=ja_JP.UTF-8 cpbjp_kw

データベース作成

    $ dropdb -U postgres cpbjp_kw

PostGISの拡張をインストール

    $  psql -U postgres -d cpbjp_kw -c "CREATE EXTENSION postgis;"

データベース、テーブル、スキーマ、ユーザ確認

    $ psql -U postgres cpbjp_kw
    mcr=# ¥dx
    mcr=# ¥du
    mcr=# ¥dn
    mcr=# ¥d index.*
    mcr=# ¥q
    $ exit

Django
------

    $ pip install django
    $ pip install django-admin-tools
    $ pip install django-environ
    $ pip install django-extensions
    $ pip install django-filter
    $ pip install djangorestframework
    $ pip install gunicorn
    $ pip install markdown
    $ pip install numpy
    $ pip install pandas
    $ pip install psycopg2-binary
    $ pip install python-dateutil

    $ django-admin startproject config .

    $ python manage.py startapp top

    $ touch top/serializers.py
    $ touch top/apis.py
    
    $ mkdir logs
    $ mkdir dist

    $ touch logs/.delete.me
    $ touch dist/.delete.me

    $ python manage.py makemigrations
    $ python manage.py migrate

contrib
-----

    $ mkdir contrib
    $ cd contrib
    $ npm init

    $ mkdir js
    $ mkdir css
    $ mkdir fonts