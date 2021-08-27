import time
import os
import vk_api
from colorama import init, Fore

from config import token, msg_post


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
init(autoreset=True)

print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '         Накрутка постов:         ', Fore.BLUE + '%%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print()

def main():

    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()

        try:
            vk.wall.post(message=msg_post)
            print(Fore.GREEN + 'Опубликован пост:\n' + msg_post)
            print()
            time.sleep(1)

        except:
            print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
            print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            time.sleep(60)
    except:
        clear()
        os.system('python start.py')

while True:
    main()
