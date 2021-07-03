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
    def __init__(self, bottle_number) -> None:
        pass

    @staticmethod
    def lyrics(number: int) -> str:
        pass

    def _lyrics(self) -> str:
        pass


class BottleVerse:
    def __init__(self, bottle_number) -> None:
        self.bottle_number = bottle_number

    @staticmethod
    def lyrics(number: int):
        return BottleVerse(BottleNumber.get(number))._lyrics()

    def _lyrics(self) -> str:
        return (
            f"{self.bottle_number.to_str().capitalize()} of beer on the wall, {self.bottle_number.to_str()} of beer.\n"
            f"{self.bottle_number.action()}, {self.bottle_number.successor().to_str()} of beer on the wall.\n"
        )


class Bottle:
    def __init__(
        self, verse_template: Type[VerseTemplate] = BottleVerse
    ) -> None:
        self.verse_template = verse_template

    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, number: int) -> str:
        return self.verse_template.lyrics(number)
