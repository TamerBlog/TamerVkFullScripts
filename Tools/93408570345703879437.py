import datetime

import time
import vk_api
from colorama import init, Fore

from config import token

init(autoreset=True)

print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '           Авто Статус:           ', Fore.BLUE + '%%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print()


def main():

    try:
        session = vk_api.VkApi(token=token)
        vk = session.get_api()

        time1 = datetime.datetime.today().strftime("%H:%M")
        date1 = datetime.datetime.today().strftime("%d:%m")
        vk.status.set(text='Date: ' + date1 + ' Time: ' + time1)
        print(Fore.GREEN + 'Сейчас в статусе: ', date1 + ' ' + time1)
        print()
        time.sleep(60)

    except:
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        time.sleep(60)


while True:
    main()