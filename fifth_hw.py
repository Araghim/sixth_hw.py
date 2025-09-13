import logging
logging.basicConfig(filename='fifth_hw.log',level=0)
logger=logging.getLogger()
# #tamrin 1
# try:
#     f=open("artificial_intelligence.txt","w",encoding="utf-8")
# except FileNotFoundError as e:
#     logger.log(msg='The file "artificial_intelligence.txt" was not found.',level=40)
#     print(e)
#
# logger.log(msg='crating file',level=20)
# artificial_intelligence_text="""هوش مصنوعی در سال های اخیر رشد چشمگیری داشته است.طبق گزارش ها,بازار جهانی هوش مصنوعی در سال
# 2023 بیش از 120 میلیارد دلار ارزش گزاری شده است و پیشبینی میشود تا سال 2030 به بیش از 500 میلیارد دلار برسد.
# مقالات علمی منتشر شده در حوزه هوش مصنوعی در سال 2022 تقریبا 150 هزار دلار بوده که نسبت به سال 2010,رشد بیش از 500 درصدی را نشان میدهد.
#  یکی از مهمترین الگوریتم های هوش مصنوعی شبکه های عصبی عمیق هستند که از میلیون ها پارامتر برای یادگیری استفاده میکنند. به عنوان مثال ,
#  مدل GPT-4 که بر پایه 175 میلیارد پارامتر ساخته شده است توانایی تولید متن هایی
#  با کیفیت انسان را  دارد.همچنین, سرعت پردازش داده ها در این مدل به بیش از 10 ترافلا پس (10*12 عملیات در ثانیه) میرسد
#  هوش مصنوعی در حوزه های م مختلفی مانند پزشکی,خودروسازی, مالی و تولید محتوا کاربرد دارد به طور مثال,در
#  پزشکی سیستم های تشخیص بیماری با دقت بیش از 95 درصد توانسته اند به کمک پزشکان بیایند. در صنعت خودرو,
#  حدود 80 درصد خودرو های جدید مجهز به فناوری های هوش مصنوعی برای رانندگی نیمه خودکار هستند."""
# f.writelines(artificial_intelligence_text)
# logger.log(msg='writing the artificial_intelligence_text in my file',level=20)
# amount_of_numbers=0
# for words in artificial_intelligence_text:
#         if words.isnumeric():
#                        amount_of_numbers+=1
#         f.close()
# amount of my numbers ch in my file
# print(amount_of_numbers)





# tamrin 2
# mass_of_object=float(input("Enter the mass of the object in kilograms: "))
# height_of_object=float(input("Enter the height of the object in meters: "))
# g=9.8
# def gravity(m:float,h:float) -> float:
#     U=m*g*h
#     logger.log(msg='the info of function ',level=20)
#     return U
# print(gravity(mass_of_object,height_of_object))
#tamrin 3
import os
# creating directory file
try:
    os.makedirs('baba benazam',exist_ok=True)
    logger.log(msg='the folder mahdi has been created with no problem',level=20)
except FileExistsError as e:
    print(e)
    logger.log(msg='there is an Error that you forgot to fix',level=40)
for i in range(1,101):
# adding my files to my directory with path  ادرس اون فایل میشه path
    path=os.path.join('mahdi',f'file_{i}.txt')
    f=open(file=path,mode='w')
    f.write('')
    f.close()






