#python&selenium yazılım geliştirme kampı 2.ödev

studentList=["fatma yıldız","ayşe tuna","sena başeğmez","ela vural"]
print(studentList)

#Öğrenci listeleme
def getAll():
    print(studentList)
def charp():
    print("-----------------------------------------------------")

#öğrenci ekleme fomksiyonu  
def studentAdd(student):
    studentList.append(student)
    print("Eklenmiş öğrenci listesi")
    getAll()
student=input("Lütfen kaydetmek istediğiniz  öğrencinin adını ve soyadını giriniz") 
studentAdd(student)
charp()
#*************************************************************************************

#öğrenci silme metodu
def studentRemove(student):
    studentList.remove(student)
    

deletestudent=input("Lütfen silmek istediğiniz öğrencinin adını ve soyadını giriniz") 
#silmek istediği öğrenciyi doğru alana kadar devam et
flag=0
while flag==0:
    if deletestudent not in studentList:
        print("Öğrenci bulunamadı")
        deletestudent=input("Lütfen silmek istediğiniz öğrencinin adını ve soyadını giriniz") 
    else:
        studentRemove(deletestudent)
        flag=1
charp()
print(f"{deletestudent}  silindi...")
getAll()
charp()

# *************************************************************************************
# çoklu öğrenci ekleme
def multiStudentAdd(array):
    students=array.split(",")
    studentList.extend(students)
   
print("Çoklu öğrenci ekleme")
charp()
student2=input("Lütfen kaydetmek istediğiniz  öğrencilerin adlarını ve soyadlarını giriniz") 
multiStudentAdd(student2)
print("çoklu öğrenci listesi")
getAll()
charp()

#*************************************************************************************
#listedeki tüm öğrencileri tek tek ekrana yazdıran ve öğrenci numarasını veren metod
def studentListing():
    print("Tüm öğrenci kayıtları:")
    i=0
    while i<len(studentList):
        print(f"{i} No'lu Öğrenci :"+studentList[i])
        i+=1
studentListing()
charp()

#*************************************************************************************
#Listeden birden fazla öğrenci silebilen metod

def multiRemove():
    flag=0

    while flag==0:
            deletestudent=input("Lütfen silmek istediğiniz öğrencinin adını ve soyadını giriniz")
            if deletestudent not in studentList:
                print("Öğrenci bulunamadı")
                flag=0
            else:
                studentRemove(deletestudent)
                print(f"{deletestudent} silindi...")
                getAll()
                flag=1
                if len(studentList)!=0:
                    want=input("Başka öğrenci silmek isterseniz lütfen 1'i silme işlemini sonlandırmak için 0'ı tuşlayınız")
                    if want=="1":
                        flag=0
                    elif want=="0":
                        flag=1
                        break
                    else:
                        print("geçersiz istek")
                else:
                    print("Listedeki tüm öğrenciler silindi")
                    getAll()
    

print("Çoklu öğrenci silme ekranı:")
charp()
multiRemove()
print("Öğrenciler silindikten sonra")
getAll()
charp()

