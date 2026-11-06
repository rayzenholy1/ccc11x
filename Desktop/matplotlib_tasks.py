import numpy as np
import matplotlib.pyplot as plt

months = ["Січ", "Лют", "Бер", "Кві", "Тра", "Чер", "Лип", "Сер", "Вер", "Жов", "Лис", "Гру"]
plan = [100, 110, 120, 130, 140, 150, 160, 155, 145, 135, 125, 170]
fact = [95, 115, 118, 125, 150, 148, 165, 150, 140, 138, 120, 180]

plt.figure(figsize=(10, 5))
plt.plot(months, plan, marker="o", label="План")
plt.plot(months, fact, marker="s", label="Факт")
plt.xlabel("Місяць")
plt.ylabel("Продажі")
plt.title("Плановi та фактичнi продажi за мiсяцями")
plt.legend()
plt.show()

ages = np.random.randint(18, 70, 100)

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=10, color="skyblue", edgecolor="black")
plt.axvline(ages.mean(), color="red", linestyle="--", label=f"Середнє: {ages.mean():.1f}")
plt.xlabel("Вік")
plt.ylabel("Кількість осіб")
plt.title("Розподіл віку 100 осіб")
plt.legend()
plt.show()

g1 = np.random.normal(70, 10, 30)
g2 = np.random.normal(75, 7, 30)
g3 = np.random.normal(65, 15, 30)

plt.figure(figsize=(8, 5))
plt.boxplot([g1, g2, g3], labels=["Група 1", "Група 2", "Група 3"])
plt.xlabel("Група")
plt.ylabel("Оцінка")
plt.title("Розкид оцінок за групами")
plt.show()

dates = ["01.10", "02.10", "03.10", "04.10", "05.10", "06.10", "07.10"]
temp = [14, 16, 15, 18, 20, 19, 17]
hum = [70, 65, 68, 60, 55, 58, 62]

plt.figure(figsize=(9, 5))
plt.plot(dates, temp, marker="o", color="red", label="Температура, °C")
plt.plot(dates, hum, marker="s", color="blue", label="Вологість, %")
plt.xlabel("Дата")
plt.ylabel("Значення")
plt.title("Температура і вологість за тиждень")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

hours = list(range(24))
load = np.random.randint(10, 90, 24)

plt.figure(figsize=(10, 5))
plt.plot(hours, load, color="green")
plt.fill_between(hours, load, color="green", alpha=0.3)
plt.grid(True)
plt.xlabel("Година")
plt.ylabel("Навантаження, %")
plt.title("Навантаження сервера за добу")
plt.xticks(hours)
plt.show()

t = np.arange(1, 13)
conversion = np.random.uniform(2, 6, 12)
retention = np.random.uniform(40, 80, 12)
check = np.random.uniform(300, 700, 12)
orders = np.random.randint(100, 500, 12)

fig, axs = plt.subplots(2, 2, figsize=(11, 8))
axs[0, 0].plot(t, conversion, color="blue")
axs[0, 0].set_title("Конверсія, %")
axs[0, 1].plot(t, retention, color="green")
axs[0, 1].set_title("Утримання, %")
axs[1, 0].plot(t, check, color="orange")
axs[1, 0].set_title("Середній чек")
axs[1, 1].bar(t, orders, color="purple")
axs[1, 1].set_title("Кількість замовлень")
for ax in axs.flat:
    ax.set_xlabel("Місяць")
    ax.grid(True)
fig.suptitle("Метрики продукту")
plt.tight_layout()
plt.show()
