import os
import sys
from django.core.wsgi import get_wsgi_application

PROJECT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '')
if not PROJECT_PATH in sys.path:
    sys.path.insert(1, PROJECT_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "rahmaninov.settings.live")
application = get_wsgi_application()
