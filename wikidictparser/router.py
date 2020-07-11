# -*- coding: utf-8 -*-
import traceback
import sys


from .english import EnWiktionaryParser
from .polish import PlWiktionaryParser

parser_routing_dict = {
    # english
    'wiktionary' : EnWiktionaryParser,
    'en': EnWiktionaryParser,
    'english': EnWiktionaryParser,
    'enwiki': EnWiktionaryParser,
    'enwiktionary': EnWiktionaryParser,
    # polish
    'wikislownik': PlWiktionaryParser,
    'wikisłownik': PlWiktionaryParser,
    'pl': PlWiktionaryParser,
    'polish': PlWiktionaryParser,
    'plwiki': PlWiktionaryParser,
    'plwiktionary': PlWiktionaryParser,
}

def get_parser(language):
    """get parser function

    This function routes the user to appriopriate parser.

    Inputs:

        - language (str) - string specyfying which wikitionary to use

    Possible language values:

        - wiktionary | en | english | enwiki | enwiktionary
            - english wiktionary parser

        - wikisłownik | wikislownik | pl | polish | plwiki | plwiktionary 
            - polish wiktionary parser
    """
    
    if not language in parser_routing_dict.keys():
        raise KeyError(f'"{language}" is not a valid option for parser language.')
    
    return parser_routing_dict[language]()
    

