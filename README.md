# Waiting Animations

![badge](https://img.shields.io/github/v/tag/AndreGraca98/console-animations?logo=python&logoColor=yellow&label=version)

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
- `chars`: list of characters to display in a loop. Defaults to clock emojis
- `wait_time`: time to wait between each iteration. Defaults to None (no wait)

For more information, see the [SimpleAnimation README](./animations/readme_animation_simple.md).
