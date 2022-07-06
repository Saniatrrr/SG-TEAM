'''this project for ditermine age'''
###import system#####
import os
######logo######
logos = ("""\033[1;32m
       
████╗░░███╗░█████╗░██╗░░██╗░█████╗░██████╗░
████╗░████║██╔══██╗██║░░██║██╔══██╗██╔══██╗
██╔████╔██║███████║███████║███████║██████╦╝
██║╚██╔╝██║██╔══██║██╔══██║██╔══██║██╔══██╗
██║░╚═╝░██║██║░░██║██║░░██║██║░░██║██████╦╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░ \033
__________________×______________________
__________________×______________________
  
  Auther   : Mahabub Vi
 
  Github   :https://github.com/Saniatrrr

  Facebook : ⭐⭐⭐⭐
  
  Contact :+8801830885369
  	
  Note:it is only free for sg✓71 member 
__________________×______________________\033[1;37m""")
logo = "\u001b[32m_____________[AGE DITERMINER]_____________"
#####function#######
print(logos)
print(logo)
print("present year")
now_year = input()
print("present mounth")
now_mounth = input()
print("TODAY")
now_day = input()
#######user######
print("_______________BIRTH INFORMATION_____________")
print("BRITH YEAR")
year = input()
print("BEITH MOUNTH")
mounth = input()
print("brith day")
day = input()
######calculate#######
y = int(now_year)-int(year)
m = int(now_mounth)-int(mounth)
d = int(now_day)-int(day)
####list####
ms = 12
ds = 30
c =[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -26, -27, -28, -29,]
###### if else ######
if m in c:
    yc = y-1
    mc = ms+m 
else:
    yc = y
    mc = m
if d in c:
    mv = mc-1
    dc = ds+d
else:
    mv = mc
    dc = d
if mv == -1:
    yv = yc-1
    mv = 0
else:
    yv = yc
    mv = mv
if dc == -1:
    mv+=1
    dc = 1
else:
    mv = mv
    dc = dc
    

######result####
print("__________________[YOUR AGE]____________________")
print("YEAR")
print(yv)
print("MOUNTH")
print(mv)
print("DAY")
print(dc)
print("[1]START AGAIN")
MAHABUB = input("choose:")
if MAHABUB in ["1", "01"]:
	os.system('clear')
	os.system('python age.py')
	os.system('clear')
""" YOU SHOULD PRACTICE MANUALY AND DO NEW THING LIKE THIS
REMEMBET IT PRACTICE MAKES A MAN PERFECT     [MAHABUB- VAU]"""