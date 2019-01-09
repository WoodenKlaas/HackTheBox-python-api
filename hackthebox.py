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
        
        soup = BeautifulSoup(requests.get('https://www.hackthebox.eu/#hofTab').text,'html.parser')
        top10 = {}

        for i in range(1, amount+1):
            top10[i] = soup.find_all('tr')[i].find_all('td')[1].text

        return top10

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

        url = 'https://www.hackthebox.eu/api/machiines/vpnping/{}?api_token={}'.format(vpn, self.API_TOKEN)
        r = requests.post(url,params={'id':machine_id}).text
        status = json.loads(r)['status']

        return status
