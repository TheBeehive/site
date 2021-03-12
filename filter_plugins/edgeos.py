def edgeos_action(object, on=None):
    """
    Return the appropriate EdgeOS configuration command to send with *object*.

    Unless *on* is specified, return "set" if *object* evaluates to ``True`` or
    "delete" if *object* evaluates to ``False``.

    When *on* is specified, if *object* evaluates to ``True``, then return an
    EdgeOS configuration command to set the configuration node specified by
    *on* to *object*. If *object* evaluates to ``False``, then return an EdgeOS
    configuration command to delete the configuration node specified by *on*.
    """

    if on is None:
        return "set" if object else "delete"
    if not object:
        return f"delete {on}"
    return f"set {on} {object}"

class FilterModule(object):
    def filters(self):
        return {"edgeos_action": edgeos_action}
