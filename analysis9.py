cat_food_stats = df.groupby(['Kedi İsmi', 'Mama']).agg({
    'Yeme Süresi': 'mean',
    'Yenilen Mama Miktari': 'mean'
}).unstack().fillna(0)
print("\nKedilerin Mama Yaklaşım Süreleri ve Yenilen Miktar Ortalamaları:")
cat_food_stats