# ===============================
# Analisis Data Nilai Siswa
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
data = pd.read_csv('analisis_siswa.csv')

# Melihat informasi dasar dataset
print("=== Informasi Dataset ===")
data.info()
print("\n")

# Menampilkan 5 data pertama
print("=== 5 Data Pertama ===")
print(data.head())
print("\n")

# Statistik deskriptif
print("=== Statistik Deskriptif ===")
print(data.describe())
print("\n")

# Rata-rata, median, dan modus
print("=== Statistik Nilai ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
print("\n")

# Menampilkan nilai per mata pelajaran
print("=== Nilai Matematika ===")
matematika = data[data['Mapel'] == 'Matematika']
print(matematika)
print("\n")

print("=== Nilai Bahasa Inggris ===")
inggris = data[data['Mapel'] == 'Bahasa Inggris']
print(inggris)
print("\n")

print("=== Nilai Bahasa Indonesia ===")
indo = data[data['Mapel'] == 'Bahasa Indonesia']
print(indo)
print("\n")

print("=== Nilai Produktif ===")
produktif = data[data['Mapel'] == 'Produktif']
print(produktif)
print("\n")

# Nilai maksimum dan minimum per mapel
print("=== Nilai Maksimum dan Minimum per Mapel ===")
print(data.groupby('Mapel')['Nilai'].agg(['max', 'min']))
print("\n")

# Rata-rata nilai per mapel
rata = data.groupby('Mapel')['Nilai'].mean()

# Grafik batang rata-rata nilai
plt.figure(figsize=(8, 5))
rata.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.tight_layout()
plt.show()

# Menyimpan grafik ke file (opsional)
plt.figure(figsize=(8, 5))
rata.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.tight_layout()
plt.savefig('grafik_rata_rata.png')

# Boxplot sebaran nilai
plt.figure(figsize=(8, 5))
sns.boxplot(x='Mapel', y='Nilai', data=data, palette='pastel')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.tight_layout()
plt.show()

# Kesimpulan
print("""
============================
KESIMPULAN:
1. Rata-rata nilai tertinggi diperoleh pada mata pelajaran Produktif.
2. Sebaran nilai paling lebar terlihat pada mata pelajaran Matematika,
   menandakan variasi kemampuan siswa cukup besar.
3. Nilai terendah terdapat pada Bahasa Inggris, menunjukkan perlunya peningkatan.
============================
""")