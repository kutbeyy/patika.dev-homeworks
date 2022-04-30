

def merge_sort(dizi: list) -> None:
    # Divide(Parçalama) Aşaması
    if len(dizi) > 1:
        ortancaIndex = len(dizi)//2
        solDizi = dizi[:ortancaIndex]
        sagDizi = dizi[ortancaIndex:]

    # Reküsif olarak fonksiyonu kendi içinde çağrıyoruz
        merge_sort(solDizi)
        merge_sort(sagDizi)

    # Çünkü üsteki if şartı ile reküsif döngüyü liste uzunlukları 1 e gelene kadar devam ettirip 1
    # dizinin her helemanının tekli tekli ayrı listeler haline dönüşmesini sağlıyoruz. len(dizi)=1
    # olduğunda if bloğuna girilmeyecek.

    # Burdada parçalanan dizileri birşeltiriyoruz
        merge_the_lists(tempDizi=dizi, solDizi=solDizi, sagDizi=sagDizi)


def merge_the_lists(tempDizi: list, solDizi: list, sagDizi: list) -> None:
    k = 0  # her parçalı listeyi birleştirirken geçiçi bir tempDizi oluşturuyoruz onun üzerinde gezici pointer
    i = 0
    j = 0
    while i < len(solDizi) and j < len(sagDizi):
        if solDizi[i] < sagDizi[j]:
            tempDizi[k] = solDizi[i]
            i = i+1
        else:
            tempDizi[k] = sagDizi[j]
            j = j+1
        k = k+1

    # Aşağıdaki kısım birleştirme esnasında bir dizide eleman bitti diğer dizide eleman kaldı
    # Kalan elemanlar sıralı olduğu için direk listenin sonuna eklemek için yapıyoruz.
    while i < len(solDizi):
        tempDizi[k] = solDizi[i]
        i = i+1
        k = k+1
    while j < len(sagDizi):
        tempDizi[k] = sagDizi[j]
        j = j+1
        k = k+1


unsortedArray = [88, 99, 44, -121, -1, 0, 0, -1, 15.6, 9, 777, -444]

merge_sort(unsortedArray)
print(unsortedArray)
