# Insertion Sort

## array = [22,27,16,2,18,6]

##### 1.Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

> ## 1.Adım
> 
> | Array Elements: | 22  | <u>**27**</u> | 16  | 2   | 18  | 6   |
> | --------------- | --- | ------------- | --- | --- | --- | --- |
> | Array Index :   | 0   | <u>**1**</u>  | 2   | 3   | 4   | 5   |
> 
> **key = array[1] >>** **key=27**
> 
> array'in 1.index'i key seçilir. key değeri 27 seçildiğinde dizinin solunda 22, sağında key değeri dahil 27,16,2,18,6 değerleri kalır. Dizinin sol tarafı tek elemanlı olduğu için dizinin solu sıralı kabul edilir.
> Dizinin solunda key değerinden büyük bir sayı var ise bu büyük sayı sağa kaydırılır (Temel Mantık). Bu kaydırma işleminde key değeri sola doğru gider. key değerine eşit veya ondan küçük bir değer görene kadar devam eder. key değerinden büyük sayılar hep sağa doğru kayar.
> key = 27 değeri solundaki 22 ile karşılaştırılır. key = 27  22'den büyük olmadığı için bir işlem yapılmaz. 22 sayısının solunda bir sayı olamdığı için bir sonraki adıma geçilir.Array bu adımdaki hali **array = [22,27,16,2,18,6]** şeklinde olduğu gibi kalır.
> 
> 1.Adım sonunda array'in son hali
> 
> | Array Elements: | 22  | 27  | 16  | 2   | 18  | 6   |
> | --------------- | --- | --- | --- | --- | --- | --- |
> | Array Index:    | 0   | 1   | 2   | 3   | 4   | 5   |
> 
> Bir sonraki adımda key'in index değeri bir arttırlır.

> ## 2.Adım
> 
> | Array Elements: | 22  | 27  | <u>**16**</u> | 2   | 18  | 6   |
> | --------------- |:--- | --- | ------------- | --- | --- | --- |
> | Array Index :   | 0   | 1   | **<u>2</u>**  | 3   | 4   | 5   |
> 
> **key = array[2] >>** **key=16**
> 
> key = array[1] = 27'den key = array[2] = 16 olur. Bu adımda key'in index değeri 1 arttırılmış olur. key'in solunda kalan sayılar ile key değeri tek tek karşılaştrılır. key = 16 ile 27 karşılaştırılır. 27 key=16 değerinden büyük olduğu için 27'i bir index sağa kaydırılır. Hemen ardından key = 16 değeri 22 ile karşılaştırılır. 22 değeri key=16'dan büyük olduğu için 22 değeri bir index sağa kaydırılır. Bu adımda **array = [16,22,27,2,18,6]** halini almış olur
> 
> 2.Adım sonunda array'in son hali
> 
> | Array Elements: | 16  | 22  | 27  | 2   | 18  | 6   |
> | --------------- |:--- | --- | --- | --- | --- | --- |
> | Array Index :   | 0   | 1   | 2   | 3   | 4   | 5   |
> 
> Bir sonraki adımda key'in index değeri bir arttırlır.

> ## 3.Adım
> 
> | Array Elements: | 16  | 22  | 27  | <u>**2**</u> | 18  | 6   |
> | --------------- | --- | --- | --- | ------------ | --- | --- |
> | Array Index :   | 0   | 1   | 2   | **<u>3</u>** | 4   | 5   |
> 
> **key = array[3] >>** **key=2**
> 
> key = array[2] = 16'den key = array[3] = 2 olur. Bu adımda key'in index değeri 1 arttırılmış olur. key'in solunda kalan sayılar ile key değeri tek tek karşılaştrılır. key = 2 ile 27 karşılaştırılır. 27 key=2 değerinden büyük olduğu için 27'i bir index sağa kaydırılır. Hemen ardından key = 2 değeri 22 ile karşılaştırılır. 22 değeri key=2'den büyük olduğu için 22 değeri bir index sağa kaydırılır. 16 değeri key=2 değerinden büyük olduğu için 16'ı bir index sağa kaydırılır. Bu adımda **array = [2,16,22,27,18,6]** halini almış olur
> 
> 3.Adım sonunda array'in son hali
> 
> | Array Elements: | 2   | 16  | 22  | 27  | 18  | 6   |
> | --------------- |:--- | --- | --- | --- | --- | --- |
> | Array Index :   | 0   | 1   | 2   | 3   | 4   | 5   |
> 
> Bir sonraki adımda key'in index değeri bir arttırlır.

