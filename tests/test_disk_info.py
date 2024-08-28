import unittest
from unittest.mock import patch, MagicMock
from src.disk_info import get_disk_info, print_disk_info

class TestDiskInfo(unittest.TestCase):

    @patch('psutil.disk_partitions')
    @patch('psutil.disk_usage')
    @patch('shutil.disk_usage')
    @patch('psutil.disk_io_counters')
    def test_get_disk_info(self, mock_io_counters, mock_shutil_usage, mock_psutil_usage, mock_partitions):
        mock_partitions.return_value = [
            MagicMock(device='/dev/sda1', mountpoint='/', fstype='ext4', opts='rw,relatime')
        ]
        mock_psutil_usage.return_value = MagicMock(
            total=100 * 1024**3,
            used=50 * 1024**3,
            free=50 * 1024**3,
            percent=50.0
        )
        mock_shutil_usage.return_value = (200 * 1024**3, 100 * 1024**3, 100 * 1024**3)
        mock_io_counters.return_value = MagicMock(
            read_count=1000,
            write_count=500,
            read_bytes=10 * 1024**2,
            write_bytes=5 * 1024**2,
            read_time=1000,
            write_time=500
        )

        info = get_disk_info()

        self.assertIn('partitions', info)
        self.assertIn('total_disk', info)
        self.assertIn('io_stats', info)
        self.assertEqual(info['partitions'][0]['device'], '/dev/sda1')
        self.assertEqual(info['partitions'][0]['total'], '100.00 GB')
        self.assertEqual(info['total_disk']['total'], '200.00 GB')
        self.assertEqual(info['io_stats']['read_count'], 1000)

    @patch('src.disk_info.get_disk_info')
    @patch('builtins.print')
    def test_print_disk_info(self, mock_print, mock_get_disk_info):
        mock_get_disk_info.return_value = {
            'total_disk': {
                'total': '200.00 GB',
                'used': '100.00 GB',
                'free': '100.00 GB',
                'percent': '50.00%'
            },
            'partitions': [{
                'device': '/dev/sda1',
                'mountpoint': '/',
                'fstype': 'ext4',
                'opts': 'rw,relatime',
                'total': '100.00 GB',
                'used': '50.00 GB',
                'free': '50.00 GB',
                'percent': '50.00%'
            }],
            'io_stats': {
                'read_count': 1000,
                'write_count': 500,
                'read_bytes': '10.00 MB',
                'write_bytes': '5.00 MB',
                'read_time': '1000 ms',
                'write_time': '500 ms'
            }
        }
        print_disk_info()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()