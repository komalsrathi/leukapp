.. This is a comment.
.. |date| date::

********
ssh tips
********

.. bibliographic fields (which also require a transform):
:author: Juan Medina
:contact: medinaj@mskcc.org
:organization: Memorial Sloan-Kettering
:status: This is "work in progress"
:date: |date|

:abstract:
    Some ssh tips. This wiki is based on the following links:

    * `ssh`_

    .. _ssh: http://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html

    Typographical conventions:

    * ``constant width`` for code fragments, commands or object attributes
    * *italic* for file names
    * **bold** important terms

.. meta::
   :keywords: leukid, sample_form, models, sample, data unit
   :description lang=en: Some ssh tips.

.. contents:: Table of Contents
.. .. section-numbering::


Tunnel Forwarding
+++++++++++++++++

Connecting to the database behind the server firewall.

.. code-block:: shell

    ssh -L 9000:localhost:5432 plvleukweb1.mskcc.org


import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('luna.mskcc.org', username='medinaj', password='', key_filename='/Users/medinaj/.ssh/id_rsa.pub')
