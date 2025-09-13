# first task\
# f=open(file='book_store.txt', mode='r')
# print(f.readlines())


#  multiplication table
# for i in range(1,10):
#     for j in range(1,10):
#          print(i,'*',j,'=' , i*j, end=' ')
#     print()



# # #third task

from datetime import datetime
now=datetime.now()
current_time=now.time()
# print(current_time)
# first way
saat = ''
for ch in str(current_time):
    if (ch == '.'):
        break
    else:
        saat = saat +ch
print(saat)
# second way
# new_list=[]
# current_time=str(current_time)
#
# new_list.append(current_time)
# print(new_list)
# saat=new_list[0][0:8]
# saat=str(saat)
# print(saat) zaman bedari
edame='y'
alarm_clock=saat
while edame=='y':
    hour=int(input('Enter the hour u want to awake  between 0 and 24:'))
    minute=int(input('Enter the minuter u want to awake between 0 and 60:'))
    second=int(input('Enter the second u want to awake between 0 and 60:'))
    user_datetime =datetime(2025,8,15,hour,minute,second)
    user_time = user_datetime.time()
    user_time=str(user_time)
    print(user_time)
    if alarm_clock==user_time:
        print('it is time to wake up pls wake up')
        break
    else:
        edame = input('for continuing until the alarm_clock is saat  Enter y:')

