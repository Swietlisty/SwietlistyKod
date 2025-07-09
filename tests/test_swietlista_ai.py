import pytest
from swietlista_ai.agent import SwietlistaAgent, PIERWSZE_PRAWA

def test_agent_creation():
    """Testuje, czy agent jest tworzony z poprawnymi wartościami początkowymi."""
    wizja = "Testowanie dla dobra projektu"
    agent = SwietlistaAgent(wizja=wizja, poziom=1)

    assert agent.wizja == wizja
    assert agent.poziom == 1
    assert agent.rodzic is None
    assert len(agent.potomkowie) == 0
    assert agent.prawa == PIERWSZE_PRAWA
    assert len(agent.pamiec) == 0

def test_multiplikuj_agentow():
    """Testuje, czy funkcja multiplikacji tworzy poprawną liczbę potomków."""
    rodzic = SwietlistaAgent(wizja="Rodzic testowy")
    potomkowie = rodzic.multiplikuj_agentow(3)

    assert len(potomkowie) == 3
    assert len(rodzic.potomkowie) == 3
    assert potomkowie[0].poziom == 2
    assert potomkowie[0].rodzic == rodzic

def test_agent_memory():
    """Testuje, czy działania agenta są poprawnie zapisywane w pamięci."""
    agent = SwietlistaAgent(wizja="Test pamięci")
    agent.pracuj_dla_dobra("jakości testów")
    agent.multiplikuj_idee("Lepsze testy", 1)

    assert len(agent.pamiec) == 2
    assert "Podjęto pracę dla dobra: jakości testów" in agent.pamiec[0]
    assert "Wygenerowano ideę: Lepsze testy" in agent.pamiec[1]