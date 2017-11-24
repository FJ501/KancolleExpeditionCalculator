#coding=utf-8
import os

Error1 = '不能输入两个相同的远征'                                                                                  #定义文本和基础数据
Error2 = '不能输入是/否外的任何内容'
data = 'data'
Yes = '是'
No = '否'
textResult = '远征收益(每小时)：'
textOil = '油：'
textAmmo = '，弹：'
textSteel = '，钢：'
textAluminum = '，铝：'
data01 = [0,120,0,0]
data02 = [0,200,60,0]
data03 = [90,90,120,0]
data04 = [0,72,0,0]
data05 = [133,133,13,13]
data06 = [0,0,0,120]
data07 = [0,0,50,30]
data08 = [17,33,17,17]
data09 = [88,0,0,0]
data10 = [0,33,0,20]
data11 = [0,0,0,50]
data12 = [6,31,25,6]
data13 = [60,75,0,0]
data14 = [0,1.40,33,0]
data15 = [0,0,25,33]
data16 = [33,33,13,13]
data17 = [93,93,67,0]
data18 = [0,0,60,20]
data19 = [67,0,9,5]
data20 = [0,0,75,0]
data21 = [137,116,0,0]
data22 = [0,3,0,0]
data23 = [0,5,0,25]
data24 = [60,0,0,18]
data25 = [23,0,13,0]
data26 = [0,0,0,11]
data27 = [0,0,40,0]
data28 = [0,0,36,14]
data29 = [0,0,0,4]
data30 = [0,0,0,2]
data31 = [0,15,0,0]
data32 = [2,2,2,2]
data33 = [0,0,0,0]
data34 = [0,0,0,0]
data35 = [0,0,34,40]
data36 = [53,0,22,22]
data37 = [0,135,102,0]
data38 = [144,0,69,0]
data39 = [0,0,10,0]
data40 = [43,43,0,13]
dataA1 = [108,108,0,0]
dataA2 = [76,43,0,11]
dataA3 = [53,0,27,27]
dataB1 = [0,0,17,51]

print('本程序计算远征每小时收益，用于对比最合适的远征组合。你需要分3次输入数据\n'                            #定义输入格式#
      '输入格式：远征1编号(01~40) 远征2编号 远征3编号\n'
      '远征1大成功(是/否) 远征2大成功 远征3大成功\n'
      '远征1大发数量(1~4) 远征2大发数 远征3大发数\n')

input1, input2, input3 = input('输入远征编号：').strip().split()                                                 #分离数据并储存为string#
inputsuccess1, inputsuccess2, inputsuccess3 = input('输入大成功状态：').strip().split()
inputcraft1, inputcraft2, inputcraft3 = input('输入大发数量：').strip().split()

if input1 == input2:                                                                                             #纠错信息
    print(Error1)
if input1 == input3:
    print(Error1)
if input2 == input3:
    print(Error1)
if inputsuccess1 != Yes:
    if inputsuccess1 != No:
        print(Error2)
if inputsuccess2 != Yes:
    if inputsuccess2 != No:
        print(Error2)
if inputsuccess3 != Yes:
    if inputsuccess3 != No:
        print(Error2)

inputcraftint1 = int(inputcraft1)                                                                                #str变为int
inputcraftint2 = int(inputcraft2)
inputcraftint3 = int(inputcraft3)
if inputcraftint1>4:                                                                                             #数值纠正
    craft1 = 4
if inputcraftint1<1:
    craft1 = 0
craft1 = inputcraftint1
if inputcraftint2>4:
    craft2 = 4
if inputcraftint2<1:
    craft2 = 0
craft2 = inputcraftint2
if inputcraftint3>4:
    craft3 = 4
if inputcraftint3<1:
    craft3 = 0
craft3 = inputcraftint3

if inputsuccess1 == Yes:                                                                                         #计算增益
    if craft1 == 0:
        gain1 = 1.5
    gain1 = 0.05*craft1+1.5
gain1 = 1
if inputsuccess2 == Yes:
    if craft2 == 0:
        gain2 = 1.5
    gain2 = 0.05*craft2+1.5
gain2 = 1
if inputsuccess3 == Yes:
    if craft3 == 0:
        gain3 = 1.5
    gain1 = 0.05*craft3+1.5
gain3 = 1

ex1 = eval(data+input1)                                                                                          #从数据列表获得远征信息
ex2 = eval(data+input2)
ex3 = eval(data+input3)

Oil1, Ammo1, Steel1, Aluminum1 = ex1                                                                             #设定各远征槽收益
Oil2, Ammo2, Steel2, Aluminum2 = ex2
Oil3, Ammo3, Steel3, Aluminum3 = ex3

resultOil = Oil1*gain1 + Oil2*gain2 + Oil3*gain3                                                                 #应用增益
resultAmmo = Ammo1*gain1 + Ammo2*gain2 + Ammo3*gain3
resultSteel = Steel1*gain1 + Steel2*gain2 + Steel3*gain3
resultAluminum = Aluminum1*gain1 + Aluminum2*gain2 + Aluminum3*gain3

print (textResult,textOil,resultOil,textAmmo,resultAmmo,textSteel,resultSteel,textAluminum,resultAluminum)
os.system("pause")