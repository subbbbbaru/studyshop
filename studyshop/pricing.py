"""Вычисления в целых рублях для учебного проекта."""

def total_cost(price: int, quantity: int, discount: int = 0) -> int:
    """Цена заказа: price — цена единицы, discount — скидка в процентах."""
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    if quantity < 1:
        raise ValueError("Количество должно быть положительным")
    if not 0 <= discount <= 100:
        raise ValueError("Скидка должна быть от 0 до 100")
    return price * quantity * (100 - discount) // 100
