# Vision Transformers (ViT) Teknik Raporu

## 1. Giriş
Vision Transformer (ViT), doğal dil işleme (NLP) alanında devrim yaratan Transformer mimarisinin, görüntü işleme (Computer Vision) alanına doğrudan uyarlanmış halidir. 2020 yılında Google araştırmacıları tarafından tanıtılan bu model, geleneksel Evrişimli Sinir Ağlarına (CNN) güçlü bir alternatif olmuştur.

## 2. Çalışma Prensibi
ViT modelinin temel çalışma adımları şunlardır:

### a) Patch Extraction (Görüntüyü Yamalara Bölme)
Geleneksel CNN'ler pikselleri tek tek işlerken, ViT görüntüyü küçük kare parçalara (patch) böler. Örneğin 224x224 boyutundaki bir görüntü, 16x16 boyutunda 196 adet parçaya ayrılır.

### b) Linear Projection (Doğrusal İzdüşüm)
Elde edilen her bir 2B yama (patch), düzleştirilerek (flatten) 1B bir vektöre dönüştürülür. Daha sonra bu vektörler doğrusal bir katmandan geçirilerek sabit uzunlukta "Token"lara (tıpkı NLP'deki kelimeler gibi) dönüştürülür.

### c) Positional Embedding (Konumsal Kodlama)
Transformer mimarisi verilerin sırasını kendi başına anlayamaz. Bu yüzden her bir yamaya, görüntünün neresinden geldiğini belirten "konum bilgisi" (1, 2, 3...) eklenir.

### d) Transformer Encoder (Transformer Kodlayıcı)
Hazırlanan bu token'lar, çoklu dikkat (Multi-Head Self-Attention) mekanizmasına sahip Transformer bloklarına beslenir. Bu mekanizma, her bir yamanın diğer tüm yamalarla olan ilişkisini analiz eder (Örneğin, köpeğin kulağının olduğu yama, köpeğin kuyruğunun olduğu yama ile ilişkilendirilir).

### e) Classification Head (Sınıflandırma Başlığı)
Son olarak, tüm görüntü hakkında bilgi toplayan özel bir `[CLS]` token'ı, MLP (Çok Katmanlı Algılayıcı) katmanına gönderilir ve görüntünün sınıfı tahmin edilir (Kedi, Köpek, Araba vb.).

## 3. Avantajları ve Dezavantajları
**Avantajları:**
- Tüm görüntüye aynı anda hakim olduğu için global bağlamı CNN'lerden daha iyi anlar.
- Çok büyük veri setlerinde (Örn: JFT-300M) eğitildiğinde CNN'leri geride bırakır.

**Dezavantajları:**
- Küçük veri setlerinde CNN'ler kadar başarılı olamaz.
- Eğitim için çok fazla donanım gücü ve zaman gerektirir.
