class Bottle:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, number: int) -> str:
        bn = BottleNumber(number)
        bns = BottleNumber(bn.successor())
        return (
            f"{bn.quantity().capitalize()} {bn.container()} of beer on the wall, {bn.quantity()} {bn.container()} of beer.\n"
            f"{bn.action()}, {bns.quantity()} {bns.container()} of beer on the wall.\n"
        )


class BottleNumber:
    def __init__(self, number: int) -> None:
        self.number = number

    def container(self) -> str:
        if self.number == 1:
            return "bottle"
        else:
            return "bottles"

    def pronoun(self) -> str:
        if self.number == 1:
            return "it"
        else:
            return "one"

    def quantity(self) -> str:
        if self.number == 0:
            return "no more"
        else:
            return str(self.number)

    def action(self) -> str:
        if self.number == 0:
            return "Go to the store and buy some more"
        else:
            return f"Take {self.pronoun()} down and pass it around"

    def successor(self) -> int:
        if self.number == 0:
            return 99
        else:
            return self.number - 1
