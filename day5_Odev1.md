Decorator Nedir?
Dekoratör(Armatür olarak da bilinir.), Python'da kullanıcının yapısını değiştirmeden mevcut bir nesneye yeni işlevler eklemesine izin veren bir tasarım desenidir. Dekoratörler genellikle dekore etmek istediğiniz bir fonksiyonun tanımından önce çağrılır.
Dekoratörler, doğrudan alt sınıfları kullanmak veya dekore edilen fonksiyonun kaynak kodunu değiştirmek zorunda kalmadan bir fonksiyonun, yöntemin veya sınıfın işlevselliğini dinamik olarak değiştirir. Python'da dekoratörleri kullanmak, kodunuzun DRY(Don't Repeat Yourself-Kendinizi Tekrar Etmeyin) olmasını da sağlar. 

Decore etmek istediğimiz fonsiyondan önce @ sembolü kullanırız
Bir cümleyi büyük harfe çevirecek basit bir dekoratör oluşturalım.
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

Dekoratör fonksiyonumuz bir fonksiyonu argüman olarak alır ve bu nedenle bir fonksiyon tanımlayıp dekoratörümüze ileteceğiz.
@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()

Pytest Decorators:Şimdide PyTestdeki decoratorleri konuşalım.

#pytest.fixture
@pytest.fixture
dekoratörünün amacı, bir fonksiyonu diğer test fonksiyonları veya fikstürler tarafından kullanılabilmesi için bir fikstür olarak işaretlemektir. Bir test işlevi, bir fikstür işlevini parametre olarak belirtirse, pytest otomatik olarak bu işlevi çağırır ve dönüş değerini test işlevi için bir argüman olarak kullanır.

@pytest.mark.parametrize
dekoratörü, bir test işlevi için bağımsız değişkenlerin parametrelendirilmesini sağlar. Selenium test otomasyonu farklı giriş kombinasyonlarında yürütülebildiğinden, bu dekoratörü kullanarak test için veriye dayalı bir yaklaşım kullanabiliriz.

Giriş değerlerini iletmek için @pytest.mark.parametrize dekoratörü şu şekilde kullanılabilir:
@pytest.mark.parametrize("input_arg_1, input_arg_2,...,input_arg_n",
                         [("input_val_1", "input_val_2",...,"input_val_n")])

@pytest.mark.filterwarnings
Belirli test öğelerine uyarı filtreleri eklemek için @pytest.mark.filterwarnings'i kullanabilirsiniz; bu, test, sınıf ve hatta modül düzeyinde hangi uyarıların yakalanması gerektiğini daha iyi kontrol etmenizi sağlar:


@pytest.mark.skip 
Bir test işlevini koşulsuz olarak atlamaya imkan verir.
     @pytest.mark.skip(reason="bu fonksiyon atlanıcak")
     def test_the_unknown():

@pytest.mark.skipif 
Koşullu olarak bir şeyi atlamak istiyorsanız bunun yerine skif'i kullanabilirsiniz.Python3.10'dan önceki bir yorumlayıcıda çalıştırıldığında atlanacak bir test işlevi  örneği
    @pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
    def test_function():

@pytest.mark.xfail
def test_function():
Bir testin başarısız olmasını beklediğinizi belirtmek için kullanılır.Bu test çalışacak, ancak başarısız olduğunda geri izleme bildirilmeyecek. XFAILBunun yerine, terminal raporlaması bunu "başarısız olması bekleniyor" ( ) veya "beklenmedik bir şekilde başarılı" ( XPASS) bölümlerinde listeleyecektir .

#Bu konu hakkında detaylı bilgi için kullandığım kaynak https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-mark-filterwarnings

