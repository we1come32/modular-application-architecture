from . import command


@command(name="func2", command="hello, pidor")
def pidor(*data, **kwargs):
    print("Pidor")
