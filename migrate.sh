#!/bin/bash

export DJANGO_SETTINGS_MODULE=djangomission.settings
./djangomission/manage.py migrate
