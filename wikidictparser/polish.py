from .base import WiktionaryParserBase


class PlWiktionaryParser(WiktionaryParserBase):
    """Polish Wiktionary Parser class

    This class is used to parse polish wiktionary.

    """

    def __init__(self):
        url = "https://pl.wiktionary.org/wiki/{}?printable=yes"
        super().__init__(url)