import unittest
from unittest.mock import patch, MagicMock
from src.memory_info import get_memory_info, print_memory_info

class TestMemoryInfo(unittest.TestCase):

    @patch('psutil.virtual_memory')
    @patch('psutil.swap_memory')
    def test_get_memory_info(self, mock_swap_memory, mock_virtual_memory):
        mock_virtual_memory.return_value = MagicMock(
            total=16 * 1024**3,
            available=8 * 1024**3,
            used=8 * 1024**3,
            free=8 * 1024**3,
            percent=50.0
        )
        mock_swap_memory.return_value = MagicMock(
            total=8 * 1024**3,
            used=2 * 1024**3,
            free=6 * 1024**3,
            percent=25.0
        )

        info = get_memory_info()

        self.assertIn('virtual', info)
        self.assertIn('swap', info)
        self.assertEqual(info['virtual']['total'], '16.00 GB')
        self.assertEqual(info['virtual']['available'], '8.00 GB')
        self.assertEqual(info['virtual']['used'], '8.00 GB')
        self.assertEqual(info['virtual']['free'], '8.00 GB')
        self.assertEqual(info['virtual']['percent'], '50.0%')
        self.assertEqual(info['swap']['total'], '8.00 GB')
        self.assertEqual(info['swap']['used'], '2.00 GB')
        self.assertEqual(info['swap']['free'], '6.00 GB')
        self.assertEqual(info['swap']['percent'], '25.0%')

    @patch('src.memory_info.get_memory_info')
    @patch('builtins.print')
    def test_print_memory_info(self, mock_print, mock_get_memory_info):
        mock_get_memory_info.return_value = {
            'virtual': {
                'total': '16.00 GB',
                'available': '8.00 GB',
                'used': '8.00 GB',
                'free': '8.00 GB',
                'percent': '50.0%'
            },
            'swap': {
                'total': '8.00 GB',
                'used': '2.00 GB',
                'free': '6.00 GB',
                'percent': '25.0%'
            }
        }
        print_memory_info()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()