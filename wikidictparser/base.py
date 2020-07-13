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

    def clean_html(self):
        unwanted_classes = ['sister-wikipedia', 'thumb', 'reference', 'cited-source']
        for tag in self.soup.find_all(True, {'class': unwanted_classes}):
            tag.extract()

    def fetch(self, word):
        """Fetch function

        This function fetches the data about a given word.

        """

        self.response = self.session.get(self.url.format(word))
        self.soup = BeautifulSoup(self.response.text.replace('>\n<', '><'), 'html.parser')
        self.current_word = word
        self.clean_html()
        return self.get_word_data()

    
    def get_word_data(self):
        """ placeholder function
        """
        print("Placeholder function")
        return {}