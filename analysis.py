import pandas as pd

# Kedilerin isimleri ve cinsleri
cat_info = {
    'Sascha': 'British Shorthair',
    'Milka': 'British Shorthair',
    'Minti': 'British Shorthair',
    'Sindy': 'British Shorthair',
    'Cabriyella': 'British Shorthair'
}

foods = ['Royal Canin', 'Hills Science Diet', 'Purina Pro Plan', 'Blue Buffalo', 'Wellness Core']

data = []

cat_list = ['Sascha', 'Milka', 'Minti', 'Sindy', 'Cabriyella']
food_list = ['Royal Canin', 'Hills Science Diet', 'Purina Pro Plan', 'Blue Buffalo', 'Wellness Core']
approach_times = [10, 15, 20, 25, 30, 35, 40]
food_eaten_quantities = [10, 20, 30, 40, 50]

for i in range(100):
    cat = cat_list[i % len(cat_list)]
    food = food_list[i % len(food_list)]
    approach_time = approach_times[i % len(approach_times)]
    food_eaten = food_eaten_quantities[i % len(food_eaten_quantities)]
    data.append([cat, cat_info[cat], food, approach_time, food_eaten])

df = pd.DataFrame(data, columns=['Kedi İsmi', 'Kedi Cinsi', 'Mama', 'Yeme Süresi', 'Yenilen Mama Miktari'])

df.head()
