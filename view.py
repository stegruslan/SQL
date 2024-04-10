"""tewtw."""

from models import Order, OrderProductLink, Product, Rack, RackProductLink


class View:
    """dfdfsg."""

    def __init__(self: "View", order_numbers: list[int]) -> None:
        """_summary_.

        Args:
        ----
            self (View): _description_.
            order_numbers (list[int]): _description_.

        """
        self.order_numbers = order_numbers
        self.racks = self._get_racks()

    def _get_racks(self: "View") -> dict:
        """_summary_.

        Args:
        ----
            self (View): _description_.

        """
        order_product: dict[int, list[Product]] = {
            number: [
                Product.get_by("id", link.product_id)
                for link in OrderProductLink.get_all_by(
                    "order_id",
                    Order.get_by("order_number", number).id,
                )
            ]
            for number in self.order_numbers
        }
        print(order_product)
        racks = [
            (Rack.get_by("id", link.rack_id).name, product, number)
            for number, products in order_product.items()
            for product in products
            for link in RackProductLink.get_all_by("product_id", product.id)
        ]
        result = {}
        for rack, product, number in racks:
            if rack in result:
                result[rack].append((rack, str(product), str(number)))
            else:
                result[rack] = [(rack, str(product), str(number))]
        for products in result.values():
            products.sort(key=lambda x: x[2])
        print(result)

    def __str__(self: "View") -> str:
        """dfhdfh.

        Args:
        ----
            self (View): _description_.

        Returns:
        -------
            _type_: _description_.

        """
        n = "\n"
        return (
            f"=+=+=+=\n"
            f"Страница сборки заказов {', '.join(self.order_numbers)}\n\n"
            f"{n.join(self.rackviews)}"
        )


v = View([10, 11, 14, 15])
