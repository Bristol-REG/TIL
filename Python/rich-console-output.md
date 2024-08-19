# Rich console output, pretty printing and formatting

If you want your script's console output to have colours and other formatting, check out [Rich](https://github.com/Textualize/rich).

See also: A [video introduction to Rich](https://calmcode.io/rich/introduction.html) by calmcode.

## Basic printing

You can easily add colours, emojis and other formatting with basic tags using an [improved version of `print()`](https://github.com/Textualize/rich#rich-print):

```python
from rich import print

print("Hello, [bold magenta]World[/bold magenta]! :vampire:")
```

Any variables you print also get nicer formatting and colour syntax highlighting.

## Inspecting objects

If you have an object with multiple attributes and methods, you can a nice overview of everything using [`rich.inspect()`](https://github.com/Textualize/rich#rich-inspect). I've used this quite a bit.

```python
from rich import inspect

my_list = ["foo", "bar"]
inspect(my_list, methods=True)
```

## Example

Via the [Rich GitHub repo](https://github.com/Textualize/rich):

![Example console output printed by `python -m rich`](https://raw.githubusercontent.com/textualize/rich/master/imgs/features.png)
