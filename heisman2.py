import csv

def read_player_stats(filename):
    player_stats = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stats.append(row)
    return player_stats

def heisman_predictor(player_stats):
    # Calculate player's total score based on their stats
    total_scores = []
    for player in player_stats:
        total_score = int(player['G']) + int(player['Cmp']) + int(player['TD']) + int(player['Yds'])
        total_scores.append(total_score)

    # Check if each player has enough stats to be considered for the Heisman
    results = []
    for i in range(len(player_stats)):
        if total_scores[i] >= 1000:
            results.append(f"{player_stats[i]['Player']} is a strong contender for the Heisman Trophy!")
        else:
            results.append(f"{player_stats[i]['Player']} needs to improve their stats to be considered for the Heisman.")
    
    return results

# Example usage
filename = 'stats2.csv'
player_stats = read_player_stats(filename)
results = heisman_predictor(player_stats)
for result in results:
    print(result)