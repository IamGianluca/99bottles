import pytest
from bottles.bottles import (
    BottleNumber,
    BottleNumber0,
    BottleNumber1,
    BottleNumber6,
    BottleVerse,
    CountdownSong,
)


@pytest.mark.parametrize("number", [99, 8, 5, 3])
def test_verse_general_rule_upper_and_lower_bound(number: int) -> None:
    expected = (
        f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
        f"Take one down and pass it around, {number-1} bottles of beer on the wall.\n"
    )
    assert BottleVerse.lyrics(number) == expected


def test_verse_seven() -> None:
    expected = (
        "7 bottles of beer on the wall, 7 bottles of beer.\n"
        "Take one down and pass it around, 1 six-pack of beer on the wall.\n"
    )
    assert BottleVerse.lyrics(7) == expected


def test_verse_six() -> None:
    expected = (
        "1 six-pack of beer on the wall, 1 six-pack of beer.\n"
        "Take one down and pass it around, 5 bottles of beer on the wall.\n"
    )
    assert BottleVerse.lyrics(6) == expected


def test_verse_two() -> None:
    expected = (
        "2 bottles of beer on the wall, 2 bottles of beer.\n"
        "Take one down and pass it around, 1 bottle of beer on the wall.\n"
    )
    assert BottleVerse.lyrics(2) == expected


def test_verse_one() -> None:
    expected = (
        "1 bottle of beer on the wall, 1 bottle of beer.\n"
        "Take it down and pass it around, no more bottles of beer on the wall.\n"
    )
    assert BottleVerse.lyrics(1) == expected


def test_verse_zero() -> None:
    expected = (
        "No more bottles of beer on the wall, no more bottles of beer.\n"
        "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
    )
    assert BottleVerse.lyrics(0) == expected


class VerseFake:
    @staticmethod
    def lyrics(number: int) -> str:
        return f"This is verse {number}."


def test_verse() -> None:
    expected = "This is verse 500."
    assert CountdownSong(VerseFake, min_=0, max_=1_000).verse(500) == expected


def test_verses() -> None:
    expected = "This is verse 99." "\n" "This is verse 98."
    assert (
        CountdownSong(VerseFake, min_=10, max_=100).verses(99, 98) == expected
    )


def test_song() -> None:
    expected = (
        "This is verse 47.\n"
        "This is verse 46.\n"
        "This is verse 45.\n"
        "This is verse 44.\n"
        "This is verse 43."
    )
    assert CountdownSong(VerseFake, min_=43, max_=47).song() == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        (0, BottleNumber0),
        (1, BottleNumber1),
        (6, BottleNumber6),
        (3, BottleNumber),
        (7, BottleNumber),
        (43, BottleNumber),
    ],
)
def test_bottlenumber_factory(number, expected) -> None:
    assert isinstance(BottleNumber.get(number), expected)
