plt.subplot(2, 1, 2)
sns.heatmap(cat_food_stats['Yeme Süresi'], annot=True, fmt=".2f", cmap="YlGnBu")
plt.title('Kedilerin Mama Yaklaşım Süreleri (Saniye)')
plt.xlabel('Mama Türü')
plt.ylabel('Kedi')

plt.tight_layout()
plt.savefig('mama_yaklasim_suresi(saniye).png')

plt.show()