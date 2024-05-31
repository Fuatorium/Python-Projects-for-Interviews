import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import pickle

df = pd.read_csv('customer_data.csv')

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = df.select_dtypes(include=['object']).columns

df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

gender_encoder = LabelEncoder()
df['Gender'] = gender_encoder.fit_transform(df['Gender'])

profession_encoder = LabelEncoder()
df['Profession'] = profession_encoder.fit_transform(df['Profession'])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop(['CustomerID'], axis=1))

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(scaled_features)

df['Segment'] = kmeans.labels_

segment_means = df.groupby('Segment').mean()

income_threshold = df['Annual Income ($)'].median()
spending_threshold = df['Spending Score (1-100)'].median()

def age_group(age):
    if age <= 18:
        return "Çocuk"
    elif age <= 35:
        return "Genç"
    elif age <= 50:
        return "Orta yaşlı"
    elif age <= 65:
        return "Yaşlı"
    else:
        return "Çok yaşlı"

segment_descriptions = {}
for segment, row in segment_means.iterrows():
    age_desc = age_group(row['Age'])
    income_desc = "düşük gelirli" if row['Annual Income ($)'] < income_threshold else "yüksek gelirli"
    spending_desc = "düşük harcama puanına sahip" if row['Spending Score (1-100)'] < spending_threshold else "yüksek harcama puanına sahip"
    segment_descriptions[segment] = f"{age_desc}, {income_desc} ve {spending_desc} müşteriler."

with open('models/segment_descriptions.pkl', 'wb') as f:
    pickle.dump(segment_descriptions, f)

pickle.dump(kmeans, open('models/kmeans_model.pkl', 'wb'))
pickle.dump(scaler, open('models/scaler.pkl', 'wb'))
pickle.dump(gender_encoder, open('models/gender_encoder.pkl', 'wb'))
pickle.dump(profession_encoder, open('models/profession_encoder.pkl', 'wb'))

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 8))
sns.barplot(data=segment_means, palette="viridis")
plt.title('Segmentlerin Ortalama Özellikleri')
plt.xlabel('Özellikler')
plt.ylabel('Ortalama Değer')
plt.savefig('static/segment_means.png')