> ## 4.Adım
> 
> | Array Elements: | 2   | 16  | 22  | 27  | <u>**18**</u> | 6   |
> | --------------- | --- | --- | --- | --- | ------------- | --- |
> | Array Index :   | 0   | 1   | 2   | 3   | <u>**4**</u>  | 5   |
> 
> **key = array[4] >>** **key=18**
> 
> key = array[3] = 2'den key = array[4] = 18 olur. Bu adımda key'in index değeri 1 arttırılmış olur. key'in solunda kalan sayılar ile key değeri tek tek karşılaştrılır. key = 18 ile 27 karşılaştırılır. 27 key=18 değerinden büyük olduğu için 27'i bir index sağa kaydırılır. Hemen ardından key = 18 değeri 22 ile karşılaştırılır. 22 değeri key=18'den büyük olduğu için 22 değeri bir index sağa kaydırılır. 16 değeri key = 18 değerinden küçük olduğu için 16'nın hemen peşine key=18 yerleşir. 16'dan öncesi küçükten büyüğe sıralı kabul edildiğinden daha sol ile karşılaştırlma yapılmaz. Bu adımda **array = [2,16,18,22,27,6]** halini almış olur
> 
> 4.Adım sonunda array'in son hali
> 
> | Array Elements: | 2   | 16  | 18  | 22  | 27  | 6   |
> | --------------- |:--- | --- | --- | --- | --- | --- |
> | Array Index :   | 0   | 1   | 2   | 3   | 4   | 5   |
> 
> Bir sonraki adımda key'in index değeri bir arttırlır.

> ## 5.Adım
> 
> | Array Elements: | 2   | 16  | 18  | 22  | 27  | <u>**6**</u> |
> | --------------- | --- | --- | --- | --- | --- | ------------ |
> | Array Index :   | 0   | 1   | 2   | 3   | 4   | <u>**5**</u> |
> 
> **key = array[5] >>** **key=6**
> 
> key = array[4] = 18'den key = array[5] = 6 olur. Bu adımda key'in index değeri 1 arttırılmış olur. key'in solunda kalan sayılar ile key değeri tek tek karşılaştrılır. key = 6 ile 27 karşılaştırılır. 27 key=6 değerinden büyük olduğu için 27'i bir index sağa kaydırılır. Hemen ardından key = 6 değeri 22 ile karşılaştırılır. 22 değeri key = 6'dan büyük olduğu için 22 değeri bir index sağa kaydırılır. 18 ile key = 6 karşılaştırılır.18 key = 6'dan büyük olduğu için 18 bir index sağa kaydırılır. 16 ile key = 6 karşılaştırılır. 16'ı key = 6'dan büyük olduğu için 16'ı bir index sağa kaydırılır. 2 ile key = 6 karşılaştırılır. 2 key = 6'dan büyük olmadığı için hemen peşine yerleşir. 2 ve 2'den öncesi küçükten büyüğe sıralı kabul edildiğinden daha sol ile karşılaştırlma tekrar yapılmaz. Bu adımda **array = [2,6,16,18,22,27]** halini almış olur.
> 
> 4.Adım sonunda array'in son hali
> 
> | Array Elements: | 2   | 6   | 16  | 18  | 22  | 27  |
> | --------------- |:--- | --- | --- | --- | --- | --- |
> | Array Index :   | 0   | 1   | 2   | 3   | 4   | 5   |
> 
> array sıralanmış olur ve işlem biter.

##### 2. Big-O gösterimini yazınız.

> Listede 6 eleman var, bu elemanlar key değeri alırken 5 kez üzerlerinde döndük.  Her key değeri üzerinde işlem yaparken sola doğru key değerlerinide ayrı olarak karşılaştırdık ve kaydırmalar yaptık.  Aslında burada key'in index değeri her adımda bir artırılması için, öncelikle o key üzerindeyken iç tarafatada ayrı olarak sola doğru sayıların üzerinden geçiyoruz. Bu durum Nested (İç içe) For döngüsüne benziyor. Dıştaki For n dönerken içteki For da belli bir miktar dönüyor. Bu bizi büyükten küçüğe dizilmiş listede bu wors case senaryo olur n*n 'e götütür. Aşağıdaki Python kodunda n1'in her değeri için n2 3 kere dönüyör. n<sup>2</sup>=3x3 olmuş oluyor. Birnevi buna benziyor. İçteki For döngüsü while döngüsüde oalbilir. Bu size kalmış. 
> 
> ```python
> for n1 in range(1,4):   
>     for n2 in range(1,4):
>         print ("n1:",n1,"n2:",n2)
>     print()
>     
> """ Output:
> n1: 1 n2: 1
> n1: 1 n2: 2
> n1: 1 n2: 3
> 
> n1: 2 n2: 1
> n1: 2 n2: 2
> n1: 2 n2: 3
> 
> n1: 3 n2: 1
> n1: 3 n2: 2
> n1: 3 n2: 3 """
> ```

3.Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.

> Liste sıralanmadan Linear Search işlemine göre;
> 
> - Best Case: 22
> 
> - Avarage Case: 16,2
> 
> - Worst Case: 6
> 
> şeklinde olucaktır.

4.Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız

>     Avarage Case: 18 olur çünkü aradığımız sayı oratalarda olmuş olur. 
