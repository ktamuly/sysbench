import unittest
from unittest.mock import patch, MagicMock
from src.gpu_info import get_gpu_info, print_gpu_info

class TestGPUInfo(unittest.TestCase):

    @patch('GPUtil.getGPUs')
    @patch('platform.machine')
    def test_get_gpu_info(self, mock_machine, mock_getGPUs):
        mock_gpu = MagicMock()
        mock_gpu.name = 'Test GPU'
        mock_gpu.driver = '123.45'
        mock_gpu.memoryTotal = 8192
        mock_gpu.memoryUsed = 4096
        mock_gpu.memoryFree = 4096
        mock_gpu.memoryUtil = 0.5
        mock_gpu.load = 0.75
        mock_gpu.temperature = 60

        mock_getGPUs.return_value = [mock_gpu]
        mock_machine.return_value = 'x86_64'

        info = get_gpu_info()

        self.assertEqual(info['name'], 'Test GPU')
        self.assertEqual(info['driver'], '123.45')
        self.assertEqual(info['memory_total'], '8192 MB')
        self.assertEqual(info['memory_used'], '4096 MB')
        self.assertEqual(info['memory_free'], '4096 MB')
        self.assertEqual(info['memory_utilization'], '50.00%')
        self.assertEqual(info['gpu_utilization'], '75.00%')
        self.assertEqual(info['temperature'], '60 °C')
        self.assertEqual(info['system_info'], 'x86_64')

    @patch('GPUtil.getGPUs')
    @patch('platform.machine')
    def test_get_gpu_info_no_gpu(self, mock_machine, mock_getGPUs):
        mock_getGPUs.return_value = []
        mock_machine.return_value = 'x86_64'

        info = get_gpu_info()

        self.assertIn('error', info)
        self.assertEqual(info['error'], 'No GPU detected')
        self.assertEqual(info['system_info'], 'x86_64')

    @patch('src.gpu_info.get_gpu_info')
    @patch('builtins.print')
    def test_print_gpu_info(self, mock_print, mock_get_gpu_info):
        mock_get_gpu_info.return_value = {
            'name': 'Test GPU',
            'driver': '123.45',
            'memory_total': '8192 MB',
            'memory_used': '4096 MB',
            'memory_free': '4096 MB',
            'memory_utilization': '50.00%',
            'gpu_utilization': '75.00%',
            'temperature': '60 °C',
            'system_info': 'x86_64'
        }
        print_gpu_info()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()