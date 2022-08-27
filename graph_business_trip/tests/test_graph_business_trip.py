import pytest
from graph.graph import *
from graph_business_trip.graph_business_trip import *


def test_metroville_pandora(planets):
    names = ["Metroville", "Pandora"]
    assert business_trip(planets, names) == (True, 82)


def test_metroville_monstropolis(planets):
    names = ["Metroville", "New Monstropolis"]
    assert business_trip(planets, names) == (True, 105)


def test_arendelle_monstropolis_naboo(planets):
    names = ["Arendelle", "New Monstropolis", "Naboo"]
    assert business_trip(planets, names) == (True, 115)


def test_naboo_pandora(planets):
    names = ["Naboo", "Pandora"]
    assert business_trip(planets, names) == (False, 0)


def test_narnia_arendelle_naboo(planets):
    names = ["Narnia", "Arendelle", "Naboo"]
    assert business_trip(planets, names) == (False, 0)

# @pytest.mark.skip()
def test_pandora_narnia_short(planets):
    names = ["Pandora", "Metroville", "Narnia"]
    assert business_trip(planets, names) == (True, 119)


def test_pandora_narnia_expensive(planets):
    names = ["Pandora", "Arendelle", "New Monstropolis", "Naboo", "Narnia"]
    assert business_trip(planets, names) == (True, 515)


@pytest.fixture
def planets():
    graph = Graph()

    metroville = graph.add_node("Metroville")
    pandora = graph.add_node("Pandora")
    arendelle = graph.add_node("Arendelle")
    new_monstropolis = graph.add_node("New Monstropolis")
    naboo = graph.add_node("Naboo")
    narnia = graph.add_node("Narnia")

    graph.add_edge(pandora, arendelle, 150)

    graph.add_edge(pandora, metroville, 82)

    graph.add_edge(metroville, arendelle, 99)

    graph.add_edge(new_monstropolis, arendelle, 42)

    graph.add_edge(new_monstropolis, metroville, 105)

    graph.add_edge(new_monstropolis, naboo, 73)

    graph.add_edge(metroville, naboo, 26)

    graph.add_edge(metroville, narnia, 37)

    graph.add_edge(narnia, naboo, 250)

    return graph
