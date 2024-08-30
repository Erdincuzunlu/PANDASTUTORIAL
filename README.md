# PANDASTUTORIAL
# Titanic Veri Seti Analizi

Bu proje, Titanic veri setini kullanarak çeşitli veri analizleri ve işlemeleri gerçekleştirir. Kapsadığı işlemler arasında veri yükleme, temizleme, seçim, standartlaştırma, gruplama ve pivot tablosu oluşturma yer alır. Ayrıca, veri setindeki eksik değerler ve kategorik değişkenler üzerinde işlem yapma örnekleri de sunulmuştur.

## Özellikler
- Titanic veri setini yükler ve inceler.
- Eksik değerleri kontrol eder ve temizler.
- Veri seçimi ve işleme yapar.
- Veriyi standartlaştırır ve pivot tablosu oluşturur.

## Gereksinimler
- pandas
- seaborn
- numpy

- # Titanic Veri Seti Analizi

Bu proje, Titanic veri setini analiz etmek ve bazı temel veri işleme tekniklerini uygulamak için kullanılmıştır. Aşağıda kullanılan kod parçacıkları ve açıklamaları bulunmaktadır.

## Veriyi Yükleme ve İnceleme

```python
import pandas as pd
import seaborn as sns

# Titanic veri setini yükleyin
df = sns.load_dataset("titanic")

# İlk birkaç satırı görüntüleyin
df.head()

# Son birkaç satırı görüntüleyin
df.tail()

# DataFrame'in şekli
df.shape

# DataFrame hakkında bilgi
df.info()

# Kolon isimleri
df.columns

# İndeks
df.index

# İstatistiksel özet
df.describe().T

# Eksik değerler
df.isnull().values.any()  # En az bir eksik değer var mı?
df.isnull().sum()  # Eksik değerlerin sayısını gösterir

# Belirli bir aralıkta seçme işlemi
df[0:13]

# Satır silme işlemi
df.drop(0, axis=0).head()

# Birden fazla satır silme
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head()

# Değişkeni indeks olarak ayarlama
df.index = df["age"]
df.drop("age", axis=1, inplace=True)

# İndeksi değişkene dönüştürme
df["age"] = df.index
df.drop("age", axis=1, inplace=True)
df.reset_index().head()

# Veri işlemlerine örnekler
df["age2"] = df["age"] ** 2
df["age3"] = df["age"] / df["age2"]

# Belirli bir string ifadesi içermeyen sütunları seçme
df.loc[:, ~df.columns.str.contains("age")].head()

# Koşullu seçim
df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()
df.loc[df["age"] > 50, ["class", "age"]].head()

# Standartlaştırma
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# Pivot tablosu
df.pivot_table("survived", "sex", "embarked")

import numpy as np

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

# DataFrame'leri birleştirme
pd.concat([df1, df2], ignore_index=True)

4. Yapılan değişiklikleri kaydedin ve `Commit changes` düğmesine tıklayın.

### 4. Kodları GitHub’a Yükleme

Kodlarınızı doğrudan GitHub'a yüklemek için şu adımları izleyin:

1. Bilgisayarınızda bir klasör oluşturun ve bu klasörde kodlarınızı `.py` uzantılı dosyalar olarak kaydedin.
2. Git komutları kullanarak bu dosyaları GitHub deposuna ekleyebilirsiniz:

   ```bash
   git init
   git add .
   git commit -m "Add initial code"
   git branch -M main
   git remote add origin <repository-url>
   git push -u origin main
