# AutoDataAnalyzer

AutoDataAnalyzer, veri bilimciler ve analistler için tasarlanmış bir araçtır. Bu proje, veri setlerini otomatik olarak analiz eder, özetler ve görselleştirir. Bu sayede, verinin hızlı bir şekilde anlaşılmasını sağlar.

## Özellikler

- Veri setlerinin otomatik olarak analizi
- Temel istatistiksel özetlerin oluşturulması
- Veri görselleştirme (grafikler ve tablolar)
- Kullanımı kolay arayüz

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Kurulum

### Gereksinimler

- Python 3.7 veya daha yeni bir sürüm
- Anaconda (tavsiye edilir)

### Adımlar

1. Depoyu klonlayın:
    ```sh
    git clone https://github.com/fuatorium/Python-Projects-for-Interviews.git
    cd Python-Projects-for-Interviews/AutoDataAnalyzer
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```sh
    conda create --name autodata-analyzer-env python=3.8
    conda activate autodata-analyzer-env
    pip install -r requirements.txt
    ```

## Kullanım

1. `main.py` dosyasını çalıştırarak veri analizine başlayın:
    ```sh
    python main.py
    ```

2. Sonuçlar, oluşturulan grafikler ve özetler şeklinde görselleştirilecektir.

## Proje Yapısı

- `data_loader.py`: Veri setlerini yükler ve hazırlar.
- `data_analyzer.py`: Veri analizi ve özet çıkarımı yapar.
- `visualizer.py`: Veriyi görselleştirir.
- `main.py`: Projenin ana dosyası, tüm bileşenleri bir araya getirir ve çalıştırır.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request açın veya bir issue oluşturun. Katkılarınız projeyi geliştirmeye yardımcı olacaktır.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
