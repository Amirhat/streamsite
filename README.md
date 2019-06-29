# live stream with Django + nginx + hls


# edit 
```
sudo apt update
sudo apt-get install build-essential libpcre3 libpcre3-dev libssl-dev




wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.42.tar.gz
tar -zxf pcre-8.42.tar.gz
rm -rf pcre-8.42.tar.gz
cd pcre-8.42
./configure
make
sudo make install
cd


wget http://zlib.net/zlib-1.2.11.tar.gz
tar -zxf zlib-1.2.11.tar.gz
rm -rf zlib-1.2.11.tar.gz
cd zlib-1.2.11
./configure
make
sudo make install
cd 


wget http://www.openssl.org/source/openssl-1.0.2q.tar.gz
tar -zxf openssl-1.0.2q.tar.gz
rm -rf openssl-1.0.2.tar.gz
cd openssl-1.0.2q
./config
make
sudo make install
cd


git clone git://github.com/arut/nginx-rtmp-module.git



wget https://nginx.org/download/nginx-1.14.2.tar.gz
tar zxf nginx-1.14.2.tar.gz
rm -rf nginx-1.14.2.tar.gz
cd nginx-1.14.2




./configure  --add-module=../nginx-rtmp-module \
--sbin-path=/usr/sbin/nginx \
--lock-path=/var/run/nginx.lock \
--conf-path=/etc/nginx/nginx.conf \
--pid-path=/run/nginx.pid \
--with-pcre=../pcre-8.42 \
--with-zlib=../zlib-1.2.11 \
--with-openssl=../openssl-1.0.2q \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--user=nginx \
--group=nginx \
--with-http_auth_request_module \
--with-http_degradation_module \
--with-http_gunzip_module \
--with-http_gzip_static_module \
--with-http_mp4_module \
--with-http_perl_module \
--with-http_realip_module \
--with-http_secure_link_module \
--with-http_slice_module \
--with-http_ssl_module  \
--with-http_stub_status_module \
--with-http_v2_module \
--with-stream_ssl_module \
--with-stream \
--with-threads \
--prefix=/etc/nginx



make
sudo make install

```

### compile and install nginx:

open terminal and download nginx
```
wget http://nginx.org/download/nginx-1.14.1.tar.gz
tar -zxvf nginx-1.14.1.tar.gz
```
download nginx-rtmp-module
```
git clone https://github.com/sergey-dryabzhinsky/nginx-rtmp-module.git
git clone https://github.com/kaltura/nginx-vod-module.git
```
install packages
```
sudo apt-get install build-essential libpcre3 libpcre3-dev libssl-dev
```
download zlib
```
wget http://zlib.net/zlib-1.2.11.tar.gz
tar -zxxvf zlib-1.2.11.tar.gz
```
make nginx and install
```
cd nginx-1.14.1
./configure --add-module=../nginx-rtmp-module/ --add-module=../nginx-vod-module/ --with-file-aio --with-threads --with-zlib=../zlib-1.2.11
make
sudo make install
```

### install Django + uwsgi

install python3
```
sudo apt-get update
sudo apt-get install python3-pip
```
install virtualenv
```
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv virtualenvwrapper
```
virtualenvwrapper 
```
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

source ~/.bashrc
```
Create Project
```
mkvirtualenv streamsite
```
install packeges
```
pip install django
```
start project 
```
cd ~
django-admin.py startproject streamsite

```
migrate
```
cd ~/streamsite
~/streamsite/manage.py migrate
~/streamsite/manage.py createsuperuser
```
collectstatic
```
~/streamsite/manage.py collectstatic
```

change setting.py

```
nano ~/streamsite/streamsite/settings.py
```
in setting.py:

```
"""
Django settings for streamsite project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# enter you ip or hostname + '127.0.0.1'
ALLOWED_HOSTS = ['192.168.56.101','127.0.0.1','localhost','192.168.56.102']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'boltstream',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'streamsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'streamsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

```

now add app1 to sour django

```
python manage.py startapp boltstream
```
and config urls.py
```
nano ~/streamsite/streamsite/utls.py
```
in urls.py:
```
"""streamsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from boltstream.views import shiny_auth, shiny_auth2

urlpatterns = [
    path("auth", shiny_auth),
    path("auth2", shiny_auth2),
    path("admin/", admin.site.urls),
]

```

