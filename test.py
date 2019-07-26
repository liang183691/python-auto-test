import math
import random
import json

weight = [0, 2, 3, 4, 5]   #商品体积
value = [0, 3, 4, 5, 6]    #商品价值
bagV = 8            #背包重量
dp = [[0 for i in range(9)] for j in range(5)]            #策略表格
item = [0]*4           #最优选择项

def findMax():
    for i in range(1, 5):
        for j in range(1, bagV+1):
            if(j < weight[i]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
def findWhat(i,j):
    if i > 0:
        if dp[i][j] == dp[i-1][j]:
            item[i-1] = 0
            findWhat(i-1, j)
        elif dp[i][j] == dp[i-1][j-weight[i]]+value[i]:
            item[i-1] = 1
            findWhat(i-1, j-weight[i])

findMax()
findWhat(4, 8)
print('策略表格:\n', dp)
print('最优选择:\n', item)