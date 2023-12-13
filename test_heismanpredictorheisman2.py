import unittest
from heisman2 import heisman_predictor

def test_heisman_predictor():
    # Test data
    player_stats = [
        {'Player': 'Jayden Daniels', 'G': '8', 'Cmp': '18', 'TD': '10', 'Yds': '1500'},
        {'Player': 'Bo Nix', 'G': '10', 'Cmp': '15', 'TD': '15', 'Yds': '1200'},
        {'Player': 'Jalen Milroe', 'G': '12', 'Cmp': '12', 'TD': '5', 'Yds': '1000'},
        {'Player': 'Zion Webb', 'G': '6', 'Cmp': '10', 'TD': '5', 'Yds': '800'},
        {'Player': 'Joe Milton', 'G': '8', 'Cmp': '15', 'TD': '10', 'Yds': '900'},
    ]

    # Expected results
    expected_results = [
        'Jalen Milroe is a strong contender for the Heisman Trophy!',
        'Bo Nix is a strong contender for the Heisman Trophy!',
        'Joe Milton is a strong contender for the Heisman Trophy!',
        'Zion Webb needs to improve their stats to be considered for the Heisman.',
        'Jayden Daniels is this years potential Heisman winner!',
    ]

    # Actual results
    actual_results = heisman_predictor(player_stats)

    # Check results
    assert actual_results == expected_results

if __name__ == '__main__':
    unittest.main()