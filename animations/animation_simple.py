import logging
import time
from typing import Self

__all__ = ["SimpleAnimation"]

_logger = logging.getLogger(__name__)


class SimpleAnimation:
    """
    A simple animation class that displays a list of characters in a loop.
    It can be used to display a loading animation"""

    DEFAULT_MAX_ITERATIONS: int = 1
    DEFAULT_DISPLAY_CHARS = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]

    def __init__(
        self,
        max_iterations: int | None = None,
        chars: list[str] | None = None,
        wait_time: float | None = None,
    ):
        """max_iterations: max number of iterations to display.
        Defaults to -1 (infinite)
        chars: list of characters to display in a loop. Defaults to clock emojis
        wait_time: time to wait between each iteration. Defaults to None (no wait)
        """
        self.reset()

        self._validate(max_iterations=max_iterations, chars=chars, wait_time=wait_time)
        self.max_iterations: int = max_iterations or self.DEFAULT_MAX_ITERATIONS
        self.chars: list[str] = chars or self.DEFAULT_DISPLAY_CHARS
        self.wait_time: float | None = wait_time

        if self.wait_time is not None:
            tt = self.wait_time * len(self.chars) * self.max_iterations
            _logger.debug(f"Animation cycle total waiting time: {tt} seconds")

    def _validate(
        self,
        max_iterations: int | None,
        chars: list[str] | None,
        wait_time: float | None,
    ):
        if max_iterations is not None:
            assert isinstance(max_iterations, int)
            assert max_iterations == -1 or max_iterations > 0
        if chars is not None:
            assert isinstance(chars, list)
            assert all(isinstance(c, str) for c in chars)
            assert len(chars) >= 1
        if wait_time is not None:
            assert isinstance(wait_time, (int, float))
            assert wait_time > 0

    @property
    def finished(self) -> bool:
        """Returns True if the animation has finished"""
        if self.max_iterations == -1:
            # Infinite iterations
            return False
        return self._current_iteration >= self.max_iterations

    def run(self, pre_text: str = "", post_text: str = "") -> None:
        """Run the animation until it finishes"""
        # TODO: add try/except for ctrl+C (KeyboardInterrupt) to exit animation (?)
        self.reset()
        while not self.finished:
            self.display(pre_text=pre_text, post_text=post_text)
        self.reset()

    def display(self, pre_text: str = "", post_text: str = "") -> None:
        """Display the next character in the animation. If internal_timer is set,
        wait for that time before displaying the next character"""
        if self.wait_time is not None:
            time.sleep(self.wait_time)
        print("\033[?25l", end="")  # Hide cursor
        print(f"{pre_text}{next(self)}{post_text}", end="\r")
        print("\033[?25h", end="")  # Show cursor

    def reset(self) -> None:
        """Reset the animation to the initial state"""
        self._element: int = 0
        self._current_iteration: int = 0

    # Use 'next()'
    def __next__(self):
        current_element = self._element
        self._element += 1
        if self._element >= len(self.chars):
            # Reset to first element
            self._element = 0
            self._current_iteration += 1
        return self.chars[current_element]

    # Use 'for' loops, iterable constructors...
    def __iter__(self):
        yield from self.chars

    # Use 'with' statements
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        ...

    def __repr__(self):
        t = self.__class__.__name__
        t += f"(max_iterations={self.max_iterations}, "
        t += f"display_chars={self.chars!r}"
        if self.wait_time is not None:
            t += f", internal_timer={self.wait_time}"
        t += ")"
        return t
