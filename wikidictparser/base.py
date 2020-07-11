# -*- coding: utf-8 -*-
import re, requests
from bs4 import BeautifulSoup
from copy import copy

class WiktionaryParserBase(object):
    """Base Wiktionary Parser class
    
    This class handles connections and contains placeholder functions
    to be override by language specific parsers.
    """

    def __init__(self, url):
        self.url = url
        self.soup = None
        self.session = requests.Session()
        self.session.mount("http://", requests.adapters.HTTPAdapter(max_retries = 2))
        self.session.mount("https://", requests.adapters.HTTPAdapter(max_retries = 2))
