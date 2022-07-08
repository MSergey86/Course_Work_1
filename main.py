
import requests
import logging
from pprint import pprint
from YaUploader import YaUploader
from VK import VK



with open('token_vk.txt', "r") as file_object:
    token = file_object.read().strip()
with open('ID_vk.txt', "r") as file_object:
    ID_vk = file_object.read().strip()
with open('token_ya.txt', "r") as file_object:
    token_ya = file_object.read().strip()


access_token = token
user_id = ID_vk
qty_photos = 5  #количество загружаемых фотографий
vk = VK(access_token, user_id)
dict_photos = vk.users_photos()['response']['items']

list_json = []


if qty_photos <= len(vk.users_photos()['response']['items']):

    list_likes = []
    for item in range(qty_photos):
        like = str(dict_photos[item]['likes']['count'])
        if like in list_likes:
            file_name = str(dict_photos[item]['likes']['count']) + "_" + str(dict_photos[item]['date']) + ".jpg"
        else:
            file_name = like + ".jpg"
            list_likes.append(like)

        dict_photo = {}

        URL = dict_photos[item]['sizes'][-1]['url']
        type = dict_photos[item]['sizes'][-1]['type']

        dict_photo["file_name"] = file_name
        dict_photo["size"] = type
        list_json.append(dict_photo)


        p = requests.get(URL)
        out = open("D:\Sergey\Learning Fullstack\HomeWork_Python\Course_Work_I\photo\/" + file_name, "wb")
        out.write(p.content)
        out.close()

        path_to_file = "Photo_vk/" + file_name
        photo_name = "D:\Sergey\Learning Fullstack\HomeWork_Python\Course_Work_I\photo\/" + file_name
        uploader = YaUploader(token_ya)
        uploader.upload(path_to_file, photo_name)


        logging.basicConfig(
            level = logging.DEBUG,
            filename = "mylog.log",
            format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
            datefmt = "%H:%M:%S",
            )
        logging.info("Hello")

else:
    print(f"""максимальное количество фотографий: {len(vk.users_photos()['response']['items'])}""")

with open("D:\Sergey\Learning Fullstack\HomeWork_Python\Course_Work_I\photo\list_json.txt", 'w', encoding="utf-8") as file:
    for item in list_json:
        file.writelines(str(item))
        file.writelines('\n')
