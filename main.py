
import requests
import logging
from pprint import pprint
from YaUploader import YaUploader
from VK import VK
import pip

def get_put_photos(dict_photos, list_photos, qty_photos):
    for item in range(qty_photos):
        URL = dict_photos[item]['sizes'][-1]['url']

        url = requests.get(URL)

        path_to_file = "Photo_vk/" + list_photos[item]['file_name']
        photo_name = url.content
        uploader = YaUploader(token_ya)
        uploader.upload(path_to_file, photo_name)

        print(f"Фото {item + 1} из vk загружено на яндекс диск")


def create_json(list_photos):
    with open("list_json.txt", 'w', encoding="utf-8") as file:
        for item in list_photos:
            file.writelines(str(item))
            file.writelines('\n')
    print("Файл \"list_json.txt\" создан")


if __name__ == '__main__':

    with open('token_vk.txt', "r") as file_object:
        token_vk = file_object.read().strip()
    with open('ID_vk.txt', "r") as file_object:
        ID_vk = file_object.read().strip()
    with open('token_ya.txt', "r") as file_object:
        token_ya = file_object.read().strip()

    vk = VK(token_vk, ID_vk)
    qty_user_photos = vk.users_photos()['response']['count']
    print(f"У пользователя {qty_user_photos} фотографий")

    qty_photos = int(input("Введите количество загружаемых фотографий: "))

    if qty_photos > qty_user_photos or qty_photos <= 0:
        print(f"Количество фотографий должно быть не менее 1 и не более {qty_user_photos}")
    else:
        dict_photos = vk.users_photos()['response']['items']
        print("Информация о фотографиях получена")
        list_photos = vk.get_list_photos(dict_photos=dict_photos, qty_photos=qty_photos)
        get_put_photos(dict_photos=dict_photos, list_photos=list_photos, qty_photos=qty_photos)
        create_json(list_photos=list_photos)
