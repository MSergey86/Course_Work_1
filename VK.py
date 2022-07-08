import requests

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {
           'user_ids': self.id,
           'fields' : 'education, sex'
       }
       response = requests.get(url, params={**self.params, **params})
       return response.json()

   def users_photos(self):
       url = 'https://api.vk.com/method/photos.get'
       params = {
           # 'owner_id': "-" + self.id,
           'owner_id': self.id,
           'album_id' : 'profile',
           'rev' : 0,
           'extended' : 1,
           'photo_sizes' : 1
       }
       response = requests.get(url, params={**self.params, **params})
       return response.json()
