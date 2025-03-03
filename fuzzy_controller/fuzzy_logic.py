import numpy as np


# Membership Functions
def triangular(x, a, b, c):
    if a < x < b:
        return (x - a) / (b - a)
    if b <= x < c:
        return (c - x) / (c - b)
    return 0


def trapezoidal(x, a, b, c, d):
    if a < x < b:
        return (x - a) / (b - a)
    if b <= x <= c:
        return 1
    if c < x < d:
        return (d - x) / (d - c)
    return 0


def get_membership(x, fuzzy_set):
    return trapezoidal(x, *fuzzy_set) if len(fuzzy_set) == 4 else triangular(x, *fuzzy_set)


# Fuzzy Sets
FUZZY_SETS = {
    "NL": [0, 0, 31, 61], "NM": [31, 61, 95], "NS": [61, 95, 127], "ZE": [95, 127, 159],
    "PS": [127, 159, 191], "PM": [159, 191, 223], "PL": [191, 223, 255, 255]
}

RULES = {
    1: ["NL", "ZE", "PL"], 2: ["ZE", "NL", "PL"], 3: ["NM", "ZE", "PM"], 4: ["NS", "PS", "PS"],
    5: ["PS", "NS", "NS"], 6: ["PL", "ZE", "NL"], 7: ["ZE", "NS", "PS"], 8: ["ZE", "NM", "PM"]
}


def fuzzify(value, sets):
    return {k: get_membership(value, v) for k, v in sets.items()}


def apply_rules(speed_fuzzy, accel_fuzzy):
    return {i: (min(speed_fuzzy[s], accel_fuzzy[a]), o) for i, (s, a, o) in RULES.items() if
            min(speed_fuzzy[s], accel_fuzzy[a]) > 0}


def calculate_areas(rule_strengths):
    areas, weighted_areas = {}, {}
    for i, (strength, out) in rule_strengths.items():
        set_vals = FUZZY_SETS[out]
        center = set_vals[1] if len(set_vals) == 3 else (set_vals[1] + set_vals[2]) / 2
        if len(set_vals) == 4:
            base1 = set_vals[3] - set_vals[0]
            base2 = set_vals[2] - set_vals[1]
            area = strength * (base1 + base2) / 2
        else:
            base = set_vals[2] - set_vals[0]
            area = strength * base / 2
        areas[i] = area
        weighted_areas[i] = area * center
    return areas, weighted_areas


def defuzzify(areas, weighted_areas):
    total_area = sum(areas.values())
    return sum(weighted_areas.values()) / total_area if total_area > 0 else 0
