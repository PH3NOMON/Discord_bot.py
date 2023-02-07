import discord
import os
import requests
import json


def wyr():
    r = requests.get("https://api.truthordarebot.xyz/v1/wyr")
    res = r.json()

    return res['question']


def dog():
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    res = r.json()

    return res['message']


def Truth():
    r = requests.get("https://api.truthordarebot.xyz/v1/truth")
    res = r.json()

    return res['question']


def Cat():
    r = requests.get("http://aws.random.cat/meow")
    res = r.json()

    return res['file']


def get_joke():
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas"
    )
    json_data = json.loads(response.text)

    joke = json_data["setup"]
    reply = json_data["delivery"]
    new_line = '\n'
    full_joke = f'{joke} {new_line}- {reply}'

    return (full_joke)
