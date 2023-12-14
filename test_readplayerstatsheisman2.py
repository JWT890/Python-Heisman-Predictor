import unittest
import csv
from unittest.mock import patch, mock_open
from heisman2 import read_player_stats

def test_read_player_stats():
    # Test that the function returns an empty list if the file does not exist
    with patch('builtins.open', mock_open(read_data='')) as mock_file:
        assert read_player_stats('file.csv') == []

    # Test that the function returns a list of dictionaries for each row in the CSV file
    with patch('builtins.open', mock_open(read_data='Player,G,Cmp,Yds,TD\nJoe Montana,16,270,4067,50\nRoger Staubach,14,223,3443,34\n')) as mock_file:
        expected_result = [
            {'Player': 'Joe Montana', 'G': '16', 'Cmp': '270', 'Yds': '4067', 'TD': '50'},
            {'Player': 'Roger Staubach', 'G': '14', 'Cmp': '223', 'Yds': '3443', 'TD': '34'}
        ]
        assert read_player_stats('file.csv') == expected_result

if __name__ == '__main__':
    unittest.main()