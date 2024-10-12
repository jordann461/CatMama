plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['Yeme Süresi'], kde=True, bins=20, color='blue')
plt.title('Yaklaşım Süresi Dağılımı')
plt.xlabel('Yaklaşım Süresi (saniye)')

plt.subplot(1, 2, 2)
sns.histplot(df['Yenilen Mama Miktari'], kde=True, bins=20, color='green')
plt.title('Yenilen Mama Miktarı Dağılımı')
plt.xlabel('Yenilen Mama Miktarı (gram)')

plt.tight_layout()
plt.savefig('yaklasimlar.png')
plt.show()