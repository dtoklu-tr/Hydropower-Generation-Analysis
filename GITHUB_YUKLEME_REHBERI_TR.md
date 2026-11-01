# GitHub'a Yükleme Rehberi

## 1. Hesap oluşturma
1. https://github.com adresini aç.
2. Sign up seçeneğine tıkla.
3. Kişisel ve profesyonel kullanıma uygun bir kullanıcı adı belirle. Örnek: `duranalitoklu` veya `duran-toklu`.
4. E-posta doğrulamasını tamamla ve güçlü bir parola kullan.
5. İki aşamalı doğrulamayı (2FA) etkinleştirmen önerilir.

## 2. Yeni depo (repository) oluşturma
1. GitHub'a giriş yap ve sağ üstteki `+` menüsünden `New repository` seç.
2. Repository name: `hydropower-generation-analysis`
3. Description: `Python-based hydropower generation and performance analysis`
4. İlk aşamada `Public` seçebilirsin; projeyi portföyünde göstermek için uygundur. Emin değilsen `Private` seçip daha sonra görünürlüğü değiştirebilirsin.
5. `Add a README file` seçeneğini işaretleme; proje klasöründe zaten README var.
6. `Create repository` ile oluştur.

## 3. Dosyaları yükleme (başlangıç için kolay yöntem)
1. Depo sayfasında `Add file` → `Upload files` seç.
2. Bilgisayarında proje klasörünün içindeki dosya ve klasörleri seçip sürükle-bırak yap.
3. Klasör yapısının korunduğunu kontrol et.
4. Commit message alanına `Initial project structure and technical report` yaz.
5. `Commit changes` ile yüklemeyi tamamla.

## 4. Önerilen son depo yapısı
```text
hydropower-generation-analysis/
├── README.md
├── src/
│   └── hydropower_analysis.py
├── notebooks/
│   └── Hydropower_Generation_Analysis.ipynb
├── data/
│   └── assumed_monthly_flows.csv
├── results/
│   ├── monthly_energy_results.csv
│   ├── design_sweep_results.csv
│   └── top_10_designs.csv
├── figures/
│   ├── monthly_energy.png
│   └── design_sweep_heatmap.png
└── docs/
    ├── Hidroelektrik_Teknik_Rapor_TR_4-6_Sayfa.pdf
    └── Hidroelektrik_Teknik_Rapor_TR_4-6_Sayfa.docx
```

## 5. Dikkat
- Gerçek santral verisi olmadığını README ve raporda açıkça belirt.
- HydroGenerate ile sayısal karşılaştırmayı doğrulamadan tamamlandı olarak yazma.
- E-posta, parola, API anahtarı veya kişisel/kurumsal gizli veri yükleme.
- Büyük ve gereksiz dosyaları (ör. geçici çıktılar) depoya ekleme.
