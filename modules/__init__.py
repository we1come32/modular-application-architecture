import importlib

modules = [
    'messages',
    'admins',
]


commands = []
errors = []


def command(name="", command=""):
    global commands

    def decorator(func):
        commands.append([name, command, func])

        def decorator_2(*data, **kwargs):
            return func(*data, **kwargs)

        return decorator_2

    return decorator


loaded_modules = {}


__all__ = []


def load():
    global loaded_modules, modules, errors, commands
    for module in modules:
        try:
            loaded_modules[module] = __import__("modules." + module, fromlist=[None])
        except Exception as e:
            errors += [str(e)]
    return {
        'commands': commands,
        'errors': errors
    }
