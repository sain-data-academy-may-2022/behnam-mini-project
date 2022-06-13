import pytest
from app import (
    add_product,
    update_product,
    delete_product,

)


@pytest.fixture()
def products():
    return ['p0', 'p1']


@pytest.fixture()
def couriers():
    return ['c0']


@pytest.fixture()
def orders():
    return [
        {
            "customer_name": "John",
            "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
            "customer_phone": "0789887334",
            "courier_id": 0,
            "status": "preparing",
            }
        ]


@pytest.mark.parametrize(
    ('inputs', 'expected_products'),
    [
        (iter(['p2']), ['p0', 'p1', 'p2']),
    ]
    )
def test_add_product(products, inputs, expected_products, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert add_product(products) == expected_products


@pytest.mark.parametrize(
    ('inputs', 'expected_products'),
    [
        (iter(['0', 'p0_new']), ['p0_new', 'p1']),
    ]
    )
def test_update_product(products, inputs, expected_products, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert update_product(products) == expected_products


@pytest.mark.parametrize(
    ('inputs', 'expected_products'),
    [
        (iter(['0']), ['p1']),
        (iter(['1']), ['p0']),
    ]
    )
def test_delete_product(products, inputs, expected_products, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert delete_product(products) == expected_products



