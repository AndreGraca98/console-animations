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
        display_chars: list[str] | None = None,
        internal_timer: float | None = None,
        raise_stop_iteration: bool = False,
    ):
        """max_iterations: max number of iterations to display.
        Defaults to -1 (infinite)
        display_chars: list of characters to display in a loop. Defaults to clock emojis
        internal_timer: time to wait between each iteration. Defaults to None (no wait)
        raise_stop_iteration: if True, raise StopIteration when the animation finishes.
        Defaults to False
        """
        self.reset()

        self._validate(
            max_iterations, display_chars, internal_timer, raise_stop_iteration
        )
        self.max_iterations: int = max_iterations or self.DEFAULT_MAX_ITERATIONS
        self.display_chars: list[str] = display_chars or self.DEFAULT_DISPLAY_CHARS
        self.internal_timer: float | None = internal_timer
        self.raise_stop_iteration: bool = raise_stop_iteration

        if self.internal_timer is not None:
            tt = self.internal_timer * len(self.display_chars) * self.max_iterations
            _logger.debug(f"Animation cycle total waiting time: {tt} seconds")

    def run(self) -> None:
        """Run the animation until it finishes"""
        # TODO: add try/except for ctrl+C (KeyboardInterrupt) to exit animation (?)
        while not self.finished:
            self.display()
        self.reset()

    def reset(self) -> None:
        """Reset the animation to the initial state"""
        self._element: int = -1
        self._current_iteration: int = 0

    def display(self) -> None:
        """Display the next character in the animation. If internal_timer is set,
        wait for that time before displaying the next character"""
        if self.internal_timer is not None:
            time.sleep(self.internal_timer)
        print(f"{next(self): <80}", end="\r")

    @property
    def finished(self) -> bool:
        """Returns True if the animation has finished"""
        if self.max_iterations == -1:
            # Infinite iterations
            return False
        return self._current_iteration >= self.max_iterations

    def _validate(
        self,
        max_iterations: int | None,
        display_chars: list[str] | None,
        internal_timer: float | None,
        raise_stop_iteration: bool,
    ):
        if max_iterations is not None:
            assert isinstance(max_iterations, int)
            assert max_iterations == -1 or max_iterations > 0
        if display_chars is not None:
            assert isinstance(display_chars, list)
            assert all(isinstance(c, str) for c in display_chars)
            assert len(display_chars) >= 1
        if internal_timer is not None:
            assert isinstance(internal_timer, (int, float))
            assert internal_timer > 0
        assert isinstance(raise_stop_iteration, bool)

    def __next__(self) -> str:
        self._element += 1
        if self._element >= len(self.display_chars):
            # Reset to first element
            self._element = 0
            self._current_iteration += 1
        if self.finished and self.raise_stop_iteration:
            raise StopIteration
        return self.display_chars[self._element]

    def __iter__(self) -> Self:
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        ...

    def __repr__(self):
        t = self.__class__.__name__
        t += f"(max_iterations={self.max_iterations}, "
        t += f"display_chars={self.display_chars!r}, "
        if self.internal_timer is not None:
            t += f"internal_timer={self.internal_timer}, "
        t += f"raise_on_finish={self.raise_stop_iteration})"
        return t
