#  Создать учет принятых и уволенных работников. Выдать общий список когла-либо работающих,
# с датами рождения, список только работающих без уволенных, определить списочную численность.
import calendar

i=0
sp_in={}
sp_out={}
#while True:

def in_ch():
    ch = int(input("число  "))
    if ch > 31:
        print("Неверный ввод")
        ch = int(input(" повторите число  "))
    return ch
def in_month():
    mm = int(input('месяц  '))
    if mm > 12:
        print("Неверный ввод")
        mm = int(input('повторите месяц  '))
    return mm
def in_year():
    yy = int(input("год  "))
    if yy > 2022:
        print("Неверный ввод")
        yy = int(input("повторите год  "))
    return yy
def of_month(mm, yy):
    import calendar
    print(calendar.month(themonth=mm, theyear=yy))
   
y=1
while y!=9:
    y=int(input('Внести данные о принятых работниках - нажмите 1,\n если об уволенных - 0,\n посмотреть календарь сегодняшнего месяца - 2,\n выход -9:\n  '))
    if y==1:
        print('Введите анкетные данные:')
        FIO = input("Введите фамилию, имя, отчество полностью  ")
        print("Дата рождения:__/__/____")

        ch=in_ch()
        mm=in_month()
        yy=in_year()
        print(ch, mm, yy)
        sp_in[FIO]=[ch, mm, yy]
        print('Список принятых: ', sp_in, '\n')
        i+=1
    elif y==0:
        print('Введите анкетные данные:')
        FIO = input("Введите фамилию, имя, отчество полностью  ")
        print("Дата рождения:__/__/____")

        ch = in_ch()
        mm = in_month()
        yy = in_year()

        sp_out[FIO] = [ch, mm, yy]
        print('Список уволенных: ',sp_out, '\n')
        i += 1
    elif y==2:
        # in_ch()
        ch = in_ch()
        mm = in_month()
        yy = in_year()
        of_month(mm, yy)

else:
    print('Конец работы')
#print(sp_in.items())
#print(sp_out.items())
#for key in sp_out:
print('Принятые (Дни рождения) ', sp_in)
d_in=set(sp_in.keys())
print('Уволенные (Дни рождения) ', sp_out)
d_out=set(sp_out.keys())
print("Список принятых", d_in)
print("Список уволенных", d_out)
d=d_in|d_out
print("Общий список когда-либо работающих", d)
S=d_in-d_out
print("Cписок работающих", S)
print("Списочная численность на сегодня", len(S))