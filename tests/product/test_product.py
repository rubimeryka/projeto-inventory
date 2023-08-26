from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="1",
        product_name="Paper",
        company_name="Dunder Mifflin",
        manufacturing_date="2013-02-28",
        expiration_date="2023-12-31",
        serial_number="123 456 789",
        storage_instructions="não rasgar",
    )
    assert product.id == '1'
    assert product.product_name == 'Paper'
    assert product.company_name == 'Dunder Mifflin'
    assert product.manufacturing_date == '2013-02-28'
    assert product.expiration_date == '2023-12-31'
    assert product.serial_number == '123 456 789'
    assert product.storage_instructions == 'não rasgar'
