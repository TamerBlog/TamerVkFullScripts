import time
import vk_api
from colorama import init, Fore

from config import token, msg_spam
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '           Спам беседы:           ', Fore.BLUE + '%%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print()
init(autoreset=True)

def mainloop():

    try:

        session = vk_api.VkApi(token=token)
        vk = session.get_api()

        chat = input("id беседы: ")
        r = vk.users.get(user_ids=chat, fields="id", v=5.73)
        r = r[0]["id"]
        chat = r
        print()

        while True:
            time.sleep(1)
            vk.messages.send(peer_id=2000000000 + chat, message=msg_spam, v=5.73)
            time.sleep(1)
            print(Fore.GREEN + "Отправлено: ", msg_spam)
            print()

    except:
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        time.sleep(60)


while True:
    mainloop()
