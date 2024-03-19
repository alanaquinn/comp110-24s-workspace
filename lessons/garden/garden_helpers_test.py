"""Test my garden functions."""

__author__ = "730411985"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

def test_add_by_kind_use_add_vegetables() -> None:
    """Use case: test basic use case for add_by_kind function by adding 2 items to vegetables."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "vegetable", "cucumber")
    add_by_kind(by_kind, "vegetable", "peppers")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots", "cucumber", "peppers"]}


def test_add_by_kind_edge_empty_groups() -> None:
    """Edge case: test adding to empty groups."""
    by_kind: dict[str, list[str]] = {"flower": [], "vegetable": [], "tree": []}
    add_by_kind(by_kind, "vegetable", "peppers")
    assert by_kind == {"flower": [], "vegetable": ["peppers"], "tree": []}


def test_add_by_date_use_add_plant() -> None:
    """Use case: test by adding a new plant to an already present month."""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(by_date, "April", "tulip")
    assert by_date == {"April": ["marigold", "tulip"], "June": ["carrots"]}


def test_add_by_date_edge_new_month() -> None:
    """Edge case: test by attempting to add to month not in dictionary/ add new month."""
    by_date: dict[str, list[str]] = {"April": ["marigold", "tulip"], "June": ["carrots"]}
    add_by_date(by_date, "May", "peonies")
    assert by_date == {"April": ["marigold", "tulip"], "June": ["carrots"], "May": ["peonies"]}


def test_lookup_by_kind_and_date_use_vegetable_June() -> None:
    """Use case: make sure lookup_by_kind_and_date returns only specified plants in specified month."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots", "cucumber", "peppers"]}
    by_date: dict[str, list[str]] = {"April": ["marigold", "tulip"], "June": ["carrots", "peppers", "zinnia"], "May": ["peonies"]}
    result: str = lookup_by_kind_and_date(by_kind, by_date, "vegetable", "June")
    # make sure it will return only vegetables in June and not cucumber or zinnia
    lookup_by_kind_and_date(by_kind, by_date, "vegetable", "June")
    assert result == "vegetables to plant in June: ['carrots', 'peppers']"


def test_lookup_by_kind_and_date_edge_none_correct() -> None:
    """Edge case: attempt to look for specified plant that does not exist in specified month."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots", "cucumber", "peppers"]}
    by_date: dict[str, list[str]] = {"April": ["marigold", "tulip"], "June": ["carrots", "peppers", "zinnia"], "May": ["peonies"]}
    result: str = lookup_by_kind_and_date(by_kind, by_date, "flower", "May")
    lookup_by_kind_and_date(by_kind, by_date, "flower", "May")
    assert result == "No flowers to plant in May."