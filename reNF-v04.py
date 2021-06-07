#!/usr/bin/env python3
#coding=utf-8
'''
Modify file names
Usage:
    V02
    1,reNF.py First_Few_letters Start_Number Extention
    2,enter or '.' will use current directory
    3,'enter' will use default setting
    V03
    rename all the files including the file in the directory
    V04
    rename the file with Number in the first place
'''
#By Gordon Cai 2018-04-05

import os,sys
defaultData = {'fExt':'jpg','letters':'','num':'1'}

def getDir():       #get the working dir ,'enter' or '.' will use the current directory
           
        while True:
            setDir = input('please input the full dir: ')
            if setDir =='.' or setDir =='':
                #setDir = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
                setDir = os.path.dirname(os.path.realpath(__file__))  #获取当前目录的方法2
            if os.path.exists(setDir):                    #change the dir
                    print('Will working on directory \''+ setDir+'\'')
                    os.chdir(setDir)
                    break
            else:
                    print('No such Dir or wrong input, Try again')

def getInfo():
    while True:
    	#print(defaultData['fExt'])
        print('\nCurrent working directory is '+ os.path.realpath(__file__))
        fExt = input('\nThe files category you want to rename(Q to quit): ')
        if fExt =='q' or fExt =='Q':
        	exit()
        if fExt == '':
        	fExt = defaultData['fExt']
        fExt = '.'+fExt
        print('work only on \''+fExt + '\' files')
        flag = 0
        path = os.path.dirname(os.path.realpath(__file__))
        for(path,dirs,files) in os.walk(path):
            for file in files:
                f=os.path.splitext(file)
                if f[1]==fExt:
                    flag+=1
        if flag:
            print('Totally '+str(flag)+' files exist')
            break
        else:print('no such ext file, Try again!')

        
    
    letters = input('\nFirst few letter you want(Q to quit): ')
    if letters =='q' or letters=='Q':
    	exit()
    if letters == '':
    	letters = defaultData['letters']
    num = input('\nEnter the number you want to start(Q to quit): ')
    if num == 'q' or num =='Q':
    	exit()
    if num == '':
    	num = defaultData['num']
   
    return fExt, letters, num

def soloReName(fExt,letters,num):
    #print('\nProcessing......')
    for file in os.listdir('.'):
        if int(num) < 100:
            num = '0'+ str(int(num))
            if int(num) <10:
                num = '00'+str(int(num))
            

        if os.path.splitext(file)[1] == fExt:
            print('rename file \''+file+ '\' to \''+letters+num+fExt+'\'')
            os.rename(file,letters+num+fExt)
            num= str(int(num)+1)
    print('\nDone!\n\n')
  #  updateDefault(fExt,letters,num)

#def updateDefault(fExt,letters,num):   
    # update default data
    fileName = os.path.realpath(__file__)
    fd = open(fileName)
    fData = []
    for lData in fd.readlines():
    	if lData.find('defaultData',0,12)== 0:
    		fExt=fExt[1:]
    		lData =  'defaultData={\'fExt\':\'%s\',\'letters\':\'%s\',\'num\':\'%s\'}\n'%(fExt,letters,num)
    	fData.append(lData)
    fd.close()
    fd = open(fileName,'w')
    fd.writelines(fData)
    print(fData)
    fd.close()
    #print('\ndefaultData updated:{\'fExt\':\'%s\',\'letters\':\'%s\',\'num\':\'%s\'}\n'%(fExt,letters,num))

def fullReName(fExt,letters,num):
    path = os.path.dirname(os.path.realpath(__file__))
    for(path,dirs,files) in os.walk(path):
        for file in files:
            if int(num) < 100:
                num = '0'+ str(int(num))
                if int(num) <10:
                    num = '00'+str(int(num))
                
            

            if os.path.splitext(file)[1] == fExt:
                print('rename file \''+file+ '\' to \''+num+letters+fExt+'\'')
                os.rename(path+'/'+file,path+'/'+num+letters+fExt)
                num= str(int(num)+1)
    print('\nDone!\n\n')
    #updateDefault(fExt,letters,num)

getDir()

fExt,letters,num = getInfo()
#check selection
while True:
    print('\nDo you want to rename files in all directories under current? (Y or N, Q to quit)')
    chSele = input('...')
    if chSele in ('Y','y','n','N','q','Q'):
        break
if chSele == 'q' or chSele == 'Q': exit()
if chSele == 'n' or chSele =='N':
	print('\nProecessing only in current directory......')
	soloReName(fExt,letters,num)
else:
	print('\nProecessing in full directory......')
	fullReName(fExt,letters,num)

