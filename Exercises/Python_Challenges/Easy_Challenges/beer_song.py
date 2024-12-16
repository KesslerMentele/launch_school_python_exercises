

class BeerSong:

    PLURAL_VERSE = (
        "CURRENT bottles of beer on the wall, CURRENT bottles of beer.\n"
            "Take one down and pass it around, NEXT bottles of beer on the "
        "wall.\n"
    )
    DOUBLE_VERSE = ("2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, 1 bottle of beer on the wall.\n")

    SINGLE_VERSE = ("1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, no more bottles of beer on the wall.\n")

    ZERO_VERSE = ("No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, 99 bottles of beer on the wall.\n")

    @staticmethod
    def verses(from_verse, to_verse)->str:
        verses = []
        for verse_number in range(from_verse, to_verse -1, -1):
            verses.append(BeerSong.verse(verse_number))
        return '\n'.join(verses)


    @staticmethod
    def verse(verse_number)->str:
        if verse_number == 0:
            return BeerSong.ZERO_VERSE
        elif verse_number == 1:
            return BeerSong.SINGLE_VERSE
        elif verse_number == 2:
            return BeerSong.DOUBLE_VERSE
        else:
            return BeerSong.PLURAL_VERSE.replace('CURRENT', str(verse_number)).replace('NEXT', str(verse_number - 1))

    @staticmethod
    def lyrics()->str:
        return BeerSong.verses(99,0)

