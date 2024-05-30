# Cryptocurrency Price Prediction

Bu proje, Bitcoin gibi kripto para birimlerinin gelecekteki fiyatlarını tahmin etmek için bir makine öğrenmesi modelini kullanır. Proje, geçmiş fiyat verilerini kullanarak gelecekteki fiyat hareketlerini tahmin etmek amacıyla zaman serisi analizine dayanmaktadır.

## Özellikler

- Geçmiş kripto para birimi fiyat verilerini çekme ve ön işleme
- LSTM modeli kullanarak fiyat tahmini yapma
- Tahmin sonuçlarını görselleştirme
- Model performans metriklerini hesaplama

## Kullanılan Teknolojiler

- Python
- TensorFlow/Keras
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn

## Kurulum

### Gereksinimler

- Python 3.7 veya daha yeni bir sürüm
- Anaconda (tavsiye edilir)

### Adımlar

1. Depoyu klonlayın:
    ```sh
    git clone https://github.com/fuatorium/cryptocurrency-price-prediction.git
    cd cryptocurrency-price-prediction
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```sh
    conda create --name crypto-prediction-env python=3.8
    conda activate crypto-prediction-env
    pip install -r requirements.txt
    ```

3. `data_collector.py`, `data_preprocessor.py`, `model.py` ve `predictor.py` dosyalarını inceleyerek ve düzenleyerek gerekli değişiklikleri yapın.

## Kullanım

1. `main.py` dosyasını çalıştırarak modeli eğitin ve tahmin yapın:
    ```sh
    python main.py
    ```

2. Sonuçlar, eğitim ve test sırasında oluşturulan grafiklerde görselleştirilecektir.

## Proje Yapısı

- `data_collector.py`: Kripto para birimi fiyat verilerini çeker.
- `data_preprocessor.py`: Verileri işler ve model için hazırlar.
- `model.py`: LSTM modelini oluşturur ve eğitir.
- `predictor.py`: Modeli kullanarak gelecekteki fiyatları tahmin eder ve sonuçları görselleştirir.
- `main.py`: Projenin ana dosyası, tüm bileşenleri bir araya getirir ve çalıştırır.

## Görseller

Modelin tahmin sonuçları ve performans metriklerini içeren görseller aşağıda sunulmuştur:

### Gerçek ve Tahmin Edilen Fiyatlar

![Actual vs Predicted](https://github.com/Fuatorium/Python-Projects-for-Interviews/blob/main/FinancePredictor/Figure_1.png)

### Gelecekteki Tahmin Edilen Fiyatlar

![Future Predictions](https://github.com/Fuatorium/Python-Projects-for-Interviews/blob/main/FinancePredictor/Figure_2.png)

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request açın veya bir issue oluşturun. Katkılarınız projeyi geliştirmeye yardımcı olacaktır.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
