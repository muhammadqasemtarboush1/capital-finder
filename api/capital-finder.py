from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        # definitions = []
        country = ''
        capital = ''
        if 'capital' in dic:
            capital = dic['capital']
        if 'country' in dic:
            country = dic['country']
        '''
        The capital of Chile is Santiago
        '''
        if len(capital) > 1:
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + capital)
            data = r.json()
            for c_data in data:
                definition = c_data['capital'][0]
                countryname = c_data['name']['common']
                message = str(definition + ' is the capital of ' + countryname)
        elif len(country) > 1:
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()
            for c_data in data:
                definition = c_data['name']['common']
                c_name = c_data['capital'][0]
            message = str('The capital of' + definition + ' is' + c_name)
        else:
            '''
             Santiago is the capital of Chile
            '''
            message = "Please provide capital= somthing or country= somthing" + capital + country

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return