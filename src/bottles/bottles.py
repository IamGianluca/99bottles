from typing import List


class Bottle:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, number: int) -> str:
        bn = BottleNumberFactory.get(number)
        return (
            f"{bn.to_str().capitalize()} of beer on the wall, {bn.to_str()} of beer.\n"
            f"{bn.action()}, {bn.successor().to_str()} of beer on the wall.\n"
        )


class BottleNumber:
    def __init__(self, number: int) -> None:
        self.number = number

    @classmethod
    def register(self, factory):
        factory.add(self)

    @staticmethod
    def can_handle(number: int) -> bool:
        return True

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
        return BottleNumberFactory.get(self.number - 1)


class BottleNumber0(BottleNumber):
    @staticmethod
    def can_handle(number: int) -> bool:
        return number == 0

    def quantity(self) -> str:
        return "no more"

    def action(self) -> str:
        return "Go to the store and buy some more"

    def successor(self) -> int:
        return BottleNumberFactory.get(99)


class BottleNumber1(BottleNumber):
    @staticmethod
    def can_handle(number: int) -> bool:
        return number == 1

    def container(self) -> str:
        return "bottle"

    def pronoun(self) -> str:
        return "it"


class BottleNumber6(BottleNumber):
    @staticmethod
    def can_handle(number: int) -> bool:
        return number == 6

    def quantity(self) -> str:
        return "1"

    def container(self) -> str:
        return "six-pack"


class BottleNumberFactory:
    registry: List = []

    @classmethod
    def add(cls, item: BottleNumber):
        cls.registry.append(item)

    @classmethod
    def get(cls, number: int):
        """BottleNumber factory."""
        bottle_number_class = [
            bn for bn in cls.registry if bn.can_handle(number)
        ]
        return bottle_number_class[0](number)


# register all BottleNumbers
for cls in BottleNumber.__subclasses__():
    print(cls)
    cls.register(BottleNumberFactory)
BottleNumber.register(BottleNumberFactory)
