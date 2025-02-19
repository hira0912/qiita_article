# 10進数でinputし、絶対値も算出する
num_10:int = int(input())
num_10_abs:int = abs(num_10)

# 結果文字列
result:str = ''
pos:int = 1

# num_10_abs==0になるまで3進数の桁を追加する
while num_10_abs:
    value:int = num_10_abs % pow(3, pos) // pow(3, pos-1) # 3進数での各桁の値
    result += str(value)
    if(value<2):
        num_10_abs -= value * pow(3, pos-1) # valueが0,1の場合は元の値から引く
    else:
        num_10_abs += pow(3, pos-1) # valueが2の場合は元の値にギャップを加算しておく
    pos += 1

# 逆順になった配列を反転させる
result_rev:str = result[::-1]

# 元の値が負数の場合は特殊3進数を考慮して1と2を入れ替える
if(num_10 < 0):
    for i in range(len(result_rev)):
        if(result_rev[i] == '1'):
            result_rev = result_rev[:i] + '2' + result_rev[i+1:]
        elif(result_rev[i] == '2'):
            result_rev = result_rev[:i] + '1' + result_rev[i+1:]

# return
print(result_rev)