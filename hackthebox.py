import requests
import json
from bs4 import BeautifulSoup


class HackTheBox:
    def __init__(self, API_TOKEN=''):
        self.API_TOKEN = API_TOKEN
    def get_machines(self):
        '''
        Get the total of machines
        '''

        data = requests.post('https://www.hackthebox.eu/api/stats/global').text

        return json.loads(data)['data']['machines']

    def get_top(self, amount):
        '''
        get_top(self, amount)

        example: get_top(10)

        return a dict of the top X

        if amount is higher than 100, it returns None
        '''

        if amount > 100:
            return None

        url = 'https://www.hackthebox.eu/api/charts/users/scores/?api_token={}'.format(self.API_TOKEN)
        r = requests.get(url).text
        data = json.loads(r)['chartData']
        topX = {}

        for i in range(1, amount+1):
            topX[i] = data[0]['name']

        return topX

    def get_userid(self, username):
        '''
        get_user_id(self,username)

        returns an integer

        gets the profile id of a user based on their name
        requires an API token
        '''

        url = 'https://www.hackthebox.eu/api/user/id?api_token={}'.format(self.API_TOKEN)
        r = requests.post(url,params={'username': username})
        data = json.loads(r)
        
        user_id = data['id']

        return user_id
    def get_owns(self, type):
        '''
        Get owns of the user
        '''

        url = 'https://www.hackthebox.eu/api/machines/get/owns/?api_token={}'.format(self.API_TOKEN)
        r = requests.post(url).text
        owns = json.loads(r)
        try:
            return owns[type]
        except:
            print 'Incorrect usage!'

    def get_status(self, vpn, machine_id):
        '''
        Get the status of a machine on a vpn server
        '''

        url = 'https://www.hackthebox.eu/api/machines/vpnping/{}?api_token={}'.format(vpn, self.API_TOKEN)
        r = requests.post(url,params={'id':machine_id}).text
        status = json.loads(r)['status']

        return status
