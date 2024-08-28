# Small Integer Caching

In python, integers (like everything else) are represented internally as objects.
Whenever you do something that creates an integer, Python makes a new object for the integer.
This takes a small amount of time,
so as a small speed optimization python pre-creates the small integers; instead of creating these on the fly every time,
it just gives you a new reference to the premade one.

The standard small integers that get cached are -5 to 256 (inclusive):

```python
x = 125
x is 125
>>> True

y = -3
y is -3
>>> True

z = 257
z is 257
>>> False

z == 257
>>> True
```
This isn't the kind of thing you should rely on, but it's illustrative of what's going on behind the scenes


## Caveats
- This is only true on CPython I think (which is the normal version that you're probably using)
I think python can choose to cache other objects, but I'm not sure when this would happen
- This doesn't matter, but it is kind of fun

