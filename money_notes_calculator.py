n = int(input("Enter some amount: "))
total_sum = 0
sum_2000=0
sum_500 = 0
sum_100 = 0
sum_50 = 0
sum_10 = 0
sum_5 = 0 
sum_2 = 0 
sum_1 = 0
while(total_sum+2000<=n):
    sum_2000=sum_2000+1
    total_sum = total_sum+2000
while(total_sum+500<=n):
    sum_500=sum_500+1
    total_sum = total_sum+500
while(total_sum+100<=n):
    sum_100=sum_100+1
    total_sum = total_sum+100
while(total_sum+50<=n):
    sum_50=sum_50+1
    total_sum = total_sum+50
while(total_sum+10<=n):
    sum_10 = sum_10+1
    total_sum = total_sum+10
while(total_sum+5<=n):
    sum_5 = sum_5+1
    total_sum = total_sum+5
while(total_sum+2<=n):
    sum_2 = sum_2+1
    total_sum = total_sum+2
while(total_sum+1<=n):
    sum_1 = sum_1+1
    total_sum = total_sum+1
print("The Individual Notes Required are")
print("2000's = ",sum_2000)
print("500's = ",sum_500)
print("100's = ",sum_100)
print("50's = ",sum_50)
print("10's = ",sum_10)
print("5's = ",sum_5)
print("2's = ",sum_2)
print("1's = ",sum_1)
