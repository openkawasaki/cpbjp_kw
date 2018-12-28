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


サーバ
-----

* [Ubuntuサーバへのdjangoアプリdeploy方法](https://qiita.com/maisuto/items/e4e69e34fb00dac8170a)


#### visudo して変更
sudoするときにいちいちパスワードを聞かれる

    -%sudo ALL=(ALL:ALL) ALL
    +%sudo ALL=(ALL:ALL) NOPASSWD: ALL

visudo で起動するエディタは nanoなのでviに変更

    $ sudo update-alternatives --config editor

#### アップデート

    $ sudo apt-get update
    言語パックインストール
    $ sudo apt-get -y install language-pack-ja-base language-pack-ja
    言語設定
    $ sudo update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"

#### タイムゾーン設定

    $ sudo cp /etc/localtime /etc/localtime.org
    $ sudo ln -sf /usr/share/zoneinfo/Japan /etc/localtime


supervisor
-----
    supervisor
    $ sudo apt-get install supervisor


    $ sudo vi /etc/supervisor/conf.d/cpbjp_kw.conf

    [program:cpbjp_kw]
    user=ubuntu
    directory=/home/ubuntu/cpbjp_kw
    #command=/home/ubuntu/.pyenv/shims/gunicorn config.wsgi:application --bind=0.0.0.0:9000 --workers=4 --timeout 7200
    command=/home/ubuntu/.pyenv/shims/gunicorn config.wsgi:application --workers=4 --timeout 7200 --bind=unix:///tmp/cpbjp_kw.sock
    stdout_logfile=/var/log/cpbjp_kw/stdout.log
    stderr_logfile=/var/log/cpbjp_kw/stderr.log
    numprocs = 1
    stdout_logfile_maxbytes = 10MB
    stderr_logfile_maxbytes = 10MB
    stdout_logfile_backups = 5
    stderr_logfile_backups = 5
    autostart = true
    autorestart = true
    redirect_stderr=true
    environment = LANG=ja_JP.UTF-8,LC_ALL=ja_JP.UTF-8,LC_LANG=ja_JP.UTF-8

    $ cd /var/log
    $ sudo mkdir cpbjp_kw
    $ sudo chown ubuntu cpbjp_kw

    $ sudo supervisorctl
    supervisor> reload
    Really restart the remote supervisord process y/N? y
    Restarted supervisord
    supervisor> status
    cpbjp_kw                         RUNNING   pid 32348, uptime 0:00:08
    supervisor> exit

    $ ls -al /tmp/cpbjp_kw.sock
    srwxrwxrwx 1 ubuntu ubuntu 0  7月 22 19:23 /tmp/cpbjp_kw.sock

nginx
----

    nginx
    $ sudo apt-get install nginx

    $sudo vi  /etc/nginx/sites-available/cpbjp_kw.conf

    upstream cpbjp_kw-app {
        server unix:///tmp/cpbjp_kw.sock;
    }

    server {
        listen 80;
        server_name cpb.openkawasaki.org

        access_log /var/log/nginx/cpbjp_kw.log;
        error_log /var/log/nginx/cpbjp_kw_error.log;

        proxy_pass_header Server;
        proxy_set_header Host $host;
        proxy_set_header REMOTE_ADDR $remote_addr;

        location /static {
            root /home/ubuntu/cpbjp_kw/dist/;
        }

        location / {
            proxy_pass http://cpbjp_kw-app;
        }
    }

    $ cd /etc/nginx/sites-enabled
    $ sudo ln -s ../sites-available/cpbjp_kw.conf cpbjp_kw.conf

    $ sudo nginx -s reload


### iptables(firewall)の設定

    $ sudo vi /etc/iptables/iptables.rule

    追加
    -A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
    -A INPUT -m state --state NEW -m tcp -p tcp --dport 443 -j ACCEPT

    $ sudo iptables-restore < /etc/iptables/iptables.rule