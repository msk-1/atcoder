# 何行入力されるかわからない文字のシステム入力。
# 改行コードが入力されると終了
import sys
a = []
for l in sys.stdin:
    if l == '\n':
        break
    else :
        a.append(l)
        
# 何行入力されるか分かる場合ver
n=int(input())
a = [int(input()) for i in range(n)]

# 何行入力されるか分かる場合ver(input文字列をソートして配列に入れる)
a=[''.join(sorted(input())) for _ in range(n)]