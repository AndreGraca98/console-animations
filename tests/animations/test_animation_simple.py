import time

import pytest

from animations.animation_simple import SimpleAnimation


def test_init():
    # Test default values
    animation = SimpleAnimation()
    assert animation.max_iterations == 1
    assert animation.chars == [
        "🕐",
        "🕑",
        "🕒",
        "🕓",
        "🕔",
        "🕕",
        "🕖",
        "🕗",
        "🕘",
        "🕙",
        "🕚",
        "🕛",
    ]
    assert animation.wait_time is None

    # Test custom values
    animation = SimpleAnimation(
        max_iterations=3,
        chars=["🐶", "🐱"],
        wait_time=0.5,
    )
    assert animation.max_iterations == 3
    assert animation.chars == ["🐶", "🐱"]
    assert animation.wait_time == 0.5


def test_reset():
    animation = SimpleAnimation(
        max_iterations=3,
        chars=["🐶", "🐱"],
        wait_time=0.5,
    )
    animation._element = 5
    animation._current_iteration = 2
    animation.reset()
    assert animation._element == 0
    assert animation._current_iteration == 0


def test_finished():
    # Test with finite iterations
    animation = SimpleAnimation(max_iterations=3)
    assert not animation.finished
    animation._current_iteration = 3
    assert animation.finished

    # Test with infinite iterations
    animation = SimpleAnimation(max_iterations=-1)
    assert not animation.finished


def test_display():
    # Test without internal timer
    animation = SimpleAnimation(chars=["🐶", "🐱"])
    assert next(animation) == "🐶"
    assert next(animation) == "🐱"
    assert next(animation) == "🐶"
    assert next(animation) == "🐱"
    assert next(animation) == "🐶"
    assert next(animation) == "🐱"

    # Test with internal timer
    animation = SimpleAnimation(chars=["🐶", "🐱"], wait_time=0.5)

    start = time.time()
    while not animation.finished:
        animation.display()
    end = time.time()

    tolerance = 0.1
    assert abs(end - start) - tolerance < (2 * 0.5 * 1)


def test_iterator():
    animation = SimpleAnimation(chars=["🐶", "🐱"])
    assert list(animation) == ["🐶", "🐱"]


def test_repr():
    animation = SimpleAnimation(
        max_iterations=3,
        chars=["🐶", "🐱"],
    )
    assert (
        repr(animation) == "SimpleAnimation(max_iterations=3, display_chars=['🐶', '🐱'])"
    )

    animation = SimpleAnimation(
        max_iterations=3,
        chars=["🐶", "🐱"],
        wait_time=0.5,
    )
    assert (
        repr(animation) == "SimpleAnimation(max_iterations=3, "
        "display_chars=['🐶', '🐱'], internal_timer=0.5)"
    )
