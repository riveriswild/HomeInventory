import pytest

from main.models import ApplianceItem, GeneralItem, Location


@pytest.mark.django_db
class TestLocationModel:

    @pytest.fixture
    def setup_locations(self):
        root_location = Location.objects.create(name="Bedroom")
        child_location = Location.objects.create(name="Shelf", parent=root_location)
        return root_location, child_location

    def test_location_str(self, setup_locations):
        root_location, child_location = setup_locations
        assert str(root_location) == "Bedroom"
        assert str(child_location) == "Shelf"

    def test_get_ancestors(self, setup_locations):
        root_location, child_location = setup_locations
        ancestors = child_location.get_ancestors()
        assert len(ancestors) == 1
        assert ancestors[0] == root_location

    def test_get_descendants(self, setup_locations):
        root_location, child_location = setup_locations
        descendants = root_location.get_descendants()
        assert len(descendants) == 1
        assert descendants[0] == child_location


@pytest.mark.django_db
class TestGeneralItemModel:

    @pytest.fixture
    def setup_general_item(self):
        location = Location.objects.create(name="Kitchen")
        item = GeneralItem.objects.create(name="Stove", location=location, price=30)
        return item

    def test_general_item_str(self, setup_general_item):
        item = setup_general_item
        assert str(item.name) == "Stove"

    def test_price_history(self, setup_general_item):
        item = setup_general_item
        assert item.pricehistory_set.count() == 1
        price_history = item.pricehistory_set.first()
        assert price_history.price == 30


@pytest.mark.django_db
class TestApplianceItemModel:

    @pytest.fixture
    def setup_appliance_item(self):
        location = Location.objects.create(name="Second drawer")
        appliance_item = ApplianceItem.objects.create(
            name="Kettle", location=location, price=40, warranty_expiration="2026-01-01"
        )
        return appliance_item

    def test_warranty_expiration(self, setup_appliance_item):
        appliance_item = setup_appliance_item
        assert str(appliance_item.warranty_expiration) == "2026-01-01"
