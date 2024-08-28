import unittest
from unittest.mock import patch, MagicMock
from src.cpu_info import get_cpu_info, print_cpu_info

class TestCPUInfo(unittest.TestCase):

    @patch('platform.processor')
    @patch('platform.machine')
    @patch('psutil.cpu_count')
    @patch('psutil.cpu_freq')
    @patch('psutil.cpu_percent')
    @patch('cpuinfo.get_cpu_info')
    def test_get_cpu_info(self, mock_cpuinfo, mock_cpu_percent, mock_cpu_freq, mock_cpu_count, mock_machine, mock_processor):
        mock_processor.return_value = 'Test Processor'
        mock_machine.return_value = 'x86_64'
        mock_cpu_count.side_effect = [4, 8]
        mock_cpu_freq.return_value = MagicMock(current=3200, min=2200, max=3800)
        mock_cpu_percent.return_value = 25.0
        mock_cpuinfo.return_value = {
            'brand_raw': 'Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz',
            'vendor_id_raw': 'GenuineIntel',
            'hz_advertised_raw': '1.3000 GHz',
            'l2_cache_size': 1048576,
            'l3_cache_size': 8388608
        }

        info = get_cpu_info()

        self.assertEqual(info['processor'], 'Test Processor')
        self.assertEqual(info['architecture'], 'x86_64')
        self.assertEqual(info['cores_physical'], 4)
        self.assertEqual(info['cores_logical'], 8)
        self.assertEqual(info['frequency_current'], '3200.00 MHz')
        self.assertEqual(info['frequency_min'], '2200.00 MHz')
        self.assertEqual(info['frequency_max'], '3800.00 MHz')
        self.assertEqual(info['usage_percent'], 25.0)
        self.assertEqual(info['brand_raw'], 'Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz')
        self.assertEqual(info['vendor_id_raw'], 'GenuineIntel')
        self.assertEqual(info['hz_advertised_raw'], '1.3000 GHz')
        self.assertEqual(info['l2_cache_size'], 1048576)
        self.assertEqual(info['l3_cache_size'], 8388608)

    @patch('src.cpu_info.get_cpu_info')
    @patch('builtins.print')
    def test_print_cpu_info(self, mock_print, mock_get_cpu_info):
        mock_get_cpu_info.return_value = {
            'processor': 'Test Processor',
            'architecture': 'x86_64',
            'cores_physical': 4,
            'cores_logical': 8,
            'frequency_current': '3200.00 MHz',
            'frequency_min': '2200.00 MHz',
            'frequency_max': '3800.00 MHz',
            'usage_percent': 25.0,
            'brand_raw': 'Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz',
            'vendor_id_raw': 'GenuineIntel',
            'hz_advertised_raw': '1.3000 GHz',
            'l2_cache_size': 1048576,
            'l3_cache_size': 8388608
        }
        print_cpu_info()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()