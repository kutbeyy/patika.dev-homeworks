# 

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
> 
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
> 
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
> 
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
> 
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
> 
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