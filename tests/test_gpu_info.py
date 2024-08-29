import unittest
from unittest.mock import patch, MagicMock
from src.gpu_info import get_gpu_info, print_gpu_info

class TestGPUInfo(unittest.TestCase):

    @patch('pynvml.nvmlInit')
    @patch('pynvml.nvmlDeviceGetCount')
    @patch('pynvml.nvmlDeviceGetHandleByIndex')
    @patch('pynvml.nvmlDeviceGetName')
    @patch('pynvml.nvmlDeviceGetUUID')
    @patch('pynvml.nvmlDeviceGetSerial')
    @patch('pynvml.nvmlDeviceGetMemoryInfo')
    @patch('pynvml.nvmlDeviceGetUtilizationRates')
    @patch('pynvml.nvmlDeviceGetTemperature')
    @patch('pynvml.nvmlDeviceGetPowerUsage')
    @patch('pynvml.nvmlDeviceGetPowerManagementLimit')
    @patch('pynvml.nvmlDeviceGetFanSpeed')
    @patch('pynvml.nvmlDeviceGetPerformanceState')
    @patch('pynvml.nvmlDeviceGetClockInfo')
    @patch('pynvml.nvmlSystemGetDriverVersion')
    @patch('pynvml.nvmlSystemGetCudaDriverVersion_v2')
    @patch('pynvml.nvmlShutdown')
    def test_get_gpu_info(self, mock_shutdown, mock_cuda_version, mock_driver_version, 
                          mock_clock_info, mock_perf_state, mock_fan_speed, mock_power_limit, 
                          mock_power_usage, mock_temp, mock_utilization, mock_memory_info, 
                          mock_serial, mock_uuid, mock_name, mock_handle, mock_count, mock_init):
        mock_count.return_value = 2
        mock_name.return_value = b'Test GPU'
        mock_uuid.return_value = b'GPU-12345678-90ab-cdef-ghij-klmnopqrstuv'
        mock_serial.return_value = b'SN12345'
        mock_memory_info.return_value = MagicMock(total=8589934592, used=4294967296, free=4294967296)
        mock_utilization.return_value = MagicMock(gpu=75, memory=50)
        mock_temp.return_value = 60
        mock_power_usage.return_value = 150000
        mock_power_limit.return_value = 250000
        mock_fan_speed.return_value = 50
        mock_perf_state.return_value = 0
        mock_clock_info.return_value = 1500
        mock_driver_version.return_value = b'450.36.06'
        mock_cuda_version.return_value = 11000

        info_list = get_gpu_info()

        self.assertEqual(len(info_list), 2)
        
        self.assertEqual(info_list[0]['id'], 0)
        self.assertEqual(info_list[0]['name'], 'Test GPU')
        self.assertEqual(info_list[0]['uuid'], 'GPU-12345678-90ab-cdef-ghij-klmnopqrstuv')
        self.assertEqual(info_list[0]['serial'], 'SN12345')
        self.assertEqual(info_list[0]['memory_total'], '8192.00 MB')
        self.assertEqual(info_list[0]['memory_used'], '4096.00 MB')
        self.assertEqual(info_list[0]['memory_free'], '4096.00 MB')
        self.assertEqual(info_list[0]['memory_utilization'], '50.00%')
        self.assertEqual(info_list[0]['gpu_utilization'], '75%')
        self.assertEqual(info_list[0]['temperature'], '60 °C')
        self.assertEqual(info_list[0]['power_usage'], '150.00 W')
        self.assertEqual(info_list[0]['power_limit'], '250.00 W')
        self.assertEqual(info_list[0]['fan_speed'], '50%')
        self.assertEqual(info_list[0]['performance_state'], 0)
        self.assertEqual(info_list[0]['clock_speeds']['graphics'], '1500 MHz')
        self.assertEqual(info_list[0]['driver_version'], '450.36.06')
        self.assertEqual(info_list[0]['cuda_version'], 11000)

    @patch('pynvml.nvmlInit')
    @patch('pynvml.nvmlDeviceGetCount')
    @patch('pynvml.nvmlShutdown')
    def test_get_gpu_info_no_gpu(self, mock_shutdown, mock_count, mock_init):
        mock_count.return_value = 0

        info_list = get_gpu_info()

        self.assertEqual(len(info_list), 1)
        self.assertIn('error', info_list[0])
        self.assertEqual(info_list[0]['error'], 'No NVIDIA GPUs detected')

    @patch('src.gpu_info.get_gpu_info')
    @patch('builtins.print')
    def test_print_gpu_info(self, mock_print, mock_get_gpu_info):
        mock_get_gpu_info.return_value = [
            {
                'id': 0,
                'name': 'Test GPU 1',
                'driver_version': '450.36.06',
                'memory_total': '8192.00 MB',
                'memory_used': '4096.00 MB',
                'memory_free': '4096.00 MB',
                'memory_utilization': '50.00%',
                'gpu_utilization': '75%',
                'temperature': '60 °C'
            },
            {
                'id': 1,
                'name': 'Test GPU 2',
                'driver_version': '450.36.06',
                'memory_total': '16384.00 MB',
                'memory_used': '8192.00 MB',
                'memory_free': '8192.00 MB',
                'memory_utilization': '50.00%',
                'gpu_utilization': '60%',
                'temperature': '55 °C'
            }
        ]
        print_gpu_info()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()