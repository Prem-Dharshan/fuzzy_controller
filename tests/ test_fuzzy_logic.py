from fuzzy_controller.fuzzy_logic import fuzzify, apply_rules, defuzzify, FUZZY_SETS


def test_fuzzify():
    result = fuzzify(100, FUZZY_SETS)
    assert isinstance(result, dict)


def test_apply_rules():
    speed_fuzzy = fuzzify(100, FUZZY_SETS)
    accel_fuzzy = fuzzify(70, FUZZY_SETS)
    rules = apply_rules(speed_fuzzy, accel_fuzzy)
    assert isinstance(rules, dict)


def test_defuzzify():
    areas = {1: 10, 2: 20}
    weighted_areas = {1: 100, 2: 300}
    result = defuzzify(areas, weighted_areas)
    assert result > 0
