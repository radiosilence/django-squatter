from squatter.utils import (
    alias_from_domain,
    get_site,
)


class TenancyRouter(object):
    def _name(self, model, **hints):
        site = get_site()
        if site is None:
            alias = 'default'
        else:
            alias = alias_from_domain(site.domain)
        return alias
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        return self._name(model, **hints)

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        return self._name(model, **hints)