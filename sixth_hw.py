import logging
import os
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(filename='logging',level=0)
logger=logging.getLogger()
# ATM program
given_password = input('Enter ur password:')
def atm(keys:int) -> None:
    mojodi=100
    edame = 'c'
    user_Password=os.getenv('PASSWORD')
    global given_password
    logger.info(f'Mojodi={mojodi},password={given_password}')
    if user_Password==given_password:
        logger.log(msg='Password matches',level=20)
    else:
        return "Password doesn't match try again"
    while edame=='c':
        if keys==1:
            print(mojodi)
        elif keys==2:
                    variz=int(input('enter the amount u want to variz:'))
                    mojodi+=variz
                    print(mojodi)
        elif keys==3:
                bardash=int(input('enter the amount u want to bardash:'))
                mojodi-=bardash
                print(mojodi)
        else:
            try:
                  exit=input('press continue for exiting ATM:')
                  if exit=='continue':
                      break
            except Exception as e:
                print(e)
                logger.log(msg='the programme has this Error fix it',level=40)
        logger.log(msg='checking if user want to continue using ATM',level=20)
        edame = input("enter c for continuing and e for exit:")
        if edame=='c':
            logger.log(msg='enter c for continuing and e for exit',level=20)
            keys=int(input("enter keys for continuing if u want:"))
        else:
            break
    return None
print(atm(keys=int(input("enter keys  from 1 to 4 1|for see ur mojodi 2|for variz to ur bank account 3|for bardash 4|for exit : ")))) # we write keys so we know what is our input
# tamrin 2

def biggest_number_(list_numbers:list) -> int:
    for i in  range(0,len(list_numbers)):
        # logger.info(list_numbers[i])
        logger.log(msg=list_numbers[i],level=20)
        if list_numbers[i]>=list_numbers[0] and list_numbers[i]>=list_numbers[1] and list_numbers[i]>=list_numbers[2] and list_numbers[i]>=list_numbers[3]:
            return list_numbers[i]
# this function only works for list with 4 members
print(biggest_number_(list_numbers=[1,2,77,9]))
