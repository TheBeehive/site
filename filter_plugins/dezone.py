from ansible.errors import AnsibleFilterError

def dezone(string, zone):
    """Return *string* without the *zone* suffix, or raise an error."""
    from jinja2.runtime import Undefined

    if not string.endswith("." + zone):
        raise AnsibleFilterError(f"Host {string!r} isn't in zone {zone!r}")
    return string[:-len("." + zone)]

class FilterModule(object):
    def filters(self):
        return {"dezone": dezone}
