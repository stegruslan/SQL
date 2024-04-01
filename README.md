# Тестовое задание создание таблиц в БД.

![Текст с описанием картинки](https://github.com/stegruslan/SQL/blob/master/image/image1.png)

## Таблица для сборки заказов. В данной таблице представленны :
- rack ( Стеллаж )
- product ( Товар )
- order ( Заказ )

Каждый стеллаж и товар имеет уникальный номер (id).







---
## Пример создание таблицы:
```product_table_create = """
CREATE TABLE IF NOT EXISTS product (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
article INTEGER UNIQUE NOT NULL
)
"""```