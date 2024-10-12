plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
sns.barplot(x=food_counts.index, y=food_counts.values, palette="viridis")
plt.title('Mama Tercih Sayıları')
plt.xlabel('Mama Türü')
plt.savefig('mama_tercih_sayisi.png')
plt.ylabel('Sayı')
