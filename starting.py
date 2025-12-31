#kendisine parametre olarak gelen bir sayının faktöriyelini alan ve sonucunu ekrana ayzdıran Python kodunu yazınız.

def factorial(num):
    faktoriel = 1
    for i in range(1, num+1):
        faktoriel= faktoriel*i
    print("The factorial is: ",faktoriel)
#factorial(3)

#kullanıcıdan girilen sayının üssünü alan Python fonksiyonunu yazınız.
def power():
    base=int(input(f"Enter number to be exponented "))
    power=int(input(f"Enter number for degree of exponent"))
    result=1 #as beginning
    for i in range(power):
        result=base*result

    print("Result of exponential expression is ",result)    

#power()
#kullanicidan sayi girilmesi istenecek,eger sayi negatifse kullanicidan yeniden giriş talep edilecek,pozitifse girilen sayılar toplqanacaktır.
def isPositiveNumber():
    total=0
    while True:
        number=int(input(f"Enter any number:"))
        if(number<0):
            print("Please enter positive integer ! ")
        else:
            total=number+total
            print("Total of all positive numbers is: ",total)
            break
#isPositiveNumber()
#klavyeden girilen sayinin 1'den n'e kadar olan sayilardan sadece çift olanlarını ekrana yazan program.

def evenNumbers():
    n=int(input(f"Enter a positive number: "))
    for i in range(1,n+1):
        if(i%2==0):
            print("Even numbers are",i)
#evenNumbers() 

#Dizi tanımlama
mylist =[1,3,4,5]

#diziye eleman ekleme
mylist.append(7)


#diziden eleman çıkarma
mylist.remove(3)

#dizi uzunluğu
diziuzunlugu =len(mylist)
print(diziuzunlugu)

#dizinin elemanlarına erişim
#print(mylist[1])

#kendisine parametre olarak gelen diziyi büyükten küçüğe sıralayan bir Python fonksiyonu yazınız.

def SortList(array1):
    array1.sort(reverse=True)
    print(array1)
#SortList([43,13,23,11,3,9,1])

#Her öğrencinin bilgilerini tuple içinde tut,bu bilgileri dictionary içinde organize et.
student1 = ("Mehmet","123475","Software Engineering")
student2 = ("Pınar","233474534","Computer Engineering")
student3 = ("Tuna","84567546","Information Systems Engineering")

students = {
    101: student1,
    102: student2,
    103: student3
}

def studentInformation(studentID):
    if studentID in students:
        student=students[studentID]
        print(f"{student[2]}")

studentInformation(101)

