import os

from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from django.utils.text import slugify

import settings

from squatter.utils import (
    get_tenant,
)


class Loader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        
        tenant = get_tenant()
        if tenant:
            alias = tenant.alias

            for dir_ in settings.TEMPLATE_DIRS:
                path = os.path.join(dir_, alias, template_name)
                try:
                    return open(path).read(), template_name
                except IOError:
                    pass
        raise TemplateDoesNotExist, template_name
