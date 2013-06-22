django-squatter
===============

Django multi-tenancy, without any core patches required!

Perfect for SAAS, saving memory, or other insane mad ideas.

Quickstart
----------

    pip install -e 'git+https://github.com/radiosilence/django-squatter.git'

Add these to settings:
    
    DATABASE_ROUTERS = (
        'squatter.routers.SquatterRouter',
        ...
    )

    MIDDLEWARE_CLASSES = (
        ...
        'squatter.middleware.SelectorMiddleware',
    )

    TEMPLATE_LOADERS = (
        'squatter.template.loaders.by_domain.Loader',
    )

    INSTALLED_APPS = (
        'squatter',
    )
