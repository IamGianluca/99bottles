class Bottle:
    def song(self) -> str:
        return self.verses(99, 0)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(
            [self.verse(i) for i in reversed(range(lower, upper + 1))]
        )

    def verse(self, number: int) -> str:
        if number == 0:
            return (
                "No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
            )
        if number == 1:
            return (
                "1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, no more bottles of beer on the wall.\n"
            )
        if number == 2:
            return (
                "2 bottles of beer on the wall, 2 bottles of beer.\n"
                "Take one down and pass it around, 1 bottle of beer on the wall.\n"
            )
        else:
            return (
                f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
                f"Take one down and pass it around, {number-1} bottles of beer on the wall.\n"
            )
