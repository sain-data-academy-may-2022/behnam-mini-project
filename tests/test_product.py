import pytest
from unittest.mock import patch, Mock

from utils.product import (
    add_product,
    update_product,
    delete_product,
)


@pytest.fixture()
def products():
    return [(1, "p1"), (2, "p2")]


@patch("builtins.input", side_effect=["p3"])
def test_add_product(mock_input, products):
    expected_products = products + [(3, "p3")]
    mock_read_products = Mock(return_value=expected_products)
    mock_insert_product_into_db = Mock()

    actual = add_product(mock_insert_product_into_db, mock_read_products)

    assert actual == expected_products
    mock_insert_product_into_db.assert_called_with("p3")


@patch("builtins.input", side_effect=["0", "p1_new"])
def test_update_product(mock_input, products):
    expected_products = [(1, "p1_new"), (2, "p2")]
    mock_read_products = Mock(return_value=expected_products)
    mock_update_product_on_db = Mock()

    actual = update_product(products, mock_update_product_on_db, mock_read_products)

    assert actual == expected_products
    mock_update_product_on_db.assert_called_with(1, "p1_new")


@patch("builtins.input", side_effect=["0"])
def test_delete_product(mock_input, products):
    expected_products = [(2, "p2")]
    mock_read_products = Mock(return_value=expected_products)
    mock_delete_product_from_db = Mock()

    actual = delete_product(products, mock_delete_product_from_db, mock_read_products)

    assert actual == expected_products
    mock_delete_product_from_db.assert_called_with(1)
