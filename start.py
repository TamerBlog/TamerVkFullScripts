import os

from colorama import init, Fore


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

clear()

def main():
    init(autoreset=True)
    print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(Fore.BLUE + '%%%         ', Fore.GREEN + 'Выберите пункт:', Fore.BLUE + '       %%%')
    print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(Fore.BLUE + '%%%', Fore.YELLOW + '1.', Fore.GREEN + 'Boost comment', Fore.YELLOW + '6.',
          Fore.GREEN + 'Flud chat', Fore.BLUE + '  %%%')
    print(Fore.BLUE + '%%%', Fore.YELLOW + '2.', Fore.GREEN + 'Boost message', Fore.YELLOW + '7.',
          Fore.GREEN + 'Spam chat', Fore.BLUE + '  %%%')
    print(Fore.BLUE + '%%%', Fore.YELLOW + '3.', Fore.GREEN + 'Boost friends', Fore.YELLOW + '8.',
          Fore.GREEN + 'Spam owner', Fore.BLUE + ' %%%')
    print(Fore.BLUE + '%%%', Fore.YELLOW + '4.', Fore.GREEN + 'Boost photo', Fore.YELLOW + '  9.',
          Fore.GREEN + 'Auto status', Fore.BLUE + '%%%')
    print(Fore.BLUE + '%%%', Fore.YELLOW + '5.', Fore.GREEN + 'Boost post', Fore.YELLOW + '  10.',
          Fore.GREEN + 'Chat killer', Fore.BLUE + '%%%')
    print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print()

    opt = input('Ответ: ')

    if opt == "1":
        clear()
        os.system(r'python ./Tools/28913827178413218903.py')
        clear()
        os.system('python start.py')

    if opt == "2":
        clear()
        os.system(r'python ./Tools/18923687162837812790.py')
        clear()
        os.system('python start.py')

    if opt == "3":
        clear()
        os.system(r'python ./Tools/87987897638967264792.py')
        clear()
        os.system('python start.py')

    if opt == "4":
        clear()
        os.system(r'python ./Tools/23749872389473267483.py')
        input()
        clear()
        os.system('python start.py')

    if opt == "5":
        clear()
        os.system(r'python ./Tools/28743699067845343221.py')
        clear()
        os.system('python start.py')

    if opt == "6":
        clear()
        os.system(r'python ./Tools/90827317820631276378.py')
        clear()
        os.system('python start.py')

    if opt == "7":
        clear()
        os.system(r'python ./Tools/09827346283879024632.py')
        clear()
        os.system('python start.py')

    if opt == "8":
        clear()
        os.system(r'python ./Tools/86786786896782626478.py')
        clear()
        os.system('python start.py')

    if opt == "9":
        clear()
        os.system(r'python ./Tools/93408570345703879437.py')
        input()
        os.system('python start.py')

    if opt == "10":
        clear()
        os.system(r'node ./Tools/23654327427537917870.js')
        clear()
        os.system('python start.py')

main()
clear()
print(Fore.BLUE + '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print(Fore.BLUE + '%%%        ', Fore.RED + 'Неверный пункт:', Fore.BLUE + '        %%%')
os.system('python start.py')

