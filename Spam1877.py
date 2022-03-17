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
    x1=input(Fade.Horizontal(Colors.green_to_cyan, "@> FOLDER NAME : "))
    if x1=="":
        print(Fade.Horizontal(Colors.green_to_cyan, (f"@> YOU CAN CREATE BLANK FOLDER")))
        time.sleep(1)
        main_()
    try:
        x=(int(input(Fade.Horizontal(Colors.green_to_cyan, "@> NUMBER OF THREAD : "))))
    except:
        print(Fade.Horizontal(Colors.green_to_cyan, (f"@> THATS NOT NUMBER...")))
        time.sleep(1)
        main_()
    if x>300:
        print(Fade.Horizontal(Colors.green_to_cyan, (f"@> MAKING 300+ FOLDER BECAUSE YOU PC GET BROKEN BY ME...")))
        time.sleep(3)
        main_()
    x-1
    folder=""
    x2=0
    
    for _ in range(x):
        folder+=f"/{x1}"
        x2+=1
        print(Fade.Horizontal(Colors.green_to_cyan, (f"@> FOLDER MADE {x2}")))

    os.makedirs(f"{x1}{folder}")
    time.sleep(.6)
    os.system("cls")
    logo()

    print(Fade.Horizontal(Colors.green_to_cyan, (f"@> SUCCESFULY MADE FOLDERS '{x1}' @> WITH {x} @> FOLDERS INSIDE.\n")))
    open=input(Fade.Horizontal(Colors.green_to_cyan, ("@> OPEN FOLDER ? Y/N")))
    if open=="y":
        p=f"{x1}{folder}"
        p=os.path.realpath(p)
        os.startfile(p)
    input(Fade.Horizontal(Colors.green_to_cyan, ("@> MADE BY D1MOD1877")))
    main_()

main_()

# if you're going to skid this, atleast give credit.
