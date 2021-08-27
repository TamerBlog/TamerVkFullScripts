import time
import vk_api
from colorama import init, Fore

from config import user_id_msg, title_msg, token

init(autoreset=True)

print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '       Накрутка сообщений:        ', Fore.BLUE + '%%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print()

def main():
    try:
        time.sleep(1)
        vk_session_1 = vk_api.VkApi(token=token)
        api_1 = vk_session_1.get_api()
        api_1.messages.createChat(user_ids=user_id_msg, title=title_msg)
        print(Fore.GREEN + 'Создана беседа: ', title_msg)
        print()
    except:
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        time.sleep(60)

while True:
    main()
