import math
import sys 

def is_power(number):
    if number == 0:
        return False
    
    power = math.log(number) / math.log(5)
    return (number == 5**power)

def count_cuts(str):
    n = len(str)
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0

    for i in range(1, n+1):
        for j in range(i):
            if str[j] == '0':
                continue
            
            if is_power(int(str[j:i], 2)):
                dp[i] = min(dp[i], dp[j] + 1)
    
    if dp[n] == sys.maxsize:
        return -1
    return dp[n]

def input_util():
    with open('input') as file:
        for line in file:
            print(count_cuts(line.strip()))

if __name__ == "__main__":
     input_util()