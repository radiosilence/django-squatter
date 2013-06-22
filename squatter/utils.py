import json

from django.db.utils import load_backend


try:
    import threading
    currentThread = threading.currentThread
except ImportError:
    def currentThread():
        return "no threading"

_sites = {}


def set_site(site, cls):
    from django.db import connections
    try:
        tenant = cls.objects.get(site=site)
        alias = alias_from_domain(site.domain)
        db = {
            'ENGINE': tenant.database_engine,
            'HOST': tenant.database_host,
            'NAME': tenant.database_name,
            'USER': tenant.database_user,
            'PORT': tenant.database_port,
            'PASSWORD': tenant.database_password,
            'OPTIONS': json.loads(tenant.database_options),
        }
        backend = load_backend(db['ENGINE'])
        conn = backend.DatabaseWrapper(db, alias)
        connections[alias] = conn
        _sites[currentThread()] = site
    except Exception:
        raise Exception('There was an issue loading database configuration for this site.')


def get_site():
    return _sites.get(currentThread(),None)


def alias_from_domain(domain):
    """
    This pulls off the port, www, and .local, so if you have a website called
    www.hello.com, you can use hello.com.local:8000 in development.
    """

    alias = ':'.join(domain.split(':')[:-1])
    if alias.endswith('.local'):
        alias = alias[:-6]
    if alias.startswith('www.'):
        alias = alias[4:]
    alias.replace('.', '_')