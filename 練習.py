# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:45:36 2019

@author: BRUCE.LU
"""
#print支援參數格式化，以下為練習:
# %s = 字串 ; %d = 整數 ; %f = 浮點數

name1 = "林小明"
score = 80
print("%s的成績為%d" % (name1, score))

price1 = 5                       
print("價格為%5d" % price1)      #固定列印5個字元，少於5位數則在數字左方填空白

name2 = "大家好"
print("哈囉!%8s" % name2)        #固定列印5個字元，少於5字元則在字串左方填空白

price2 = 2.8
print("價格為%8.3f" % price2)    #固定列印8個字元(含小數點)，小數固定列印3位數.
                                #若整數少於4位數(8-4)，會在數字左方填入空白。

#以字串的format做格式化，以一對大括號{}表示參數位置:
#語法 print(字串 .format(參數列))

name1 = "林小明"
score = 80
print("{}的成績為{}".format(name1, score))   #第一對大括號 = name變數
                                            #第二對大括號 = score變數

#type命令: 取得資料型態。
#語法 type(項目)

print(type(12))
print(type("你好!"))
print(type(True))

#2.1.4練習: 格式化列印
#目標: 以print命令列印成績單

print("姓名   座號   國文  數學  英文")
print("%3s   %2d   %3d   %3d   %3d" % ("林大明", 1, 100, 87, 79))
print("%3s   %2d   %3d   %3d   %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s   %2d   %3d   %3d   %3d" % ("張小英", 11, 82, 65, 8))

#input命令: 見2-9說明
#語法 變數 = input([提示字串])

score = input("請輸入數學成績:")
print(score)

#運算子
#算術運算子
# +, -, *, /, %, //, **

# % = 餘數
32%5
# // = 整除的商數
36//5
# ** = 次方
7**2

#關係運算子: 回傳True 或 False
# == (等於) ; !=(不等於) ; >(大於) ; <(小於) ; >=(大於或等於) ; <=(小於或等於)
#邏輯運算子: 回傳True 或 False.
# not (不是) ; and ; or
#複合指定運算子
# ex: 迴圈一般寫法 (i = i + 1, 變數值i進行運算後再指定給原來的變數)
# +=: 相加後再指定給原變數 (i = 10, i += 5 = 15)
# 其他如: -=, *=, /=, %=, //=, **= 皆是類似用法。

# 2.2運算式練習: input指令 & 各類運算子應用
# 目標: 計算總分級平均成績

score1 = input("請輸入國文成績:")
score2 = input("請輸入數學成績:")
score3 = input("請輸入英文成績:")
tot_score = int(score1) + int(score2) + int(score3)
avg_score = tot_score / 3
print("成績總分:%d，平均成績:%5.2f" % (tot_score, avg_score))

# 判斷式:根據關係運算或邏輯運算條件式來判斷程式執行的流程，若True則執行跳躍。
# if....elif....else
# 迴圈: 根據關係運算或邏輯運算條件式的結果True或False判斷，決定是否重複執行指定的程式
# for ; while


# 單向判斷式 if...
# 語法 if (條件式): 或 if 條件式:   (條件式可為關係運算式或邏輯運算式)

# 2.3.2練習: 密碼輸入判斷
# 目標: 使用者輸入正確密碼1234則顯示"歡迎光臨!" ; 輸入錯誤密碼則不顯示歡迎訊息

# My trial
welcome = input("請輸入密碼:")
if (int(1234)):
    welcome = "歡迎光臨!"
print(welcome)

# Book code
welcome = input("請輸入密碼:")
if (welcome == "1234"):
    print("歡迎光臨!")

# 雙向判斷式 if...else
# 語法 
#           if (條件式)/條件式:
#               程式區塊1
#           else:
#               程式區塊2
    
# 2.3.3練習: 進階密碼判斷
# 目標: 使用者輸入正確密碼1234則顯示"歡迎光臨!" ; 輸入錯誤密碼則顯示密碼錯誤訊息

# My trial = Book code
welcome2 = input("請輸入密碼:")
if (welcome2 == "1234"):
    print("歡迎光臨!")
else:
    print("密碼錯誤!")    

# 多向判斷式 if...elif...else
# 語法
#           if (條件式一)/條件式一:
#               程式區塊1
#           elif (條件式二)/條件式二:
#               程式區塊2
#               .....
#           else:
#               程式區塊else

# 2.3.4練習: 判斷成績等第
# 目標: 使用者輸入成績，成績90分以上 = 優等;80-89分=甲等....60分以下 = 丁等。

# My trial (Syntax error)
welcome3 = input("請輸入成績:")
if (welcome3 >= 90):
    print("優等")
elif (welcome3 > 80) or (welcome3 < 89):
    print("甲等")    
elif(welcome3 > 70) or (welcome3 < 79):
    print("乙等")
elif(welcome3 >= 60) or (welcome3 < 69):
    print("丙等")
else:
    print("丁等")    
    
# Book Code
score = input("請輸入成績:")
if(int(score) >= 90):
    print("優等")
elif(int(score) >= 80):
    print("甲等")
elif(int(score) >= 70):
    print("乙等")
elif(int(score) >= 60):
    print("丙等")
else:
    print("丁等")
    
# 2.3.5練習: 百貨公司折扣戰 (巢狀判斷式)
# 目標: 購買金額100000以上 = 8折; 50000以上 = 85折; 30000以上 = 9折; 10000以上 = 95折

# My trial (incomplete)
price = input("請輸入購物金額:")
if(int(price) >= 100000):
    price = float(price) * 0.8
    print(price)
elif(int(price) >= 50000):
    price = float(price) * 0.85
    print(price)
elif(int(price) >= 30000):
    price = float(price) * 0.9
    print(price)
elif(int(price) >= 10000):
    price = float(price) * 0.95
    print(price)
else:
    print(price)

# Book Code
money = int(input("請輸入購物金額:"))
if(money >= 10000):
    if(money >= 100000):
        print(str(money * 0.8), end = " 元\n")
    elif(money >= 50000):
        print(str(money * 0.85), end = " 元\n")
    elif(money >= 30000):
        print(str(money * 0.9), end = " 元\n")
    else:
        print(str(money * 0.95), end = " 元\n")
else:
    print(str(money), end = " 元\n")

# 3.1.1 串列(List) = 清單 或 列表
# 串列中每一個資料稱為"元素", 每一個元素相當於一個變數
# 取得元素值的方法為將索引值至於中括號內，正數從0開始，負數從-1開始(由後面數回)
# 語法  串列名稱 = [元素1, 元素2, ...]

list5 = [["joe","1234"], ["marry","abcd"], ["david","5678"]]
print(list5[1])
print(list5[1][1])

# 範例練習:串列初值設定
# 目標: 建立一個包含三個整數元素的串列，代表學生三科成績，再依序顯示各科成績。

# My trial
list1 = ["國文成績:","數學成績:","英文成績:"]
list2 = [85,79,93]
print(list1[0]+str(list2[0]), end = " 分\n", list1[1]+str(list2[1]), end = " 分\n", list1[2]+str(list2[2]), end = " 分\n")

# Book Code
score = [85,79,93]
print("國文成績: %d 分" % score[0])
print("數學成績: %d 分" % score[1])
print("英文成績: %d 分" % score[2])






