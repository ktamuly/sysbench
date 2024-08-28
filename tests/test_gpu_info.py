import unittest
from unittest.mock import patch, MagicMock
from src.gpu_info import get_gpu_info, print_gpu_info

class TestGPUInfo(unittest.TestCase):

    @patch('GPUtil.getGPUs')
    def test_get_gpu_info(self, mock_getGPUs):
        mock_gpu1 = MagicMock()
        mock_gpu1.name = 'Test GPU 1'
        mock_gpu1.driver = '123.45'
        mock_gpu1.memoryTotal = 8192
        mock_gpu1.memoryUsed = 4096
        mock_gpu1.memoryFree = 4096
        mock_gpu1.memoryUtil = 0.5
        mock_gpu1.load = 0.75
        mock_gpu1.temperature = 60

        mock_gpu2 = MagicMock()
        mock_gpu2.name = 'Test GPU 2'
        mock_gpu2.driver = '123.45'
        mock_gpu2.memoryTotal = 16384
        mock_gpu2.memoryUsed = 8192
        mock_gpu2.memoryFree = 8192
        mock_gpu2.memoryUtil = 0.5
        mock_gpu2.load = 0.6
        mock_gpu2.temperature = 55

        mock_getGPUs.return_value = [mock_gpu1, mock_gpu2]

        info_list = get_gpu_info()

        self.assertEqual(len(info_list), 2)
        
        self.assertEqual(info_list[0]['id'], 0)
        self.assertEqual(info_list[0]['name'], 'Test GPU 1')
        self.assertEqual(info_list[0]['driver'], '123.45')
        self.assertEqual(info_list[0]['memory_total'], '8192 MB')
        self.assertEqual(info_list[0]['memory_used'], '4096 MB')
        self.assertEqual(info_list[0]['memory_free'], '4096 MB')
        self.assertEqual(info_list[0]['memory_utilization'], '50.00%')
        self.assertEqual(info_list[0]['gpu_utilization'], '75.00%')
        self.assertEqual(info_list[0]['temperature'], '60 °C')

        self.assertEqual(info_list[1]['id'], 1)
        self.assertEqual(info_list[1]['name'], 'Test GPU 2')
        self.assertEqual(info_list[1]['memory_total'], '16384 MB')
        self.assertEqual(info_list[1]['gpu_utilization'], '60.00%')
        self.assertEqual(info_list[1]['temperature'], '55 °C')

    @patch('GPUtil.getGPUs')
    def test_get_gpu_info_no_gpu(self, mock_getGPUs):
        mock_getGPUs.return_value = []

        info_list = get_gpu_info()

        self.assertEqual(len(info_list), 1)
        self.assertIn('error', info_list[0])
        self.assertEqual(info_list[0]['error'], 'No GPUs detected')

    @patch('src.gpu_info.get_gpu_info')
    @patch('builtins.print')
    def test_print_gpu_info(self, mock_print, mock_get_gpu_info):
        mock_get_gpu_info.return_value = [
            {
                'id': 0,
                'name': 'Test GPU 1',
                'driver': '123.45',
                'memory_total': '8192 MB',
                'memory_used': '4096 MB',
                'memory_free': '4096 MB',
                'memory_utilization': '50.00%',
                'gpu_utilization': '75.00%',
                'temperature': '60 °C'
            },
            {
                'id': 1,
                'name': 'Test GPU 2',
                'driver': '123.45',
                'memory_total': '16384 MB',
                'memory_used': '8192 MB',
                'memory_free': '8192 MB',
                'memory_utilization': '50.00%',
                'gpu_utilization': '60.00%',
                'temperature': '55 °C'
            }
        ]
        print_gpu_info()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()