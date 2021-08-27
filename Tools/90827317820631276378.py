import time
import vk_api
from colorama import init, Fore

from config import token

init(autoreset=True)

print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '         Флуд в беседу:           ', Fore.BLUE + '%%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')


def main():

    chat = input('id беседы: ')
    user = input('id пользователя: ')
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()

    try:
        while True:
            api.messages.removeChatUser(chat_id=chat, user_id=user)
            print(Fore.GREEN + 'Выход:\n')
            api.messages.addChatUser(chat_id=chat, user_id=user)
            print(Fore.GREEN + 'Вход:\n')
            print()
    except:
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        time.sleep(60)

while True:
    main()
