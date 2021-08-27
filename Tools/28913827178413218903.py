import time
import vk_api
from colorama import init, Fore

from config import msg_comm , post_id_comm, user_id_comm, token

init(autoreset=True)

print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%', Fore.GREEN + '      Накрутка комментариев: ', Fore.BLUE + '     %%%')
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print()

def main():

    try:
        time.sleep(1)
        vk_session_1 = vk_api.VkApi(token=token)
        api_1 = vk_session_1.get_api()
        api_1.wall.createComment(owner_id=user_id_comm, post_id=post_id_comm, message=msg_comm)
        print(Fore.GREEN + 'Оставлен комментарий:\n' + msg_comm)
        print()
    except:
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(Fore.BLUE + '%%%', Fore.RED + '              Ошибка:             ', Fore.BLUE + '%%%')
        print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        time.sleep(60)

while True:
    main()