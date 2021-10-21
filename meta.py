class CustomMeta:
    def __new__(meta_cls, class_name, class_parents, class_attrs):
        custom_attrs = {}
        for attr_name, attr_value in class_attrs.items():
            # Don't change magic methods
            if attr_name.startswith('__') and attr_name.endswith('__'):
                custom_attrs[attr_name] = attr_value
            else:
                custom_attrs['custom_' + attr_name] = attr_value

        custom_attrs['__setattr__'] = lambda self, name, value: object.__setattr__(self, 'custom_' + name, value)

        return type(class_name, class_parents, custom_attrs)


class CustomPerson(metaclass=CustomMeta):
    age = 20

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.custom_first_name + ' ' + self.custom_last_name

    def legal_age(self):
        return 18
