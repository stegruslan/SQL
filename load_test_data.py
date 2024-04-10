"""Модуль для загрузки тестовых данных в бд."""

from database import Database
from migrate import migrate
from settings import settings


def execute_many_command(
    sql_command: str,
    data: list[tuple[str | int]],
) -> None:
    """Выполнить команду c  разлиными данными.

    Args:
    ----
        sql_command (str): сама sql команда.
        data (list[tuple[str  |  int]]): данные в нужном формате

    """
    db = Database(settings=settings)
    with db() as conn:
        cur = conn.cursor()
        cur.executemany(sql_command, data)
        conn.commit()


rack_insert = """
INSERT INTO rack(name)
VALUES (%s)
"""
rack_insert_values = [("А",), ("Б",), ("Ж",), ("В",), ("З",)]

order_insert = """
INSERT INTO ordert(order_number, consumer_name)
VALUES (%s, %s)
"""
order_insert_values = [(10, "A"), (11, "B"), (14, "C"), (15, "D")]

product_insert = """
INSERT INTO product(name, article)
VALUES (%s, %s)
"""
product_insert_values = [
    ("Ноутбук", 1),
    ("Телевизор", 2),
    ("Телефон", 3),
    ("Системный блок", 4),
    ("Часы", 5),
    ("Микрофон", 6),
]

rack_product_link_insert = """
INSERT INTO rack_product_link(rack_id, product_id, main)
VALUES (
    (SELECT id FROM rack WHERE rack.name = %s),
    (SELECT id FROM product WHERE product.article = %s),
    %s
    )
"""
order_product_link_insert = """
INSERT INTO order_product_link(order_id, product_id, count)
VALUES (
    (SELECT id FROM ordert WHERE ordert.order_number = %s),
    (SELECT id FROM product WHERE product.article = %s),
    %s
    )
"""
rack_product_link_insert_values = [
    ("А", 1, True),
    ("А", 2, True),
    ("Б", 3, True),
    ("З", 3, False),
    ("В", 3, False),
    ("Ж", 4, True),
    ("Ж", 5, True),
    ("Ж", 6, True),
]

order_product_link_insert_values = [
    (10, 1, 2),
    (11, 2, 3),
    (14, 1, 3),
    (10, 3, 1),
    (14, 4, 4),
    (15, 5, 1),
    (10, 6, 1),
]


def load() -> None:
    """Основная функция модуля."""
    migrate()
    execute_many_command(rack_insert, rack_insert_values)
    execute_many_command(order_insert, order_insert_values)
    execute_many_command(product_insert, product_insert_values)
    execute_many_command(
        rack_product_link_insert,
        rack_product_link_insert_values,
    )
    execute_many_command(
        order_product_link_insert,
        order_product_link_insert_values,
    )


if __name__ == "__main__":
    load()
