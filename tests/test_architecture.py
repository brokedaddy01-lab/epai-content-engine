from content_engine.registry import ManagerRegistry


def test_all_managers_registered():

    registry = ManagerRegistry()

    managers = registry.list_managers()

    assert "strategy" in managers
    assert "creation" in managers
    assert "intelligence" in managers
    assert "quality" in managers
    assert "optimization" in managers
    assert "production" in managers
    assert "publishing" in managers



def test_all_managers_have_health():

    registry = ManagerRegistry()

    health = registry.health()

    for manager in health.values():

        assert manager["status"] == "healthy"