#!/usr/bin/env python3
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda d: d['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda d: d['power'] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda x: f"* {x} *", spells)


def mage_stats(mages: list[dict]) -> dict:
    avg = 0
    try:
        avg = round(sum(m['power'] for m in mages) / len(mages), 2)
    except (ZeroDivisionError, KeyError):
        raise ValueError("Check if dict is in proper format")
    return {
        'max_power': max(mages, key=lambda d: d['power'])['power'],
        'min_power': min(mages, key=lambda d: d['power'])['power'],
        'avg_power': avg
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Storm Crown', 'power': 69, 'type': 'accessory'},
        {'name': 'Shadow Blade', 'power': 92, 'type': 'relic'},
        {'name': 'Crystal Orb', 'power': 74, 'type': 'accessory'},
        {'name': 'Crystal Orb', 'power': 83, 'type': 'armor'}
    ]
    mages = [
        {'name': 'Luna', 'power': 86, 'element': 'lightning'},
        {'name': 'Storm', 'power': 90, 'element': 'lightning'},
        {'name': 'Sage', 'power': 50, 'element': 'light'},
        {'name': 'Jordan', 'power': 88, 'element': 'earth'},
        {'name': 'Jordan', 'power': 95, 'element': 'wind'}
    ]
    spells = ['lightning', 'meteor', 'darkness', 'tsunami']

    print("\nTesting artifact sorter...")
    try:
        artifact_sort = artifact_sorter(artifacts)
        first = artifact_sort[0]
        second = artifact_sort[1]
        print(
            f"{first['name']} ({first['power']} power) comes before "
            f"{second['name']} ({second['power']} power)"
        )

        print("\nTesting power filter...")
        ultra_power = power_filter(mages, 76)
        print(*[x['name'] for x in ultra_power], sep=', ')

        print("\nTesting spell transformer...")
        transpell = spell_transformer(spells)
        print(*transpell)

        print("\nTesting mage_stats...")
        m_stat = mage_stats(mages)
        for k, v in m_stat.items():
            print(f"{k}:\n{v}")
    except (IndexError, KeyError, ValueError) as e:
        print("Invalid input. Use gernerator.tar.gz downloadable from Intra")
        print(f"{type(e).__name__}: {e}")
    except Exception as e:
        print("Unexpected error! Good job finding it!!")
        print(f"{type(e).__name__}: {e}")
