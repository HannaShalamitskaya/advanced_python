class ClassMembers(dict):
    def __init__(self):
        self.members = []
        super(ClassMembers, self).__init__()

    def __setitem__(self, key, value):
        if key not in self:
            self.members.append(key)
        dict.__setitem__(self, key, value)

        # add property for special methods
        if key[:3] in ('get', 'set', 'del'):
            property_name = key[4:]
            property_method = key[:3]
            if property_name not in self:
                self.members.append(property_name)

            try:
                custom_property = dict.__getitem__(self, property_name)
            except KeyError:
                custom_property = property(**{'f' + key[:3]: value})
            else:
                prop_params = dict(fget=custom_property.fget,
                                   fset=custom_property.fset,
                                   fdel=custom_property.fdel)
                prop_params['f' + property_method] = value

                custom_property = property(**prop_params)

            dict.__setitem__(self, property_name, custom_property)


class PropertyMeta(type):
    @classmethod
    def __prepare__(cls, name, baseClasses):
        return ClassMembers()

    def __new__(cls, name, baseClasses, classdict):
        result = type.__new__(cls, name, baseClasses, dict(classdict))
        return result


class Example(metaclass=PropertyMeta):
    def __init__(self):
        self._x = 12
        self._y = "Magic!"

    def get_y(self):
        print("getter for _y")
        return self._y

    def set_y(self, value):
        print("setter for _y")
        self._y = value

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        print("Goodbye, _x!")
        del self._x


if __name__ == "__main__":
    ex = Example()

    print(ex.y)
    ex.y = "Other value"
    print(ex.y)

    print(ex.x)
    ex.x = 255
    print(ex.x)
    del ex.x
    try:
        print(ex.x)
    except Exception as error:
        print(error)
