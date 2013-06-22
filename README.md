django-squatter [pre-alpha]
===========================

** DO NOT FUCKING USE THIS YET **

Django multi-tenancy, without any core patches required!

Perfect for SAAS, saving memory, or other insane mad ideas.


Quickstart
----------

    pip install -e 'git+https://github.com/radiosilence/django-squatter.git'

Add these to settings:
    
    DATABASE_ROUTERS = (
        'squatter.routers.TenancyRouter',
        ...
    )

    MIDDLEWARE_CLASSES = (
        ...
        'squatter.middleware.TenancyMiddleware',
    )

    TEMPLATE_LOADERS = (
        'squatter.template.loaders.by_domain.Loader',
    )

    INSTALLED_APPS = (
        ...
        'squatter',
        ...
    )

Do a migration, etc.

To-Do
-----

* Template loader
* Docs
* Static loader
* Testing
* Tests