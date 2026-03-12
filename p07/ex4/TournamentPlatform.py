from typing import Dict, List
from ex4.Rankable import Rankable
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform for running card tournaments."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.participants: List[TournamentCard] = []
        self.matches_played = 0

    def register_participant(self, card: TournamentCard) -> Dict:
        """Register a card for the tournament."""
        self.participants.append(card)
        return {
            "registered": card.name,
            "rank_score": card.get_rank_score(),
            "total_participants": len(self.participants)
        }

    def run_match(self, card1: TournamentCard, card2: TournamentCard) -> Dict:
        """Run a match between two cards."""
        score1 = card1.get_rank_score()
        score2 = card2.get_rank_score()

        if score1 > score2:
            winner, loser = card1, card2
        elif score2 > score1:
            winner, loser = card2, card1
        else:
            # Tie-breaker: higher attack wins
            if card1._attack >= card2._attack:
                winner, loser = card1, card2
            else:
                winner, loser = card2, card1

        winner.record_match(True)
        loser.record_match(False)
        self.matches_played += 1

        return {
            "match": self.matches_played,
            "winner": winner.name,
            "loser": loser.name,
            "winner_score": winner.get_rank_score(),
            "loser_score": loser.get_rank_score()
        }

    def get_rankings(self) -> List[Dict]:
        """Get current rankings."""
        sorted_cards = sorted(
            self.participants,
            key=lambda c: c.get_rank_score(),
            reverse=True
        )
        return [
            {
                "rank": i + 1,
                "card": card.name,
                "score": card.get_rank_score(),
                "record": card.get_record()
            }
            for i, card in enumerate(sorted_cards)
        ]

    def get_tournament_summary(self) -> Dict:
        """Get tournament summary."""
        return {
            "tournament_name": self.name,
            "total_participants": len(self.participants),
            "matches_played": self.matches_played,
            "rankings": self.get_rankings()
        }
