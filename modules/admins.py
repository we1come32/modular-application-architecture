from . import command


@command(name="Hello, world", command="hello")
def hello_world(*data, **kwargs):
    print("Hello, world")
