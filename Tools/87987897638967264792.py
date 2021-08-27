import time
import os
import vk_api
from colorama import init, Fore

from config import token


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
init(autoreset=True)


def logo():
    print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(Fore.BLUE + '%%%', Fore.GREEN + '        Накрутка друзей:          ', Fore.BLUE + '%%%')
    print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')


logo()


def main():

    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()

        usr_list = vk.users.search(count=200)
        usr_banlist = vk.account.getBanned()

        for i in range(len(usr_list['items'])):
            usr_id = usr_list['items'][i]['id']
            usr_fname = usr_list['items'][i]['first_name']
            usr_lname = usr_list['items'][i]['last_name']
            print(Fore.YELLOW + '\nИмя: ' + usr_fname + '\nФамилия: ' + usr_lname)

            if usr_id in usr_banlist:
                print(Fore.RED + 'Пользователь находится в ЧС')
            else:
                print(Fore.GREEN + 'Отправил')

                try:
                    vk.friends.add(user_id=usr_id)
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
pass
