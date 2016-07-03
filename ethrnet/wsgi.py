import os
import sys
import site
site.addsitedir(
    '/home/vishal/.virtualenvs/ethernet/local/lib/python2.7/site-packages')

sys.path.append('/var/www/ethernet/ethrnet')
sys.path.append('/var/www/ethernet/ethrnet/ethrnet')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ethrnet.settings'

# activate_env = os.path.expanduser('/home/vishal/.virtualenvs/ethernet/bin/activate_this.py')

# execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ethrnet.settings")

application = get_wsgi_application()
