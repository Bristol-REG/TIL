# Doing nothing with `pass` and `Ellipsis`

In python, you can do nothing by typing `pass` - people also use `...` (`Ellipsis`), but this is also used in other places.
 
For ignoring exceptions:

```python
try:
    f(x)
except ValueError:
    pass
```
 
For writing skeleton code (to me, `pass` looks like it's intended to be empty, `...` looks like it will be filled in later).

```python
def my_fcn():
    ...
```

You can put anything in place of the `...` here though, so people often just write a docstring:

```python
def my_fcn():
   """
   Do some things and stuff
   """
```

Via: [Richard](https://github.com/richard-lane)

## Postscript

For skeleton code you could also do:

```python
def my_fcn():
    raise NotImplementedError
```

or:

```python
def my_fcn():
    return NotImplemented
```

(these do different things)
