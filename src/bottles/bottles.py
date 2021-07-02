class Bottle:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, number: int) -> str:
        return (
            f"{self.quantity(number).capitalize()} {self.container(number)} of beer on the wall, {self.quantity(number)} {self.container(number)} of beer.\n"
            f"{self.action(number)}, {self.quantity(self.successor(number))} {self.container(number-1)} of beer on the wall.\n"
        )

    def container(self, number: int) -> str:
        if number == 1:
            return "bottle"
        else:
            return "bottles"

    def pronoun(self, number: int) -> str:
        if number == 1:
            return "it"
        else:
            return "one"

    def quantity(self, number: int) -> str:
        if number == 0:
            return "no more"
        else:
            return str(number)

    def action(self, number: int) -> str:
        if number == 0:
            return "Go to the store and buy some more"
        else:
            return f"Take {self.pronoun(number)} down and pass it around"

    def successor(self, number: int) -> int:
        if number == 0:
            return 99
        else:
            return number - 1
