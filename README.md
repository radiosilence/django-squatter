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
        'squatter.template.loaders.Loader',
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
* Schemas option
* Static loader
* Testing
* Tests
* Some way of doing things like migrate/syncdb from the command line.

Inspiration
-----------

 * Neelesh Shastry - The guy who inspired the whole thing with that Posterous article: https://github.com/neeleshs
 * https://github.com/bruth
 * Andy Baker