#!/usr/bin/env python3

from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform():
    def __init__(self) -> None:
        self._cards = []
        self.matches = 0
        self.activity = "dead"
        self.total_cards = 0

    def register_card(self, card: TournamentCard) -> str:
        """Adds card to self.cards if it is a valid card

        Args:
            card (TournamentCard): Card to register

        Returns:
            str: Result of registration
        """
        if isinstance(card, TournamentCard):
            self._cards.append(card)
            self.total_cards += 1
            return "Card registered"
        else:
            return "Failed to register"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Randomly chooses winner from two contestants chosen from self.cards

        Args:
            card1_id (str): Challenger
            card2_id (str): Defender

        Raises:
            ValueError: If card_ids are not in self.cards

        Returns:
            dict: Result of match
        """
        challenger = None
        defender = None
        for card in self._cards:
            if card.id == card1_id:
                challenger = card
            elif card.id == card2_id:
                defender = card
        if challenger and defender:
            winner = random.choice([challenger, defender])
            loser = challenger if winner is defender else defender
            self.matches += 1
            self.activity = "active"
            winner.calculate_rating()
            loser.calculate_rating()
            winner.wins += 1
            loser.losses += 1
            winner.update_wins(winner.wins)
            loser.update_losses(loser.losses)
        else:
            raise ValueError("Card_ids have not applied for tournament")
        return {
            'winner': winner.id,
            'loser': loser.id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating,
        }

    def get_leaderboard(self) -> list:
        """For every three cards, one card will enter the leaderboard

        Returns:
            list: All cards in leaderboard, showing name, rating, and record
        """
        top_ratings = len(self._cards) // 3
        rankers = []
        if top_ratings:
            for i in range(top_ratings):
                max_rating_index = max(
                    range(len(self._cards)),
                    key=lambda i: self._cards[i].rating
                )
                rankers.append(self._cards.pop(max_rating_index))
        else:
            raise ValueError("Not enough cards in tournament")
        return [(c.name, c.rating, c.record) for c in rankers]

    def generate_tournament_report(self) -> dict:
        card_count = len(self._cards)
        avg = round(
            sum(c.rating for c in self._cards) / card_count
        ) if card_count else 0
        return {
            'total_cards': self.total_cards,
            'matches_played': self.matches,
            'avg_rating': avg,
            'platform_status': self.activity,
        }
