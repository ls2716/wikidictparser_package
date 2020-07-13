from .base import WiktionaryParserBase
import logging
import bs4

class PlWiktionaryParser(WiktionaryParserBase):
    """Polish Wiktionary Parser class

    This class is used to parse polish wiktionary.

    """

    def __init__(self):
        url = "https://pl.wiktionary.org/wiki/{}?printable=yes"
        self.language_of_interest = 'pl'
        super().__init__(url)
    

    def get_word_data(self):
        """Get word data function

        This function gets the data about the word and outputs a json file.
        """
        # get a list of tags inside main content of the page
        self.content_tag_list = self.soup.find('div', {'class': 'mw-parser-output'})
        # return None if the word could not be found
        if not self.content_tag_list:
            logging.info(f'The data about the word "{ self.current_word }" could not be found.')
            return None
        # get dictionary with language sections 
        self.language_section_dict = self.get_language_section_dict()
        # divide the language section into dictionary with subsection names as keys
        self.divide_subsections()
        self.parse_meanings()

        return {}

    def get_language_section_dict(self):
        """Get language section function

        This function divides the main contents of the page
        into dictionary where the keys are language codes
        (e.g. 'pl', 'en') and the values are the list of tags
        corresonding to that language.

        Returns:

            - language_section_dict (dict) - dictionary with language sections

        """
        contents = self.content_tag_list.contents
        # create the dict and set initial key for first sections to be omitted
        language_section_dict = {'_': []}
        i = 0
        last_lang = '_'
        # iterate through tags
        for tag in contents:
            tag_name = tag.name
            # if the tag is language tag then set default dict key to language code
            if tag_name=='h2':
                last_lang = tag.select('span.lang-code.primary-lang-code')[0].attrs['id']
                # logging.debug(f'Found language "{last_lang}".')
                language_section_dict[last_lang] = []
            # append the tag to list for the given language if element is a Tag
            if isinstance(tag, bs4.element.Tag):
                language_section_dict[last_lang].append(tag)
        # delete the initial tags
        del language_section_dict['_']
        return language_section_dict

    def divide_subsections(self):
        """ Divide subsections function

        This function divides the languages sections
        into subsections depending on the heading.
        """
        # for every language section
        for lang in self.language_section_dict.keys():
            # create a dict for subsection name and corresponding tag list
            subsection_dict = {}
            subsections = self.language_section_dict[lang]
            # starts with heading subsection
            subsection_name = 'heading'
            subsection_dict[subsection_name] = []
            for tag in subsections:
                # span.field-title elements contain subsection names
                if tag.select('span.field-title'):
                    # text content is <subsection_name>: so last char is skipped
                    subsection_name = tag.select('span.field-title')[0].text[:-1]
                    # logging.debug(f'Found subsection "{subsection_name}".')
                    # list for new subsection is created
                    subsection_dict[subsection_name] = []
                # tag is being appended to last subsection
                subsection_dict[subsection_name].append(tag)
            # language sections dict will contan subsection dicts
            self.language_section_dict[lang] = subsection_dict

    

    def parse_meanings(self):
        """ parse meanings function

        This function parsers the meanings subsection
        (marked with key "znaczenia".)
        """
        # for every language section
        for lang in self.language_section_dict.keys():
            meaning_tags = self.language_section_dict[lang]['znaczenia']
            major = 0
            minor = 0
            part_of_speech = None
            meanings = []
            logging.debug(f'Language {lang}.')
            # for every tag in meaning subsection
            for tag in meaning_tags:
                logging.debug(f'Tag {tag}')
                # if part of speech tag then parse
                if tag.select('p > i'):
                    major = major + 1
                    minor = 0
                    part_of_speech = tag.select('p > i')[0].text
                    logging.debug(f'Major {major}, part of speect {part_of_speech}.')
                # if meaning then parse meaning
                elif tag.select('span.field-title'):
                    logging.debug(f'Found tag {tag}')
                    pass
                elif tag.select('dl > dd'):
                    try:
                        for meaning in tag.select('dl > dd'):
                            minor = minor + 1
                            meaning_text = meaning.text
                            number = meaning_text.split(' ')[0]
                            meaning_text = meaning_text[len(number):]
                            logging.debug(f'Minor {minor}, number {number}, meaning: {meaning_text}.')
                            # check if numbering is correct - if not raise Exception
                            if f'({major}.{minor})'!=number:
                                raise Exception(f'The numbering for meaning {meaning} is inconsistent.')
                            meanings.append((major, minor, part_of_speech, meaning_text))
                    except:
                        logging.debug(f'Failed to parse tag {tag}.')
                    
                    
            self.language_section_dict[lang]['znaczenia'] = meanings







