def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Give me name and phone please.'
        except KeyError:
            return "Contact does not exist"
        except IndexError:
            return 'Give me a name please'
        except TypeError:
            return 'Change contact missing 2 required positional arguments: "name" and "phone"'

    return inner
