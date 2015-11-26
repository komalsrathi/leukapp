# -*- coding: utf-8 -*-

"""
Code used across the leukapp :mod:`~leukapp.apps`.
"""

# django
from django.core.exceptions import ImproperlyConfigured

# thirdparty
import environ
import paramiko

env = environ.Env()


class LeukConnect(object):

    """NOTTESTED
    This class is used to send commands to the Leukgen Data Center (leukdc)
    """

    def __init__(self):
        if env('LEUKDC_ACTIVE') == 'TRUE':
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.LEUKDC_PROJECTS_DIR = env('LEUKDC_PROJECTS_DIR')
            self.LEUKDC_SAMPLES_DIR = env('LEUKDC_SAMPLES_DIR')
            self.LEUKDC_HOST = env('LEUKDC_HOST')
            self.LEUKDC_USER = env('LEUKDC_USER')
            self.LEUKDC_PASSWORD = env('LEUKDC_PASSWORD')
            self.LEUKDC_SSHKEY = env('LEUKDC_SSHKEY')
            self.DEPLOYMENT = env('DEPLOYMENT')
        else:
            msg = 'LEUKDC_ACTIVE environment variable must be set to TRUE'
            raise(ImproperlyConfigured(msg))

    def connect(self):
        self.ssh.connect(
            self.LEUKDC_HOST,
            username=self.LEUKDC_USER,
            password=self.LEUKDC_PASSWORD,
            key_filename=self.LEUKDC_SSHKEY,
            )

    def exec_command(self, command):
        return self.ssh.exec_command(command)

    def close(self):
        self.ssh.close()
