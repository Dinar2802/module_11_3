import inspect
from pprint import pprint


def introspection_info(obj):
    type_ = type(obj)
    attribute = getattr(obj, '__dict__', None)
    methods = dir(obj)
    module = inspect.getmodule(obj)
    info = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module}
    return info


number_info = introspection_info(42)
pprint(number_info)
