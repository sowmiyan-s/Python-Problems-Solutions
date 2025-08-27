n = int(input())
arr=[]
arr = list(map(int, input().split()))
total_sum = (n * (n + 1)) // 2  
actual_sum = sum(arr) 
print(total_sum - actual_sum)