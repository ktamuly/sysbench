import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.report_generator import generate_report, save_report, print_report

class TestReportGenerator(unittest.TestCase):

    @patch('src.report_generator.get_cpu_info')
    @patch('src.report_generator.get_memory_info')
    @patch('src.report_generator.get_disk_info')
    @patch('src.report_generator.get_network_info')
    @patch('src.report_generator.get_gpu_info')
    def test_generate_report(self, mock_gpu, mock_network, mock_disk, mock_memory, mock_cpu):
        mock_cpu.return_value = {'cpu': 'info'}
        mock_memory.return_value = {'memory': 'info'}
        mock_disk.return_value = {'disk': 'info'}
        mock_network.return_value = {'network': 'info'}
        mock_gpu.return_value = {'gpu': 'info'}

        report = generate_report()

        self.assertIn('timestamp', report)
        self.assertEqual(report['cpu'], {'cpu': 'info'})
        self.assertEqual(report['memory'], {'memory': 'info'})
        self.assertEqual(report['disk'], {'disk': 'info'})
        self.assertEqual(report['network'], {'network': 'info'})
        self.assertEqual(report['gpu'], {'gpu': 'info'})

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('json.dump')
    def test_save_report(self, mock_json_dump, mock_open):
        report = {'test': 'report'}
        save_report(report, 'test.json')
        mock_open.assert_called_with('test.json', 'w')
        mock_json_dump.assert_called_with(report, mock_open(), indent=4)

    @patch('builtins.print')
    def test_print_report(self, mock_print):
        report = {
            'timestamp': '2023-01-01T00:00:00',
            'cpu': {'processor': 'Test CPU', 'cores_physical': 4, 'cores_logical': 8, 'frequency_current': '3.2 GHz', 'usage_percent': 50},
            'memory': {'virtual': {'total': '16 GB', 'available': '8 GB', 'used': '8 GB'}},
            'disk': {'total_disk': {'total': '1 TB', 'used': '500 GB', 'free': '500 GB'}},
            'network': {'hostname': 'test-host', 'ip_address': '192.168.1.1'},
            'gpu': {'name': 'Test GPU', 'memory_total': '8 GB', 'memory_used': '4 GB'}
        }
        print_report(report)
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()