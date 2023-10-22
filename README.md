# Waiting Animations

A collection of Python classes to create waiting animations on the console.

## Install

```bash
pip install git+https://github.com/AndreGraca98/console-animations.git
```

## Animations

### Simple Animation

The `SimpleAnimation` class creates a loop of characters that are displayed on the console. The animation is customizable by changing the number of iterations, the characters to display, and the time to wait between each iteration.

Parameters:

- `max_iterations`: max number of iterations to display. Defaults to 1 (-1 means infinite)
- `display_chars`: list of characters to display in a loop. Defaults to clock emojis
- `internal_timer`: time to wait between each iteration. Defaults to None (no wait)
- `raise_stop_iteration`: if True, raise StopIteration when the animation finishes. Defaults to False

For more information, see the [SimpleAnimation README](./animations/readme_animation_simple.md).
