# -*- coding: utf-8 -*-

from .context import wikidictparser as wdp

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_key_error(self):
        self.assertRaises(KeyError, wdp.get_parser, *['five'])
        self.assertRaises(KeyError, wdp.get_parser, *[None])

    def test_polish_keys(self):
        for language in ['wikislownik', 'wikisłownik', 'pl', 'plwiki', 'polish', 'plwiktionary']:
            parser = wdp.get_parser(language)
            self.assertIsInstance(parser, (wdp.polish.PlWiktionaryParser, wdp.base.WiktionaryParserBase))
            self.assertEqual(parser.url, "https://pl.wiktionary.org/wiki/{}?printable=yes")

    def test_english_keys(self):
        for language in ['wiktionary', 'en', 'enwiki', 'english', 'enwiktionary']:
            parser = wdp.get_parser(language)
            self.assertIsInstance(parser, (wdp.english.EnWiktionaryParser, wdp.base.WiktionaryParserBase))
            self.assertEqual(parser.url, "https://en.wiktionary.org/wiki/{}?printable=yes")


if __name__ == '__main__':
    unittest.main()