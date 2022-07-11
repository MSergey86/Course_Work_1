import requests
from pprint import pprint

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   # def users_info(self):
   #     url = 'https://api.vk.com/method/users.get'
   #     params = {
   #         'user_ids': self.id,
   #         'fields' : 'education, sex'
   #     }
   #     response = requests.get(url, params={**self.params, **params})
   #     return response.json()

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

   def get_list_photos(self, dict_photos, qty_photos):

       list_photos = []
       list_likes = []
       for item in range(qty_photos):
         like = str(dict_photos[item]['likes']['count'])
         if like in list_likes:
            file_name = str(dict_photos[item]['likes']['count']) + "_" + str(dict_photos[item]['date']) + ".jpg"
         else:
            file_name = like + ".jpg"
            list_likes.append(like)

         type = dict_photos[item]['sizes'][-1]['type']
         dict_photo = {}
         dict_photo["file_name"] = file_name
         dict_photo["size"] = type
         list_photos.append(dict_photo)

         print(f"Даем название фотографии {item + 1}")

       return list(list_photos)
