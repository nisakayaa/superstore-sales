
# Superstore Sales — Profitability Deep-Dive

ABD'de bir perakende zincirinin (Superstore) satış ve kâr verisi üzerinde yaptığım analiz. "Çok satıyoruz ama kâr edemiyoruz" probleminin nereden kaynaklandığını bulmaya çalıştım.

## Neden bu proje?

Sales analysis projemi yaptıktan sonra fark ettim ki **gelir != kâr**. Çok satılan bir ürün şirkete para kazandırmıyor olabilir — özellikle indirim politikaları yüzünden. Bu projede aynı veri üzerinden "satış" ve "kâr" perspektiflerini ayırıp karşılaştırdım.

## Sorduğum sorular

- Hangi ürün kategorileri kâr getiriyor, hangileri zarar?
- İndirim oranı ile kâr marjı arasındaki ilişki ne?
- Hangi bölgeler kârlı, hangileri sürekli zarar?
- En çok satan müşteriler aynı zamanda en kârlı müşteriler mi?

## Bulgular

- **Furniture** kategorisi cirosunun büyüklüğüne rağmen genelde **zarar** ediyor — özellikle "Tables" alt kategorisi
- **Technology** kategorisi en kârlı grup (kâr marjı yaklaşık %17)
- İndirim oranı **%20'yi geçtikten sonra** kâr genelde negatife dönüyor — pazarlama indirimlerinin sınırı burada
- Central bölgesi ciro olarak ikinci ama net kâr olarak son sırada → indirim politikası agresif
- En çok satın alan müşterilerin önemli bir kısmı şirkete **net zarar** ettiriyor (yüksek indirimle alıyor)

## Yöntem

1. Veriyi kategorik feature'lar üzerinden agregasyona aç
2. Her satış için **kâr marjı = profit / sales** hesapla
3. İndirim aralıklarına göre bucket'la (`0%`, `1-10%`, `11-20%`, `21%+`)
4. Bölge × kategori cross-tabulation
5. Müşteri bazında lifetime value ve net kârlılık skoru

## Kullandığım araçlar

- pandas (groupby, pivot_table burada çok işe yaradı)
- matplotlib, seaborn

## Çalıştırmak için

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/analysis.py
```

## Not

Bu projeye başlarken sales-analysis ile aynı şey olur diye düşünmüştüm. Ama profitability bambaşka bir bakış açısı — özellikle **"en iyi müşteri kim?"** sorusunun cevabı satış miktarına bakınca farklı, kâr miktarına bakınca farklı çıkıyor. İş dünyasındaki bir karar verici için "kim çok aldı?" yanlış soru, doğru soru **"kim para kazandırdı?"**.



## Author

Nisa Kaya — [github.com/nisakayaa](https://github.com/nisakayaa)
