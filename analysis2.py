cat_food_counts = df.groupby(['Kedi İsmi', 'Mama']).size().unstack().fillna(0)
print("\nKedilerin Mama Tercihleri:")
cat_food_counts