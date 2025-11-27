import random

n = 100
ages = random.sample(range(1, 100), n)
print(ages)

print("\n --- Listeden sadece 18 yaş üstülerini çek. --- \n")
adults = []
for age in ages:
    if age >= 18:
        adults.append(age)
        print(age)
        print("Liste uzunluğu: ", len(adults))

print("\n --- Listedeki en uzun kelimeyi bul. --- \n")
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
        print(longest_word)


print("\n /////////////////// \n")
def find_longest_word(words2):
    longest_word2 = ""
    for word in words:
        if len(word2) > len(longest_word2):
            longest_word2 = word2
    return longest_word2

print(find_longest_word(words))

print("\n --- Listedeki sayıların karelerini yeni listeye al. --- \n")
num_len = 10
random_nums = [random.randint(1, 50) for _ in range(num_len)]
print(f"Orijinal Rasgele Liste: {random_nums}")

squares = [num ** 2 for num in random_nums]
print(f"Karelerin Listesi: {squares}")

squares_for= []
for num in random_nums:
    square = num ** 2
    squares_for.append(square)
print(f"Karelerin Listesi(for): {squares_for}")

print("\n --- Kullanıcı listesinden sadece adı “a” ile başlayanları çek. --- \n")
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack", "Anna", "Anabeth"]
a_names = [name for name in names if name.startswith("A")]
print(f"A ile başlayan isimler: {a_names}")

print("\n --- Bir sözlük listesinde “price > 1000” olan ürünleri listele. --- \n")
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 150},
    {"name": "Smartwatch", "price": 300},
    {"name": "Camera", "price": 1000},
    {"name": "Printer", "price": 200},
    {"name": "Monitor", "price": 700},
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25}
]

products_over_1000 = [product for product in products if product["price"] > 1000]
print(f"Ürünlerin fiyatı 1000'den fazla olanlar: {products_over_1000}")
