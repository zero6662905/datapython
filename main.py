import matplotlib.pyplot as plt

weeks = ['Тиждень 1', 'Тиждень 2', 'Тиждень 3', 'Тиждень 4']

traffic = [1500, 1600, 1700, 1800]

sales_product_a = [300, 350, 400, 450]
sales_product_b = [200, 250, 300, 350]
sales_product_c = [100, 150, 200, 250]

plt.figure(figsize=(10, 6))

plt.plot(weeks, traffic, linestyle='-', marker='o', label='Веб-трафік')

plt.plot(weeks, sales_product_a, linestyle='--', marker='s', label='Продажі продукту A')
plt.plot(weeks, sales_product_b, linestyle='-.', marker='^', label='Продажі продукту B')
plt.plot(weeks, sales_product_c, linestyle=':', marker='d', label='Продажі продукту C')

plt.title('Щотижнева активність веб-трафіку та продажів')
plt.xlabel('Тижні')
plt.ylabel('Кількість')
plt.legend()
plt.grid(True)

plt.show()
