# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

# Test Caseler;

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class testSauce:
     
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        sleep(5)

    # def getDriver(self):
    #     self.driver=webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get("https://www.saucedemo.com/")
    #     sleep(5)
    
    #Hata mesajı alanını bir çok  yerde alacağımız için bu işlem  fonksiyonda yapıldı
    def returnErrorMesagge(self):
        errorMessage=self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']/h3")
        return errorMessage
    #Kullanıcı adı ve şifre alanları birer fonksiyonda alındı
    def returnUserName(self):
        userNameInput=self.driver.find_element(By.ID , "user-name")
        return userNameInput
    
    def returnPaswword(self):
        passwordInput =self.driver.find_element(By.ID , "password")
        return passwordInput
    
    #giriş butonu
    def loginBtnClick(self):
        self.loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        self.loginBtn.click()

    #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    # Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def enter_invalid_Control(self):
        # self.getDriver()
        testResult=self.returnErrorMesagge().text=="Epic sadface: Username is required"
        testResult2=self.returnErrorMesagge().text=="Epic sadface: Password is required"
        if testResult==True:
            print(f"Uyarı Mesajı:{self.returnErrorMesagge().text}")
        elif testResult2==True:
            print(f"Uyarı Mesajı:{self.returnErrorMesagge().text}")

     # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def lockedUserName(self):
        # self.getDriver()
        self.returnUserName().send_keys("locked_out_user")
        self.returnPaswword().send_keys("secret_sauce")
        self.loginBtnClick()
        print(f"Uyarı Mesajı:{self.returnErrorMesagge().text}")

    # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
    def xIcon(self):
        # self.getDriver()
        self.returnUserName().send_keys("")
        self.returnPaswword().send_keys("")
        self.loginBtnClick()
        #kullanıcı adı boş girildiğinde zaten istenen işlemleri site yaptığı için ekstra bir işlem yapılmamıştır.
        sleep(5)
    # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.

    def  standartUserControl(self):
        # self.getDriver()
        self.returnUserName().send_keys("standard_user")
        self.returnPaswword().send_keys("secret_sauce")
        self.loginBtnClick()
        sleep(2)
        print("/inventory.html sayfasına yönlendiriliyorsunuz.....")
        sleep(10)

    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def numberOfProduct(self):
        self.standartUserControl()
        number_products =self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        sleep(2)
        print(f"Standart kullanıcıya gösterilen toplam üyün sayısı: {len(number_products)}")
        
testSauce=testSauce()
# testSauce.enter_invalid_Control()
testSauce.lockedUserName()
# testSauce.xIcon()
# testSauce.standartUserControl()
# testSauce.numberOfProduct()
sleep(5)

while True:
    continue
       
