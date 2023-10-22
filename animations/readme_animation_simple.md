# Simple Animation

A Python class that creates a waiting animation. The animation consists of a loop of characters that are displayed on the console. The animation can be customized by changing the number of iterations, the characters to display, and the time to wait between each iteration.

## Example

```python
from animations import SimpleAnimation
import time

chars:list[str] = "🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘 ".split()

animation = SimpleAnimation(display_chars=chars, internal_timer=0.25)
animation.run()
```

```python
animation = SimpleAnimation(display_chars=chars, raise_stop_iteration=True)
for char in animation:
    print(char, end="\r")
    time.sleep(0.25)
animation.reset()
```

```python
animation = SimpleAnimation(display_chars=chars, internal_timer=0.25)
while not animation.finished:
    animation.display()
animation.reset()
```

This will display each moon phase during .25 seconds one time.

### Some other cool waiting animations

```python
chars = ["◌","○","◎","◍","◉","●","◉","◍","◎","○" ]
```

```python
chars = ["|", "/", "-", "\\"]
```

```python
chars = ["▖", "▘", "▝", "▗"]
```

```python
chars = ["▁", "▃", "▄", "▅", "▆", "▇", "█", "▇", "▆", "▅", "▄", "▃"]
```

```python
chars=["░","▒","▓","▒"]
```

```python
chars = ['⠾', '⠽', '⠻', '⠟', '⠯', '⠷']
```

```python
chars = ['⡀', '⡠', '⡢', '⡪', '⡫', '⡻', '⡿', '⣿', '⣿', '⣿']
```

```python
chars = ["◐", "◓", "◑", "◒"]
```

```python
chars=["🌍", "🌎", "🌏"]
```

```python
chars=["⏳", "⌛"]
```

```python
chars=["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
```

## Help

### `__init__()`

The constructor method that initializes the animation with the specified settings. It takes four optional parameters:

- `max_iterations`: The maximum number of times to display the animation. Default is `1`, which means it will loop once. -1 means it runs until manually stopped.
- `display_chars`: A list of characters to display in the animation loop. Default is a list of clock emojis.
- `internal_timer`: The duration to wait between each iteration of the animation loop. Default is `None`, which means no wait time.
- `raise_stop_iteration`: A boolean that indicates whether to raise a `StopIteration` exception when the animation finishes. Default is `False`.

### `run()`

Runs the animation loop until it reaches its maximum number of iterations. It uses a `while` loop to display the animation until it completes.

### `display()`

Displays the next character in the animation loop. If the `internal_timer` is set, it will wait for that duration before displaying the next character.

### `finished`

A read-only property that returns `True` if the animation has finished its maximum number of iterations. If the maximum number of iterations is `None`, which means infinite, this property will always return `False`.

### `reset()`

Resets the animation to its initial state. It sets the internal state back to the starting position, so you can start the animation over again.

### `__next__()`

Returns the next character in the animation loop. This method is used to iterate over the animation's characters one-by-one.

### `__iter__()`

Returns an iterator for the animation. This method is used to make the animation loop iterable, so you can use it in a `for` loop.
