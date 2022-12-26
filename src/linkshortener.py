"""This module implements link shortening functions"""

import constants as c
import random

class LinkShortener:
    """This class is used to represent the link shortening functionalities

    Attributes
    ----------
    url_dict: dict
        the dictionary that is used to store long and short urls in memory

    Methods
    -------

    generate_random_code()
        generates a random string that is used as an individual key

    get_key_by_value(val: str)
        A code to get the key of a given value in the dictionary. Is used to decode the short url

    encode(long_url: str)
        encodes a long url into a short one, stores the long and short url pair in the
        dictionary and returns the short url code

    decode(short_url: str)
        decodes a short url into the long url by returning the value in the dictionary
        returns None if no value is found
    """

    url_dict = {}

    @staticmethod
    def generate_random_code() -> str:
        """
        This function generates a random code

        Returns
        -------
        random_code: str
            A random code made up of letters and digits with length 6
        """
        return ''.join(random.choices(c.CODE_STRUCTURE, k=c.CODE_LENGTH))

    def get_key_by_value(self, val: str) -> str:
        """
        A function to get the key by value in a dictionary

        Parameters
        ----------
        val: str
            The value you want to have the key of

        Returns
        -------
        key: str
            The key of the given value
        """
        for key, value in self.url_dict.items():
            if value == val:
                return key
        return 'Key Not Found'

    def encode(self, long_url: str) -> str:
        """
        A function that generates a shortened link by generating
        a random code and adding it to the base url

        Parameters
        ----------
        long_url: str
            The url you want to shorten

        Returns
        -------
        short_url: str
            The shortened url
        """
        if long_url not in self.url_dict:
            short_url = self.generate_random_code()
            self.url_dict[short_url] = long_url
            return short_url
        else:
            return self.url_dict.get_key_by_value(long_url)

    def decode(self, short_url: str) -> str:
        """
        A function that takes a shortened url and decodes it back to its
        original url by getting it from the dictionary

        Parameters
        ----------
        short_url: str
            The url you want to decode

        Returns
        -------
        long_url: str
            The decoded url
        """
        return self.url_dict.get(short_url)
