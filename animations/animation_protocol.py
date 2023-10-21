from typing import Protocol, Self


class AnimationProtocol(Protocol):
    DEFAULT_MAX_ITERATIONS: int
    DEFAULT_DISPLAY_CHARS: list[str]

    def run(self) -> None:
        ...

    def reset(self) -> None:
        ...

    def display(self) -> None:
        ...

    @property
    def finished(self) -> bool:
        ...

    def __next__(self) -> str:
        ...

    def __iter__(self) -> Self:
        ...
