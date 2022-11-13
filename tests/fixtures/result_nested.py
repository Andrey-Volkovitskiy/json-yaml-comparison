exp_result = [
    {
        'name': ('a', 'a'),
        'value': (10, 100),
        'children': None
    },
    {
        'name': ('b', None),
        'value': (20, None),
        'children': None
    },
    {
        'name': ('c', 'c'),
        'value': (None, None),
        'children': [
            {
                'name': ('d', 'd`'),
                'value': (30, 300),
                'children': None
            },
            {
                'name': ('e', 'e'),
                'value': ({'f': 40}, 700),
                'children': None
            }
        ]
    },
    {
        'name': (None, 'g'),
        'value': (None, {'h': 800}),
        'children': None
    }
]


file_3 = {
    "a": 10,
    "b": 20,
    "c": {
        "d": 30,
        "e": {
            "f": 40
        }
    }
}

file_4 = {
    "a": 100,
    "c": {
        "d": 300,
        "e": 700
    },
    "g": {
        "h": 800
    }
}
