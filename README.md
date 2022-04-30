# Data Structures And Algorithms
## Veri Yapıları ve Algoritmalar Ödevleri

1. Insertion Sort (Sokma Sıralaması)

    - Araya Sokarak Sıralama yapılır
    - Türkçe Araya Sokma Sıralaması olarakta adlandırılır
    - Kaydırma işlemi yapılır
    - Doğrusal (Linear) yapıdadır
    - Worst Case senaryoda Big-O Notasyonu büyüme faktörü olarak $n^2$ ye gider (O($n^2$))
    - Küçükten büyüğe sıralama yapılır
    - Dizinin indeksi 0'dan başladığı kabul edilirse 1.indeksteki eleman key olarak seçilir



2. Merge Sort (Birleştirme Sıralaması)
    - Böl (Divide) ve İşini Hallet(Conqueror)
    - Doğrusal (Linear) değildir.
    - Big-O notasyonu worst case'te zaman karmaşılığı O(nlogn)'e gider
    - Az sayıda elamanı olan dizilerde hız fark edilmez ama milyonlu sayılarda hızı fark edilicektir.
    - İlk aşamada dizi elamanları bölme işlemine tabi tutularak en küçük 1 elemanlı dizilere bölünür.
    - İkinci aşamada 1 elamanlı diziler sıralanarak 2 elamanlı dizilere 2 elemanlı diziler 4 elemanlı dizlilere şeklinde devam edilir. (Dizi eleman sayısı çift ise bu şekilde olur tek ise bir tarafta 4 elamanlı diğer tarafta 3 elemanlı dizi olabilir)

