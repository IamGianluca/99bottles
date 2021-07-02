class Bottle:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, number: int) -> str:
        bn = BottleNumber.get(number)
        return (
            f"{bn.to_str().capitalize()} of beer on the wall, {bn.to_str()} of beer.\n"
            f"{bn.action()}, {bn.successor().to_str()} of beer on the wall.\n"
        )


class BottleNumber:
    def __init__(self, number: int) -> None:
        self.number = number

    @staticmethod
    def get(number: int):
        """BottleNumber factory."""
        try:
            return eval(f"BottleNumber{number}")(number)
        except NameError as e:
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
