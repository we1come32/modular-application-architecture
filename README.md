# Modular application architecture
How to use:
  1) Create file <module_name>.py in directory modules
  2) In the <module_name>.py: from . import command
  3) Create a function, describe its name and command
  4) in __init__.py add to list modules <module_name>
  5) to import main models
  6) data = modules.load()

Result:
  - data['commands'] - a list of teams with their names
  - data['errors'] - a list of modules in which an import error occurred

Example:
File main.py
```python3
import importlib
modules = importlib.import_module('modules')
```

File modules/\_\_init\_\_.py:
```python3
modules = [
    'admins',
]

......
```
File modules/admins.py
```python3
from . import command

@command(name="Hello, world", command="hello")
def hello_world(*data, **kwargs):
    print("Hello, world")
```
