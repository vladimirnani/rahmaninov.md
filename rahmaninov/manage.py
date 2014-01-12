#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line

PROJECT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '')
if not PROJECT_PATH in sys.path:
    sys.path.insert(1, PROJECT_PATH)

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'rahmaninov.settings.settings')
    execute_from_command_line(sys.argv)
