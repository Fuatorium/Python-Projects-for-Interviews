# Python Projects for Interviews

Bu depo, iş görüşmelerinde kullanılabilecek çeşitli Python projelerini içermektedir. Her proje, belirli bir problem alanını hedef almakta ve çözüm önerileri sunmaktadır. Aşağıda projelerin kısa açıklamaları ve her birine nasıl erişileceği hakkında bilgiler yer almaktadır.

## İçindekiler

- [AutoDataAnalyzer](#autodataanalyzer)
- [FinancePredictor](#financepredictor)

## AutoDataAnalyzer

AutoDataAnalyzer projesi, otomatik veri analizi yaparak veri setlerini hızlı bir şekilde özetler ve görselleştirir. Proje, veri bilimciler ve analistler için büyük kolaylık sağlar.

- **Özellikler**:
  - Veri setlerinin otomatik olarak analizi
  - Görselleştirme ve özetleme
  - Kolay kullanım arayüzü

Daha fazla bilgi için [AutoDataAnalyzer README dosyasını](./AutoDataAnalyzer/README.md) inceleyin.

## FinancePredictor

FinancePredictor projesi, Bitcoin gibi kripto para birimlerinin gelecekteki fiyatlarını tahmin etmek için bir makine öğrenmesi modelini kullanır. Proje, zaman serisi analizine dayanmaktadır.

- **Özellikler**:
  - Geçmiş kripto para birimi fiyat verilerini çekme ve ön işleme
  - LSTM modeli kullanarak fiyat tahmini yapma
  - Tahmin sonuçlarını görselleştirme
  - Model performans metriklerini hesaplama

Daha fazla bilgi için [FinancePredictor README dosyasını](./FinancePredictor/README.md) inceleyin.

## Kurulum

### Gereksinimler

- Python 3.7 veya daha yeni bir sürüm
- Anaconda (tavsiye edilir)

### Adımlar

1. Depoyu klonlayın:
    ```sh
    git clone https://github.com/fuatorium/Python-Projects-for-Interviews.git
    cd Python-Projects-for-Interviews
    ```

2. Her proje için bağımlılıkları yükleyin. Örneğin, `FinancePredictor` için:
    ```sh
    cd FinancePredictor
    conda create --name finance-prediction-env python=3.8
    conda activate finance-prediction-env
    pip install -r requirements.txt
    ```

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request açın veya bir issue oluşturun. Katkılarınız projeyi geliştirmeye yardımcı olacaktır.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
