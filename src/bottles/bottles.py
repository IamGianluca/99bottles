from typing import Protocol, Type


class BottleNumber:
    def __init__(self, number: int) -> None:
        self.number = number

    @staticmethod
    def get(number: int):
        """BottleNumber factory."""
        if number == 0:
            return BottleNumber0(number)
        elif number == 1:
            return BottleNumber1(number)
        elif number == 6:
            return BottleNumber6(number)
        else:
            return BottleNumber(number)

    def to_str(self) -> str:
        return " ".join([self.quantity(), self.container()])

    def container(self) -> str:
        return "bottles"

    def pronoun(self) -> str:
        return "one"

    def quantity(self) -> str:
        return str(self.number)

    def action(self) -> str:
        return f"Take {self.pronoun()} down and pass it around"

    def successor(self) -> int:
        return self.get(self.number - 1)


class BottleNumber0(BottleNumber):
    def quantity(self) -> str:
        return "no more"

    def action(self) -> str:
        return "Go to the store and buy some more"

    def successor(self) -> int:
        return self.get(99)


class BottleNumber1(BottleNumber):
    def container(self) -> str:
        return "bottle"

    def pronoun(self) -> str:
        return "it"


class BottleNumber6(BottleNumber):
    def quantity(self) -> str:
        return "1"

    def container(self) -> str:
        return "six-pack"


class VerseTemplate(Protocol):
    @staticmethod
    def lyrics(number: int) -> str:
        pass


class BottleVerse:
    def __init__(self, number) -> None:
        self.number = number

    @staticmethod
    def lyrics(number: int):
        return BottleVerse(BottleNumber.get(number))._lyrics()

    def _lyrics(self) -> str:
        return (
            f"{self.number.to_str().capitalize()} of beer on the wall, {self.number.to_str()} of beer.\n"
            f"{self.number.action()}, {self.number.successor().to_str()} of beer on the wall.\n"
        )


class CountdownSong:
    def __init__(
        self,
        verse_template: Type[VerseTemplate],
        max_: int = 999_999,
        min_: int = 0,
    ) -> None:
        self.verse_template = verse_template
        self.min_ = min_
        self.max_ = max_

    def song(self) -> str:
        return self.verses(self.max_, self.min_)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, number: int) -> str:
        return self.verse_template.lyrics(number)
