#!/usr/bin/env python3

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def make_tournament(lineup: TournamentPlatform) -> None:
    cards_data: list[tuple[str, int, str, str, int, int, str, int]] = [
        ("Fire Dragon", 8, "legend",    "dragon_001",  9, 60, "dragon",  9500),
        ("Ice Golem",   6, "rare",      "golem_042",   5, 80, "witch",   7800),
        ("Shade Rogue", 4, "special",   "rogue_017",   7, 35, "royal",   3600),
        ("Storm Mage",  5, "rare",      "mage_088",    6, 40, "witch",   7200),
        ("Holy Knight", 3, "common",    "knight_023",  4, 70, "bishop",  1500),
        ("Plague Rat",  1, "common",    "rat_005",     2, 15, "necro",    800),
        ("Phoenix",     7, "legend",    "phoenix_099", 8, 55, "dragon", 12000),
        ("Void Wraith", 5, "rare",      "wraith_034",  6, 45, "necro",   6500),
        ("Soul Dealer", 7, "rare",      "dealer_011",  5, 90, "vampire", 7100),
        ("Light Hawk",  4, "special",   "hawk_056",    8, 30, "elf",     3900),
        ("Vertex Car",  6, "rare",      "car_078",     7, 40, "nemesis", 5800),
        ("Bone Archer", 3, "common",    "archer_019",  6, 25, "necro",   1800),
        ("Sea Serpent", 6, "rare",      "serpent_063", 7, 65, "dragon",  6900),
        ("Aluzard",     9, "legend",    "zard_002",   10, 75, "vampire", 9900),
    ]
    # lineup._cards = [TournamentCard(*param) for param in cards_data]
    # Genius but too bad, doesn't fit the bill
    for param in cards_data:
        lineup.register_card(TournamentCard(*param))


if __name__ == "__main__":
    try:
        arena = TournamentPlatform()
        print("\n=== DataDeck Tournament Platform ===")

        print("\nRegistering Tournament Cards...")
        make_tournament(arena)
        for card in arena._cards:
            print(f"\n{card.name} (ID: {card.id}):")
            rank_info = card.get_rank_info()
            for k, v in rank_info.items():
                print(f"- {k.capitalize()}: {v}")

        print("\nCreating tournament match...")
        losers = []
        while len(arena._cards) > 1:
            result = arena.create_match(arena._cards[0].id, arena._cards[1].id)
            print(f"Match result: {result}")
            for i, card in enumerate(arena._cards):
                if card.id == result['loser']:
                    losers.append(arena._cards.pop(i))
                    break
        arena._cards += losers

        leaderboard = arena.get_leaderboard()
        print("\nTournament Leaderboard:")
        for i, entry in enumerate(leaderboard, 1):
            n, rate, rec = entry
            print(f"{i}. {n} - Rating: {rate} ({rec})")

        print("\nPlatform Report:")
        print(f"{arena.generate_tournament_report()}")

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(f"Error: {e}")
