import os, requests, ctypes, time
from pystyle import Center, Cursor
from pyfade import Fade, Colors

r=requests.get('https://pastebin.com/67RFp4wN').text

def logo():
    ascii="""
███████╗ ██████╗ ██╗     ██████╗ ███████╗██████╗     ███████╗██████╗  █████╗ ███╗   ███╗
██╔════╝██╔═══██╗██║     ██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
█████╗  ██║   ██║██║     ██║  ██║█████╗  ██████╔╝    ███████╗██████╔╝███████║██╔████╔██║
██╔══╝  ██║   ██║██║     ██║  ██║██╔══╝  ██╔══██╗    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
██║     ╚██████╔╝███████╗██████╔╝███████╗██║  ██║    ███████║██║     ██║  ██║██║ ╚═╝ ██║
╚═╝      ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝"""
    print(Fade.Vertical(Colors.green_to_cyan, Center.XCenter(ascii)))
    print(Fade.Horizontal(Colors.black_to_green, Center.XCenter("────────────────────────────────────────────────────────────────────────────────────────────")))
    print(Fade.Horizontal(Colors.green_to_cyan, Center.XCenter(f"MADE BY D1MOD1877")))
    print(Fade.Horizontal(Colors.black_to_green, Center.XCenter("────────────────────────────────────────────────────────────────────────────────────────────")))
    print("")

def main_():
    os.system("cls")
    Cursor.HideCursor()
    os.system("mode 92, 40")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Folder Spam | {r}")

    logo()
    x1=input(Fade.Horizontal(Colors.green_to_cyan, "Folder name: "))
    if x1=="":
        print(Fade.Horizontal(Colors.green_to_cyan, (f"You cant create a blank folder silly.")))
        time.sleep(1)
        main_()
    try:
        x=(int(input(Fade.Horizontal(Colors.green_to_cyan, "Amount of folders inside: "))))
    except:
        print(Fade.Horizontal(Colors.green_to_cyan, (f"Thats not a number.")))
        time.sleep(1)
        main_()
    if x>300:
        print(Fade.Horizontal(Colors.green_to_cyan, (f"Making more than 300 folders inside will end up breaking your explorer/pc.")))
        time.sleep(3)
        main_()
    x-1
    folder=""
    x2=0
    
    for _ in range(x):
        folder+=f"/{x1}"
        x2+=1
        print(Fade.Horizontal(Colors.green_to_cyan, (f"Folders made: {x2}")))

    os.makedirs(f"{x1}{folder}")
    time.sleep(.6)
    os.system("cls")
    logo()

    print(Fade.Horizontal(Colors.green_to_cyan, (f"Successfully made folder '{x1}' with {x} folders inside.\n")))
    open=input(Fade.Horizontal(Colors.green_to_cyan, ("Open folder(y/n): ")))
    if open=="y":
        p=f"{x1}{folder}"
        p=os.path.realpath(p)
        os.startfile(p)
    input(Fade.Horizontal(Colors.green_to_cyan, ("Thanks for using my tool!")))
    main_()

main_()

# if you're going to skid this, atleast give credit.
