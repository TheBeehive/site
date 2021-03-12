def hostname(string):
    """Return just the host portion of *string*."""
    return string.split('.', 1)[0]

def domainname(string):
    """Return just the domain portion of *string* or ``Undefined``."""
    from jinja2.runtime import Undefined

    try:
        return string.split('.', 1)[1]
    except IndexError:
        return Undefined(hint=f"No domain in {string!r}")

class FilterModule(object):
    def filters(self):
        return {"hostname": hostname, "domainname": domainname}