and go to views
```
nano ~/streamsite/boltsteam/views.py
```
in views.py
```
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Stream


def shiny_auth(request):
    if request.user.is_authenticated:
        return HttpResponse(status=200)
    return HttpResponse(status=403)

@csrf_exempt
def shiny_auth2(request):
    if 'psk' in request.POST:
        if request.POST['psk'] == 'totallysecretpassword':
            return HttpResponse(status=200)
    return HttpResponse(status=403)
```
and admin.py
```
nano ~/streamsite/boltsteam/admin.py
```
admin.py:
```

```
and models.py
```
nano ~/streamsite/boltsteam/models.py
```
models.py:
```
```
migrate
```
cd ~/streamsite
~/streamsite/manage.py migrate
~/streamsite/manage.py createsuperuser
```
you can use workon and deactivate to activate and deactivate venv
```
deactivate
workon streamsite
```
now deactive venv and install uwsgi:
```
deactivate
sudo apt-get install python3-dev
sudo -H pip3 install uwsgi
```

and configure its service
```
sudo mkdir -p /etc/uwsgi/sites
```
add your site:
```
sudo nano /etc/uwsgi/sites/streamsite.ini
```
in /etc/uwsgi/sites/streamsite.ini:
```
[uwsgi]
project = streamsite
uid = amir
base = /home/%(uid)

chdir = %(base)/%(project)
home = %(base)/Env/%(project)
module = %(project).wsgi:application

master = true
processes = 5

socket = /run/uwsgi/%(project).sock
chown-socket = %(uid):www-data
chmod-socket = 660
vacuum = true
```

and edit 
/etc/systemd/system/uwsgi.service
```
sudo nano /etc/systemd/system/uwsgi.service
```
in /etc/systemd/system/uwsgi.service:

```
[Unit]
Description=uWSGI Emperor service

[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown amir:www-data /run/uwsgi'
ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```
# configure nginx

first edit nginx.cong
```
cd /etc/nginx/
sudo nano nginx.conf
```
in nginx.conf
```
user www-data;

worker_processes 1;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 1024;
	# multi_accept on;
}

http {
	log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for" $request_time';
	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##

	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;


	# hls server

	server {
        listen       8080;
        server_name localhost 192.168.56.102;


        # this two blocks for serving hls for authenticated user
		#auth start
	
        location = /auth {
            internal;
            proxy_pass              http://127.0.0.1;
            proxy_pass_request_body off;
            proxy_set_header        Content-Length "";
            proxy_set_header        X-Original-URI $request_uri;
        }

		#private
        location /private/ {
		root /home/amir/streamsite;
            auth_request     /auth;
            auth_request_set $auth_status $upstream_status;

        }
		#private



        location /hls {

            auth_request     /auth;
            auth_request_set $auth_status $upstream_status;
		
            # Serve HLS fragments
            # CORS setup
            add_header 'Access-Control-Allow-Origin' '*' always;
            add_header 'Access-Control-Expose-Headers' 'Content-Length';
            # allow CORS preflight requests
            if ($request_method = 'OPTIONS') {
                add_header 'Access-Control-Allow-Origin' '*';
                add_header 'Access-Control-Max-Age' 1728000;
                add_header 'Content-Type' 'text/plain charset=UTF-8';
                add_header 'Content-Length' 0;
                return 204;
            }
            types {
                application/vnd.apple.mpegurl m3u8;
                video/mp2t ts;
            }
            root /tmp;
            add_header Cache-Control no-cache;
        }
    }

	#end hsl server
	
}
	
#rtmp
rtmp {

    server {
        listen 1935;
        chunk_size 8192;


        application hls {
		live on;
		on_publish http://127.0.0.1/auth2;

		hls_playlist_length 120m;
		#hls_nested on;

		# this can play playlist at start
		hls_type event;
		recorder all {
				record all;
				record_path /tmp/live;
				record_max_size 100000K;
				#record_max_frames 4;
				record_unique on;
				record_suffix _%d%m%Y_%H%M%S.flv;
				record_append on;
				#record_interval 5s;
				#record_notify on;
				#exec_record_done ffmpeg -i $path  -f mp4 /tmp/live/$basename.mp4;
			}

            meta copy;
            hls on;
            hls_path /tmp/hls;
		}
    }
}

#end rtmp

#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
# 
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
# 
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
# 
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}
```

config streamsite in nginx
```
sudo nano /etc/nginx/sites-available/streamsite
```
in sudo nano /etc/nginx/sites-available/streamsite
```
server {
    listen 80;
    server_name amir.com www.amir.com 192.168.56.102 127.0.0.1;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/amir/streamsite;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/run/uwsgi/streamsite.sock;
    }
}

```
and active streamsite config
```
sudo ln -s /etc/nginx/sites-available/streamsite /etc/nginx/sites-enabled
```

create dires
```
mkdir /tmp/live
mkdir /tmp/hls
```
and in the last config firewall:
```
sudo ufw delete allow 8080
sudo ufw allow 'Nginx Full'
```
and restart services
```
sudo systemctl enable nginx
sudo systemctl enable uwsgi
```

at last for basic usage copy streamsite/private into your project

now you can stream site by obs in:
server:
rtmp://yourip_or_domin/hls
stream key:
stream?psk=totallysecretpassword

### enjoy!
