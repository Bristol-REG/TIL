# Progress bars for long-running loops or tasks

If you have a loop that has a number of iterations or takes a long time to run, you can get an easy progress bar (with an estimated time to completion) using tools like [tqdm](https://tqdm.github.io/) or [Rich](https://rich.readthedocs.io/en/latest/progress.html). They also work in Jupyter notebooks.

## tqdm

Change your loop from:

```python
for i in range(10000):
    ...
```

to:

```python
from tqdm import tqdm
for i in tqdm(range(10000)):
    ...
```

And get this for free:

```
76%|████████████████████████████         | 7568/10000 [00:33<00:10, 229.00it/s]
```

You can also manually update the progress bar in your code using [`tqdm.update()`](https://tqdm.github.io/docs/tqdm/#update).

## Rich

Rich works in a similar way, and also provides [rich console output](rich-console-output.md) more generally.
