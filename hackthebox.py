import requests
import json
from bs4 import BeautifulSoup
class HackTheBox:
    def __init__(self,api_token=''):
        self.api_token = api_token
    def get_machines(self):
        '''
        returns an integer
        '''
        data = requests.post('https://www.hackthebox.eu/api/stats/global').text
        machines = json.loads(data)['data']['machines']
        return machines
    def get_top(self,amount):
        '''
        get_top(self,amount)
        example: get_top(10)

        returns a dict

        if amount is higher than 100, it returns None
        '''
        if amount > 100:
            return None
        
        soup = BeautifulSoup(requests.get('https://www.hackthebox.eu/#hofTab').text,'html.parser')
        top10 = {}
        for i in range(1,amount+1):
            top10[i] = soup.find_all('tr')[i].find_all('td')[1].text
        return top10
    def get_user_id(self,username):
        '''
        get_user_id(self,username)

        returns an integer

        gets the profile id of a user based on their name
        requires an API token
        '''
        param = {'username':username}
        data = json.loads(requests.post('https://www.hackthebox.eu/api/user/id?api_token={}'.format(self.api_token,),params=param))
        user_id = data['id']
        return user_id
    
