from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="1",
        product_name="Paper",
        company_name="Dunder Mifflin",
        manufacturing_date="2013-02-28",
        expiration_date="2023-12-31",
        serial_number="123 456 789",
        storage_instructions="não rasgar",
    )
    assert str(product) == (
        f"The product {product.id} - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        "must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )
