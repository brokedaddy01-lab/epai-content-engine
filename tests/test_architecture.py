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


def test_registry_is_singleton():

    first = ManagerRegistry()

    second = ManagerRegistry()

    assert first is second


def test_intelligence_uses_registry_content_memory():

    registry = ManagerRegistry()

    assert (
        registry.managers["intelligence"].content_memory
        is registry.content_memory
    )