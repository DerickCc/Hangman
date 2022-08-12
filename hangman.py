import random
import os

listsoal=['anjing','babi','tikus','naga','singa','harimau','kelinci','buaya','kuda','burung',
      'monyet','sapi','kerbau','ular','gajah','siput','keledai','bebek','kodok','beruang',
      'lebah','rayap','cacing','jerapah','lalat','nyamuk','cicak','hyena','cheetah','rubah']

game=0
win=0
lose=0

while True:
    soal=random.choice(listsoal)
    listsoal.remove(soal)
    os.system('cls')

    game+=1
    print('Tebak Nama Hewan')
    print('================\n')

    chance=7
    tebakan=[]
    selesai = False
    while chance>0:
        tertebak=0
        for char in soal:
            if char in tebakan:
                print(char,end=' ')
            else:
                print('_',end=' ')
                tertebak+=1
        print()
        if tertebak==0:
            print('\nYou WIN !!')
            win+=1
            break

        while True:
            try:
                jwb=input('\nHuruf ? ').lower()
                if jwb>='a' and jwb<='z':
                    tebakan.append(jwb)
                    if jwb not in soal:
                        chance-=1
                        if chance>0:
                            print('Sisa',chance,'kesempatan\n')
                        else:
                            print('\nYou LOSE ?!?')
                            lose+=1
                    break
                else:
                    raise Exception('Hanya boleh huruf')
            except Exception as e:
                print('Error :',e)
    selesai = True

    if selesai == True: 
        while True:
            ulg=input('Main lagi (y/n) ? ').lower()
            if ulg in ('y','n'):
                break
        if ulg in ('n'):
            break 

os.system('cls')
print('Sumarry')
print('=======')
print('Played',game,'time(s)')
print('Win  =',win)
print('Lose =',lose)