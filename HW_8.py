import heapq # імпортуємо модуль

def minimum_cost_to_connect_cables(cables):
    # Перетворюємо список довжин кабелів у мінімальну купу
    heapq.heapify(cables)
    total_cost = 0

    # Об'єднуємо кабелі, поки в купі не залишиться один кабель
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість з'єднання дорівнює сумі їхніх довжин
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    # Повертаємо мінімальну з можливих сум загальних витрат
    return total_cost

# Приклад використання функції
cables = [4, 3, 2, 6]
print("Мінімальна сума загальних витрат:", minimum_cost_to_connect_cables(cables))
