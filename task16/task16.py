
"""
GÖREV 16: CNN (Convolutional Neural Networks) Mimarisi Nedir?

CNN (Evrişimli Sinir Ağları), görsel verileri analiz etmek için kullanılan en yaygın derin öğrenme mimarisidir. 
Özellikle nesne tanıma, görüntü sınıflandırma ve tıbbi görüntüleme gibi alanlarda devrim yaratmıştır. 

CNN Mimarisinin Temel Bileşenleri:

1. Convolutional Layer (Evrişim Katmanı): 
   Görüntü üzerindeki pikselleri filtreler yardımıyla tarayarak kenarlar, köşeler ve dokular gibi 
   önemli özellikleri (features) öğrenir.

2. Activation Function (ReLU): 
   Genellikle evrişim katmanından sonra kullanılır. Negatif değerleri sıfıra indirerek 
   modele doğrusal olmayan (non-linear) bir özellik kazandırır.

3. Pooling Layer (Havuzlama Katmanı): 
   Görüntünün boyutunu küçültür. Bu, hesaplama maliyetini düşürür ve modelin aşırı öğrenmesini (overfitting) engeller. 
   En yaygın kullanılan yöntem "Max Pooling"dir.

4. Fully Connected Layer (Tam Bağlantılı Katman): 
   Özniteliklerin toplandığı ve sınıflandırma kararının verildiği son aşamadır. 
   Burada her nöron bir önceki katmandaki tüm nöronlara bağlıdır.

5. Softmax/Sigmoid Layer: 
   Modelin tahminlerini olasılık değerlerine (0 ile 1 arası) dönüştüren çıkış katmanıdır.
"""
