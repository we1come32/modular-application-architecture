from . import command


@command(name="Hello, world", command="tipo command")
def hello_world(*data, **kwargs):
    print("Hello, world")
