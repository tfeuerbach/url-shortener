import csv
import json
import re
import requests
import validators
from argparse import ArgumentParser
from pprint import pprint
from pyfiglet import Figlet


def get_url(url: str):
    endpoint = 'http://myshortened.link/url'
    query = {"target_url" : url}
    response = requests.post(endpoint, json=query)
    return response.json()

def view_url(admin_url: str):
    if 'http://myshortened.link/admin/' not in admin_url:
        print('\nArgument must be http://myshortened.link/admin/YOUR_SECRET_KEY')
    else:
        response = requests.get(admin_url)
        return response.json()

def delete_url(admin_url: str):
    if 'http://myshortened.link/admin/' not in admin_url:
        print('\nArgument must be http://myshortened.link/admin/YOUR_SECRET_KEY')
    else:
        response = requests.delete(admin_url)
        return response.json()

if __name__ == '__main__':
    parser = ArgumentParser(description='A command line tool for interacting with the myshortened.link API')
    parser.add_argument('-g', '--get', action='store', help='shows a preview of the data.')
    parser.add_argument('-s', '--show', action='store', help='view information about your shortened URL. Takes the Admin URL as the argument.')
    parser.add_argument('-d', '--delete', action='store', help='deletes the shortened URL from the database. Takes the Admin URL as the argument.')

    args = parser.parse_args()

    if args.get:
        response = get_url(args.get)
        admin_url = response['admin_url']
        secret_key = re.search(r'(?<=admin/).*', admin_url)

        print(f"\n"
              f"{response['target_url']} --- shortened to ---> {response['url']}\n"
              f"\n"
              f"Admin URL --> {response['admin_url']}\n"
              f"Secret Key -> {secret_key.group(0)}\n")

    if args.show:
        response = view_url(args.show)

        print(f"\n"
              f"Admin Info for {response['admin_url']}\n"
              f"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
              f"Target URL -------> {response['target_url']}\n"
              f"Shortened URL ----> {response['url']}\n"
              f"Admin URL --------> {response['admin_url']}\n"
              f"Active -----------> {response['is_active']}\n"
              f"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
              f"Your shortened URL has been clicked {response['clicks']} time(s)."
              f"\n")

    if args.delete:
        target_url = view_url(args.delete)
        response = delete_url(args.delete)

        print(f"\n"
              f"Shortened URL for {target_url['target_url']} successfuly deleted!")

    else:
        f = Figlet(font='doom')
        print(f.renderText('url    shortener'))
        print('Use the -h or --help flags for help')    