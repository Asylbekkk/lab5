"""
#Резюме
print("                      Резюме            ")
fio = "Ф.И.О : Рахманберді Асылбек Талғатұлы"
date_of_birth = "Дата рождения : 25.09.2002"
obrazovanie = "Образование : Satbayev University"
print(fio)
print(date_of_birth)
obrazovanie = {
    'ВУЗ': 'Satbayev University',
    'Специальность ': 'Computer Science',
    'GPA': '2,9',
    'Год окончания ': '2023'
}
for x, y in obrazovanie.items():
    print(x + ' : ' + y)

skills = ['Языки программирования Python', 'Django', 'HTML,CSS']
for x in skills:
    print("\tОсновные навыки : " + x)

info = []
info.append("Номер телефона : ")
info.append("Эл.почта : ")
print(info[0] + '87026565747')
print(info[1] + 'arakhmanberdy@gmail.com')
print("Цель : " + "Получить работу программист-стажер")
"""

"""


#1.Бағдарламалау секцияларына қатысатын әртүрлі топтағы студенттерді таныстыруды сұрайтын бағдарламаны жазыңыз.
# Тізімді сыныптардың өсу реті бойынша сұрыптау қажет. Фамилиялар мен сыныптардың тізімін басып шығарыңыз.
d = {}
n = int(input('Студенттердің санын енгізіңіз :  '))
# создаем пустой лист
# информациия о студенте
list = []
for i in range(0, n):
	# split
	x,y = input("Студенттің аты - жөні және бағасы : ").split()
	#  x - имя , y - балл
	list.append((y,x))
  #сортировка по баллу
list = sorted(list, reverse = False)

print('Өсу реті бойынша өңделген тізім : ')

for i in list:
	print(i[1], i[0])
"""
"""




# Добавление оценки студента по предметам и вывод журнала по имени
def addStudent():
  a = int(input("Хотите добавить оценку по предмету для ученика  ? 1 - ДА / 2 - НЕТ "))
  if(a==1):    
    studentName = input("Введите имя студента : ")
    studentSubject = input("Введите предмет студента : ")
    studentGrade = int(input("ВВедите оценку по этому предмету : "))
    list.append([studentName,studentSubject,studentGrade])
    addStudent()
  else:
    showList()

def showList():
  a = input("Введите имя студента : ")
  for i in list:
    if(i[0]==a):
      print(i[1] + " : "+ str(i[2]))

list = []
i = int(input("Что хотите сделать? Добавить оценку - 1 | Посмотреть журнал -2 : "))
if(i==1):
  addStudent()
elif(i==2):
  showList()
else:
  print("Извините я на такую команду не запрограммирован !")
"""


"""
'''Для выигрыша главного приза необходимо, чтобы шесть
номеров на лотерейном билете совпали с шестью числами,
 выпавшими случайным образом в диапазоне от 1 до 49 во время очередного тиража.
  Напишите программу, которая будет
  случайным образом подбирать шесть номеров для вашего билета.
Убедитесь в том, что среди этих чисел не будет дубликатов.
 Выведите номера билетов на экран по возрастанию.'''

from random import shuffle

arr = [*range(1, 50)]
shuffle(arr)
print(sorted(arr[:6]))
"""
"""



# task
a = [["Asylbek", 100],
     ["Abzal", 95]]
name = input("name:")
for i in range(len(a)):
    for j in range(len(a)):
        if name == a[i][0]:
            print(a[i][0], ":", a[i][1])
            break
        else:
            print("Student jok!")
            break
          """
          
"""          
#task
a = ["Asylbek", "Abzal"]
course = ["python", "SQL"]
a.sort()
print(a)
course.sort()
print(course)    
"""     
  
