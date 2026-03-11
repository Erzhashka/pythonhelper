#!/usr/bin/env python3

print("=== Game Analytics Dashboard ===")
print()

players_data = [
    {'name': 'alice', 'score': 2300, 'level': 15, 'region': 'north'},
    {'name': 'bob', 'score': 1800, 'level': 12, 'region': 'east'},
    {'name': 'charlie', 'score': 2150, 'level': 18, 'region': 'north'},
    {'name': 'diana', 'score': 2050, 'level': 14, 'region': 'central'},
    {'name': 'eve', 'score': 1500, 'level': 8, 'region': 'east'},
    {'name': 'frank', 'score': 1950, 'level': 11, 'region': 'central'}
]

achievements = {
    'alice': ['first_kill', 'level_10', 'boss_slayer', 'treasure_hunter', 'speed_demon'],
    'bob': ['first_kill', 'level_10', 'collector'],
    'charlie': ['first_kill', 'level_10', 'boss_slayer', 'perfectionist', 'explorer', 'speed_demon', 'legend'],
    'diana': ['level_10', 'treasure_hunter', 'collector', 'explorer'],
    'eve': ['first_kill', 'collector'],
    'frank': ['first_kill', 'level_10', 'boss_slayer']
}

scores = [2300, 1800, 2150, 2050, 1500, 1950]

print("=== List Comprehension Examples ===")

high_scorers = [p['name'] for p in players_data if p['score'] > 2000]
print(f"High scorers (>2000): {high_scorers}")

scores_doubled = [s * 2 for s in scores]
print(f"Scores doubled: {scores_doubled}")

active_players = [p['name'] for p in players_data if p['level'] >= 10]
print(f"Active players (level 10+): {active_players}")

score_categories = ['high' if s > 2000 else 'medium' if s > 1700 else 'low' for s in scores]
print(f"Score categories: {score_categories}")

north_players = [p['name'] for p in players_data if p['region'] == 'north']
print(f"North region players: {north_players}")

print()
print("=== Dict Comprehension Examples ===")

player_scores = {p['name']: p['score'] for p in players_data}
print(f"Player scores: {player_scores}")

player_levels = {p['name']: p['level'] for p in players_data}
print(f"Player levels: {player_levels}")

achievement_counts = {name: len(achs) for name, achs in achievements.items()}
print(f"Achievement counts: {achievement_counts}")

high_level_scores = {p['name']: p['score'] for p in players_data if p['level'] > 12}
print(f"High level player scores: {high_level_scores}")

score_to_player = {p['score']: p['name'] for p in players_data}
print(f"Score to player mapping: {score_to_player}")

print()
print("=== Set Comprehension Examples ===")

unique_regions = {p['region'] for p in players_data}
print(f"Unique regions: {unique_regions}")

all_achievements = {ach for player_achs in achievements.values() for ach in player_achs}
print(f"All unique achievements: {all_achievements}")

high_scorer_names = {p['name'] for p in players_data if p['score'] > 1900}
print(f"High scorer names: {high_scorer_names}")

boss_slayers = {name for name, achs in achievements.items() if 'boss_slayer' in achs}
print(f"Players with boss_slayer: {boss_slayers}")

unique_levels = {p['level'] for p in players_data}
print(f"Unique levels: {sorted(unique_levels)}")

print()
print("=== Combined Analysis ===")

total_players = len(players_data)
print(f"Total players: {total_players}")

total_achievements = len(all_achievements)
print(f"Total unique achievements: {total_achievements}")

all_scores = [p['score'] for p in players_data]
average_score = sum(all_scores) / len(all_scores)
print(f"Average score: {average_score}")

highest_score = max(all_scores)
lowest_score = min(all_scores)
print(f"Score range: {lowest_score} - {highest_score}")

top_player = [p for p in players_data if p['score'] == highest_score][0]
top_name = top_player['name']
top_ach_count = len(achievements[top_name])
print(f"Top performer: {top_name} ({highest_score} points, {top_ach_count} achievements)")

score_name_pairs = [(p['score'], p['name']) for p in players_data]
sorted_pairs = sorted(score_name_pairs, reverse=True)
ranking = [pair[1] for pair in sorted_pairs]
print(f"Player ranking: {ranking}")

print()
print("=== Region Analysis ===")

region_counts = {region: len([p for p in players_data if p['region'] == region]) for region in unique_regions}
print(f"Players per region: {region_counts}")

region_scores = {region: sum([p['score'] for p in players_data if p['region'] == region]) for region in unique_regions}
print(f"Total scores per region: {region_scores}")

print()
print("=== Achievement Analysis ===")

common_achievements = {ach for ach in all_achievements if len([name for name, achs in achievements.items() if ach in achs]) >= 4}
print(f"Common achievements (4+ players): {common_achievements}")

rare_achievements = {ach for ach in all_achievements if len([name for name, achs in achievements.items() if ach in achs]) == 1}
print(f"Rare achievements (1 player): {rare_achievements}")

most_achievements = max(achievement_counts.values())
top_achievers = [name for name, count in achievement_counts.items() if count == most_achievements]
print(f"Most achievements ({most_achievements}): {top_achievers}")
