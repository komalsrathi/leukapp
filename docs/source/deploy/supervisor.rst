Supervisor
==========

Please ignore this documentation. Supervisor wasn't used at all.

To install `supervisor` and `pip2` I did::

    curl -O https://bootstrap.pypa.io/get-pip.py
    dzdo python2 get-pip.py
    dzdo pip2 install supervisor
    echo_supervisord_conf | dzdo tee /etc/supervisord.conf


I needed to do this::

    cd /usr/lib/python2.6/site-packages/
    dzdo find pip -type f -exec chmod 644 {} ";"
    dzdo find pip -type d -exec chmod 755 {} ";"
    dzdo find pip-7.1.2.dist-info -type f -exec chmod 644 {} ";"
    dzdo find pip-7.1.2.dist-info -type d -exec chmod 755 {} ";"

    dzdo find supervisor -type f -exec chmod 644 {} ";"
    dzdo find supervisor -type d -exec chmod 755 {} ";"
    dzdo find supervisor-3.1.3-py2.6.egg-info -type f -exec chmod 644 {} ";"
    dzdo find supervisor-3.1.3-py2.6.egg-info -type d -exec chmod 755 {} ";"

    dzdo find meld3 -type f -exec chmod 644 {} ";"
    dzdo find meld3 -type d -exec chmod 755 {} ";"
    dzdo find meld3-1.0.2.dist-info -type f -exec chmod 644 {} ";"
    dzdo find meld3-1.0.2.dist-info -type d -exec chmod 755 {} ";"


At `/etc/supervisor/conf.d/production.conf`::

    [program:production]
    command=/opt/rh/rh-python34/root/usr/bin/python /home/medinaj/sites/leukgen.mskcc.org/source/manage.py run_gunicorn
    directory=/home/medinaj/sites/leukgen.mskcc.org/source/
    user=medinaj
    autostart=true
    autorestart=true
    redirect_stderr=True


To use `supervisor` see this `blog post`_.

.. _`blog post`:
    https://davidpoblador.com/run-django-apps-using-gunicorn-and-nginx/
