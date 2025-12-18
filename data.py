"""Data file.

This stores the classroom codes available."""

# Constant number
N_CONST = "010000"

# Classroom codes organized by building
CLASSROOMS = {
    "Building E1": {
        # Floor 1
        "101": "",
        "102": "",
        "103": "",
        "104": "3.1.15",  # Vrf (25/11/2025)
        "105": "",
        # Floor 2
        "106": "",  # S. Juicios Orales
        "107": "3.1.17",  # Vrf (25/11/2025)
        "108": "",  # ARQ? - EST
        "109": "",
        "110": "3.1.14",  # Vrf (25/11/2025)
    },
    "Building E2": {
        # Floor 1
        "203": "3.1.26",  # Vrf (26/11/2025)
        "204": "3.1.27",  # EST
        "205": "3.1.28",  # Vrf (26/11/2025)
        "206": "3.1.29",  # EST
        "207": "3.1.30",  # Vrf (26/11/2025)
        "208": "3.1.196",  # Vrf (26/11/2025) - REV AGN
        "209": "3.1.32",  # Vrf (26/11/2025)
        # Floor 2
        "210": "3.1.33",  # Vrf (24/11/2025)
        "211": "3.1.34",  # EST
        "212": "3.1.35",  # Vrf (24/11/2025)
        "213": "3.1.36",  # Vrf (24/11/2025)
        "214": "3.1.37",  # EST
        "215": "3.1.38",  # Vrf (21/11/2025)
        "216": "3.1.39",  # EST
        "217": "3.1.40",  # EST
        "218": "3.1.41",  # EST
        "219": "3.1.42",  # EST
        # Floor 3
        "220": "",  # ACT
        "221": "34.97.52",  # Vrf (21/11/2025)
        "222": "34.97.53",  # EST
        "223": "34.97.54",  # EST
        "224": "34.97.55",  # Vrf (21/11/2025)
        "225": "34.97.56",  # EST
        "226": "34.97.57",  # EST
        "227": "34.97.50",  # ACT - Vrf (21/11/2025)
    },
    "Building E3": {

    },
    "Building E4": {
        # Bld. E4, Fl. 1
        "406": "",
        "407": "",
        "408": "",
        "409": "38.36.1",  # ACT - Vrf (21/11/2025)
        "410": "",
        "411": "3.1.59",  # Vrf (21/11/2025)

        # Bld. E4, Fl. 2
        "421": "3.1.126",  # EST
        "422": "3.1.127",  # EST
        "423": "3.1.128",  # EST
        "424": "3.1.129",  # Vrf (25/11/2025)
        "425": "3.1.130",  # EST
        "426": "3.1.131",  # EST
        "427": "3.1.132",  # EST
        "428": "3.1.133",  # Vrf (25/11/2025)
    }
}
"""# Bld. A2, Fl. 1
    "602": "38.34.1",  # ACT - Vrf (21/11/2025)
    "603": "38.35.50",  # ACT-MAC - Vrf (21/11/2025)

    # Bld. E5, Fl. 1
    "516": "37.80.1",  # ACT - Vrf (25/11/2025)

    # Bld. B, Fl. 1
    "701": "39.107.1", # SAVI - Vrf (24/11/2025)"""
# Creates a list from the classroom codes dictionary
CLASSROOMS_LIST = []
for building, classrooms_in_building in CLASSROOMS.items():
    for room_number, r_value in classrooms_in_building.items():
        if r_value:  # Solo añade salones que tienen un r_value definido
            CLASSROOMS_LIST.append({
                "Building": building,
                "Room Number": room_number,
                "R_Value": r_value
            })

# Orders list by building and classroom number
CLASSROOMS_LIST.sort(key=lambda x: (x["Building"], x["Room Number"]))
