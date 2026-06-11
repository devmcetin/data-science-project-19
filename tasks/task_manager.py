import numpy as np
from typing import List, Dict


# Açıklama: Karakterlerin büyü gücünü Gaussian (Normal) dağılım kullanarak üret.
# Girdi: n=100
# Çıktı: [75.2, 81.0, 68.3, ..., 90.5] (numpy array)
# Dağılım: np.random.normal(loc=75, scale=10, size=n)
def generate_magic_power_scores(n):
    return np.random.normal(75, 10, n)


# Açıklama: Normal dağılım skoru al, Z-score ile standartlaştır.
# Input: [70, 75, 80]
# Output: [-1.0, 0.0, 1.0]
def standardize_scores(scores):
    scores_array = np.array(scores)
    return (scores_array - np.mean(scores_array)) / np.std(scores_array, ddof=1)


# Açıklama: Karakter sadakat puanlarını uniform dağılımla üret (0-100)
# Input: n=5
# Output: [21.4, 87.3, 45.1, 68.9, 12.3]
def generate_uniform_loyalty_scores(n):
    return np.random.uniform(0, 101, n)


# Açıklama: Güce göre ilk n karakterin ismini döndür.
# Input: [80, 55, 90], ["Harry", "Ron", "Hermione"], 2
# Output: ["Hermione", "Harry"]
def get_top_n_characters_by_power(scores, names, n):
    sorted_indices = np.argsort(scores)[::-1]
    top_n_indices = sorted_indices[:n]

    return [names[i] for i in top_n_indices]


# Açıklama: Verilen bir değerin z-skorunu hesapla.
# Input: value=85, mean=75, std=5
# Output: 2.0
def calculate_z_score(value, mean, std):
    return (value - mean) / std


# Açıklama: Büyü gücüne göre Gryffindor, Slytherin, Hufflepuff veya Ravenclaw ata.
# Kurallar:
# 90 → Gryffindor
# 75–90 → Slytherin
# 50–75 → Ravenclaw
# <50 → Hufflepuff
# Input: score=82
# Output: "Slytherin"
def assign_house(score):
    if score >= 90:
        return "Gryffindor"
    elif score >= 75:
        return "Slytherin"
    elif score >= 50:
        return "Ravenclaw"
    else:
        return "Hufflepuff"


# Açıklama: Her bir ev için büyü puanlarının ortalamasını hesapla.
# Input: { 'Gryffindor': [95, 90], 'Hufflepuff': [45, 50] }
# Output: { 'Gryffindor': 92.5, 'Hufflepuff': 47.5 }
def calculate_house_average(house_dict):
    return {house: np.mean(score) for house, score in house_dict.items()}


# Açıklama: Normal dağılımda IQR kullanarak uç karakterleri bul.
# Input: [50, 52, 90, 91], ['A', 'B', 'C', 'D']
# Output: ['C', 'D']
def get_outlier_characters(scores, names):
    scores_array = np.array(scores)
    names_array = np.array(names)

    q1 = np.quantile(scores_array, 0.25)
    q3 = np.quantile(scores_array, 0.75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    higher_fence = q3 + 1.5 * iqr

    mask = (scores_array < lower_fence) | (scores_array > higher_fence)

    return names_array[mask].tolist()
