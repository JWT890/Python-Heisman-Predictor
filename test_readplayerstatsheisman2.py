import unittest
import csv
from heisman2 import read_player_stats
def test_read_player_stats():
    # Test that the function returns an empty list if the file does not exist
    assert read_player_stats("stats2.csv") == []

    # Test that the function returns a list of dictionaries for each player
    with open("stats2.csv", "r") as file:
        reader = csv.DictReader(file)
        player_stats = read_player_stats("stats2.csv")
        assert all([type(player) is dict for player in player_stats])

if __name__ == "__main__":
    unittest.main()