from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(dic,"dic")
        definitions = []
        if 'word' in dic:
            word = dic['word']
            print(word, "word")
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + word)
            data = r.json()
            print(data,"wordwordwordwordwordwordwordwordword")
            for word_data in data:
                definition = word_data['meanings'][0]['definitions'][0]['definition']
                definitions.append(definition)

            message = str(definitions)

        else:
            message = "Please provide me with a word"


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return