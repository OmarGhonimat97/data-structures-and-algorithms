import pytest
from hashtable import HashTable


def test_hash_method():
    """
    'd' = 100
    100 * 283 = 28300
    28300 % 1024 = 652
    """
    hash = HashTable()
    expected = 652
    actual = hash._HashTable__hash('d')
    assert expected == actual


def test_set(hash_table):
    hash_table.set('key3', 'test3')
    assert hash_table.key()[2] == 'key3'


def test_get(hash_table):
    assert hash_table.get('key1') == 'test1'
    assert hash_table.get('key2') == 'test2'
    assert hash_table.get('key7') is None


def test_unique_keys(hash_table):
    assert hash_table.key() == ['key1', 'key2']


def test_handling_collision(hash_table):
    hash_table.set('key3', 'test3')
    hash_table.set('key3', 'test4')
    hash_table.set('key3', 'test5')
    assert len(hash_table.get('key3')) == 3
    assert hash_table.get('key3') == ['test5', 'test4', 'test3']


def test_contains(hash_table):
    assert hash_table.contains('key1') is True
    assert hash_table.contains('key4') is False


@pytest.fixture
def hash_table():
    hash = HashTable()
    hash.set('key1', 'test1')
    hash.set('key2', 'test2')
    return hash
