result_list = ['0'] # 結果配列の初期作成
current = ['0'] # 現在の特殊3進数の値配列

# 1~100000までの値の算出と格納
for _ in range(100000):
    i = 0  
    carry = 1 # 繰り上がりの有無
    
    # 1足した後の各桁の数値変更を行う
    while i < len(current) and carry:
        digit = int(current[i])
        if(digit == 1):
            current[i] = '2'
            carry = 1
        elif(digit == 2):
            current[i] = '0'
            carry = 0
        else:
            current[i] = '1'
            carry = 0
        i += 1
    
    # 全ての計算を終えた後に繰り上がりが残っている場合
    if carry:
        current.append('1')
    
    # 結果配列result_listに追加
    result_list.append(''.join(current[::-1]))

# 10進数でinputし、絶対値も算出する
num_10:int = int(input())
num_10_abs:int = abs(num_10)

# 配列から値を取得
result:str = result_list[num_10_abs]

# 元の値が負数の場合は特殊3進数を考慮して1と2を入れ替える
if(num_10 < 0):
    for i in range(len(result)):
        if(result[i] == '1'):
            result = result[:i] + '2' + result[i+1:]
        elif(result[i] == '2'):
            result = result[:i] + '1' + result[i+1:]

# return
print(result)