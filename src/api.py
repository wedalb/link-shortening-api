"""This module implements api functions and the endpoint"""

from fastapi import FastAPI, HTTPException
import validators
import linkshortener
import constants as c

app = FastAPI(
    title="Short.est URL Shortener API",
    description="This is a url shortener api written in python using fastapi",

)
"""This variable is a description of the api itself"""

link_shortener = linkshortener.LinkShortener()


@app.get("/")
def root():
    """A route in the api that outputs Hello world when you access the base url,
    Hello world, try /docs for documentation."""
    return {"message": "Hello world, try /docs for documentation."}


@app.get("/encode/{url:path}")
def encode_url(url):
    """
    An api endpoint that shortens a given url

    Parameters
    ----------
    url : str
        The url you want to shorten

    Raises
    ------
    HTTPException
        Invalid url possible typo

    Returns
    -------
    encoded_url
        a shortened url in json
    """
    short_url = link_shortener.url_dict.get(url)
    if url == "":
        message = f"URL is missing."
        return HTTPException(status_code=400, detail=message)
    if not validators.url(url):
        message = f"URL '{url}' is not a valid url. Please use only valid URLs."
        return HTTPException(status_code=400, detail=message)
    if short_url is None:
        short_url = c.BASE_URL + link_shortener.encode(url)
    return {"encoded_url": short_url}


@app.get("/decode/{url:path}")
def decode_url(url):
    """
    An api endpoint for decoding your shortened url

    Parameters
    ----------
    url : str
        The shortened url you want to decode

    Raises
    ------
    HTTPException
        Invalid url or url does not exist in memory

    Returns
    -------
    decoded_url
        the decoded url in json
    """
    if url == "":
        message = f"URL is missing."
        return HTTPException(status_code=400, detail=message)
    url_code = url.replace(c.BASE_URL, "")
    long_url = link_shortener.decode(url_code)
    if long_url is None:
        message = f"URL '{c.BASE_URL + url}' is not a valid URL. Please try a valid URL " \
                  f"or encode your url again using /encode"
        return HTTPException(status_code=404, detail=message)
    return {"decoded_url": long_url}