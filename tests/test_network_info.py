import unittest
from unittest.mock import patch, MagicMock
from src.network_info import get_network_info, print_network_info

class TestNetworkInfo(unittest.TestCase):

    @patch('psutil.net_if_addrs')
    @patch('psutil.net_io_counters')
    @patch('psutil.net_connections')
    @patch('socket.gethostname')
    @patch('socket.gethostbyname')
    def test_get_network_info(self, mock_gethostbyname, mock_gethostname, mock_connections, mock_io_counters, mock_if_addrs):
        mock_if_addrs.return_value = {'eth0': [MagicMock(family='IPv4', address='192.168.1.1', netmask='255.255.255.0', broadcast='192.168.1.255')]}
        mock_io_counters.return_value = {'eth0': MagicMock(bytes_sent=1024**2, bytes_recv=1024**2, packets_sent=100, packets_recv=100, errin=0, errout=0, dropin=0, dropout=0)}
        mock_connections.return_value = [MagicMock(status='ESTABLISHED'), MagicMock(status='LISTEN')]
        mock_gethostname.return_value = 'test-host'
        mock_gethostbyname.return_value = '192.168.1.1'

        info = get_network_info()

        self.assertIn('interfaces', info)
        self.assertIn('io_stats', info)
        self.assertIn('connections', info)
        self.assertEqual(info['hostname'], 'test-host')
        self.assertEqual(info['ip_address'], '192.168.1.1')

    @patch('src.network_info.get_network_info')
    @patch('builtins.print')
    def test_print_network_info(self, mock_print, mock_get_network_info):
        mock_get_network_info.return_value = {
            'hostname': 'test-host',
            'ip_address': '192.168.1.1',
            'interfaces': {'eth0': [{'family': 'IPv4', 'address': '192.168.1.1', 'netmask': '255.255.255.0', 'broadcast': '192.168.1.255'}]},
            'io_stats': {'eth0': {'bytes_sent': '1.00 MB', 'bytes_recv': '1.00 MB', 'packets_sent': 100, 'packets_recv': 100, 'errin': 0, 'errout': 0, 'dropin': 0, 'dropout': 0}},
            'connections': {'total': 2, 'established': 1, 'listening': 1}
        }
        print_network_info()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()