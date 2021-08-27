import os
import time
import vk_api
from colorama import init, Fore
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll

from config import token, album_id_photo


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
init(autoreset=True)

print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '          Накрутка фото:          ', Fore.BLUE + '%%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print()

def main():

    try:
        vk_session = vk_api.VkApi(token=token)
        longpoll = VkLongPoll(vk_session)

        a = 0
        for _ in longpoll.listen():
            try:
                count = 10000
                al = album_id_photo
                upload = VkUpload(vk_session)
                for x in range(int(count)):
                    upload.photo(photos="./Tools/Photo/photo1.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo2.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo3.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo4.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo5.png", album_id=int(al))
                    a += 1
                    upload.photo(photos="./Tools/Photo/photo6.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo7.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo8.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo9.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
                    upload.photo(photos="./Tools/Photo/photo10.png", album_id=int(al))
                    a += 1
                    print('+', a, 'Фото')
            except Exception:
                print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
                print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                time.sleep(60)
    except:
        clear()
        os.system('python start.py')
while True:
    main()
