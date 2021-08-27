import time
import vk_api
from colorama import init, Fore

from config import token, msg_spam

print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '           Спам в лс:             ', Fore.BLUE + '%%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

init(autoreset=True)


def mainloop():

    session = vk_api.VkApi(token=token)
    vk = session.get_api()

    user = input("id пользователя: ")

    try:
        while True:
            vk.messages.send(user_id=user, message=msg_spam, v=5.73)
            time.sleep(1)
            print(Fore.GREEN + "Отправлено: ", msg_spam)

    except:
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

while True:
    mainloop()
