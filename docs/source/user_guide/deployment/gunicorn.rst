.. _gunicorn-d:

=========================
使用Gunicorn部署项目
=========================

`Gunicorn <http://docs.gunicorn.org/>`_  是一个由纯Python实现的UNIX类操作系统平台下WSGI服务，它非常容易部署和使用，而且没有别的依赖  

我使用的是nginx+gunicorn进行部署，如果你愿意，你用可以只使用Gunicorn  

另外，这个方法只适用于linux系统下  

安装Gunicorn
===============
.. code-block:: bash

    pip install gunicorn

运行gunicorn
==============

你可以单纯使用命令 ``nohup gunicorn deeru.wsgi & `` 运行，但这样一旦gunicorn意外停止，你的网站就无法访问。
官方介绍了Gaffer、Runit、Supervisor等多种工具帮助你以守护进程的方式运行，详见：http://docs.gunicorn.org/en/stable/deploy.html#monitoring  

这里使用的是 Systemd 的方式运行

1. 新建 ``/etc/systemd/system/gunicorn.service``:: 

    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target

    [Service]
    PIDFile=/run/gunicorn/pid

    # 改为你自己的用户
    User=someuser
    Group=someuser

    RuntimeDirectory=gunicorn

    # DeerU路径
    WorkingDirectory=/home/xxx/DeerU

    # 如果是用了虚拟环境，需要用虚拟环境中gunicorn的绝对路径 '/home/xx/deeru_env/bin/gunicorn'
    
    # workers单核cpu建议不超过2

    # 其他参数参照gunicorn文档

    # 我socket来进行nginx与gunicorn之间的的通信，你也可以改为tcp方式--bind 127.0.0.1:9001 ，这里不再叙述tcp通信方式的配置
    
    ExecStart=/home/xx/deeru_env/bin/gunicorn  --workers 2 --pid /run/gunicorn/pid  --bind unix:/run/gunicorn/socket  deeru.wsgi
    
    ExecReload=/bin/kill -s HUP $MAINPID
    ExecStop=/bin/kill -s TERM $MAINPID
    PrivateTmp=true

    [Install]
    WantedBy=multi-user.target

2. 新建 ``/etc/systemd/system/gunicorn.socket``:: 

    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn/socket

    [Install]
    WantedBy=sockets.target

3. 新建 ``/etc/tmpfiles.d/gunicorn.conf``:: 

    d /run/gunicorn 0755 someuser somegroup -


4. 设置开机启动并开始gunicorn services:: 

    systemctl enable gunicorn.socket

    systemctl start gunicorn.socket

5. 修改nginx配置:: 

    ...

    http {
      
      ...

      upstream app_server {
        server unix:/tmp/gunicorn.sock fail_timeout=0;

        # TCP 方式改为
        # server 192.168.0.7:8000 fail_timeout=0;
      }

     

      server {
        
        ...

        listen 80;

        location / {
          
          try_files $uri @proxy_to_app;
        }

        location @proxy_to_app {
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header Host $http_host;
          # we don't want nginx trying to do something clever with
          # redirects, we set the Host: header above already.
          proxy_redirect off;
          proxy_pass http://app_server;
        }

        # 静态文件
        location ~ ^/(static|media)/   {
         root /home/xxx/project/DeerU;
         add_header Access-Control-Allow-Origin *;
         expires 864000;
        }
        
      }
    }

6. 重启nginx:: 

    nginx -s reload
