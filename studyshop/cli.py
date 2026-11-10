"""Консольный интерфейс."""
import argparse
import humanize
from .pricing import total_cost


def main() -> None:
    parser = argparse.ArgumentParser(description="Расчёт суммы заказа")
    parser.add_argument("price", type=int, help="Цена единицы в рублях")
    parser.add_argument("quantity", type=int, help="Количество")
    parser.add_argument("--discount", type=int, default=0, help="Скидка, 0–100 процентов")
    args = parser.parse_args()
    try:
        result = total_cost(args.price, args.quantity, args.discount)
    except ValueError as error:
        parser.error(str(error))
    print(f"Стоимость: {humanize.intcomma(result)} руб.")


if __name__ == "__main__":
    main()
