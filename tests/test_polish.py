# -*- coding: utf-8 -*-

from .context import wikidictparser as wdp

import unittest


class PolishParserTestSuite(unittest.TestCase):
    """Basic test cases."""

    parser = wdp.get_parser('pl')
    words_to_check = ['to', 'tamto', 'można', 'drzewo', 'słowo']

    def test_not_found(self):
        self.assertIsNone(self.parser.fetch('abfk'))
        self.assertIsNone(self.parser.fetch('This is not a word'))

    def test_word_to_language_sections_dict(self):
        self.parser.fetch('to')
        self.assertTrue('pl' in self.parser.language_section_dict.keys())
        self.assertTrue('en' in self.parser.language_section_dict.keys())
        self.assertFalse('_' in self.parser.language_section_dict.keys())

    def test_words_subsection_dict(self):
        for word in self.words_to_check:
            self.parser.fetch(word)
            subsection_dict = self.parser.language_section_dict['pl']
            self.assertTrue(list(subsection_dict.keys())[0] == 'heading')
            self.assertTrue('znaczenia' in subsection_dict.keys())

    def test_adjective_declination(self):
        self.parser.fetch('mądry')
        declination_dict =\
            self.parser.language_section_dict['pl']['odmiana'][1][1]
        self.assertTrue('liczba pojedyncza n' in declination_dict['mianownik'].keys())
    
    def test_verb_declination(self):
        self.parser.fetch('widzieć')
        declination_dict =\
            self.parser.language_section_dict['pl']['odmiana'][1][1]
        self.assertTrue('liczba pojedyncza 1. os.' in declination_dict['bezokolicznik'].keys())


if __name__ == '__main__':
    unittest.main()
