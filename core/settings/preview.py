"""Isolated local QA; never use this module for production traffic."""
import os
os.environ.setdefault('SECRET_KEY', 'binux-local-preview-only')
os.environ.setdefault('DEBUG', 'True')
os.environ.setdefault('ALLOWED_HOSTS', '127.0.0.1,localhost,testserver')
from .base import *
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']

DATABASES['default']['NAME'] = '/tmp/binux-preview.sqlite3'
