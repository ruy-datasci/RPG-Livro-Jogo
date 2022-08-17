class Check:
    @classmethod
    def type_check(cls, obj, types, name='object'):
        types = types if isinstance(types, type) else tuple(types)
        if not isinstance(obj, types):
            raise TypeError(f'The {name} has to be of one of the following type(s) {types}')


if __name__ == '__main__':
    Check.type_check(2, (int, float))
    Check.type_check('2', (int, float))
