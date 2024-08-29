import pynvml
import platform

def get_gpu_info():
    """
    Retrieve detailed GPU information for all available NVIDIA GPUs using pynvml.
    
    Returns:
        list: A list of dictionaries containing various GPU details.
    """
    gpu_info_list = []
    
    try:
        pynvml.nvmlInit()
        num_gpus = pynvml.nvmlDeviceGetCount()
        
        if num_gpus > 0:
            for i in range(num_gpus):
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                gpu_info = {}
                
                gpu_info['id'] = i
                gpu_info['name'] = pynvml.nvmlDeviceGetName(handle).decode('utf-8')
                gpu_info['uuid'] = pynvml.nvmlDeviceGetUUID(handle).decode('utf-8')
                gpu_info['serial'] = pynvml.nvmlDeviceGetSerial(handle).decode('utf-8')
                
                memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
                gpu_info['memory_total'] = f"{memory.total / 1024**2:.2f} MB"
                gpu_info['memory_used'] = f"{memory.used / 1024**2:.2f} MB"
                gpu_info['memory_free'] = f"{memory.free / 1024**2:.2f} MB"
                gpu_info['memory_utilization'] = f"{(memory.used / memory.total) * 100:.2f}%"
                
                utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
                gpu_info['gpu_utilization'] = f"{utilization.gpu}%"
                gpu_info['memory_utilization'] = f"{utilization.memory}%"
                
                gpu_info['temperature'] = f"{pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)} °C"
                gpu_info['power_usage'] = f"{pynvml.nvmlDeviceGetPowerUsage(handle) / 1000:.2f} W"
                gpu_info['power_limit'] = f"{pynvml.nvmlDeviceGetPowerManagementLimit(handle) / 1000:.2f} W"
                
                gpu_info['fan_speed'] = f"{pynvml.nvmlDeviceGetFanSpeed(handle)}%"
                gpu_info['performance_state'] = pynvml.nvmlDeviceGetPerformanceState(handle)
                
                gpu_info['clock_speeds'] = {
                    'graphics': f"{pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)} MHz",
                    'sm': f"{pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_SM)} MHz",
                    'memory': f"{pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_MEM)} MHz",
                }
                
                gpu_info['driver_version'] = pynvml.nvmlSystemGetDriverVersion().decode('utf-8')
                gpu_info['cuda_version'] = pynvml.nvmlSystemGetCudaDriverVersion_v2()
                
                gpu_info_list.append(gpu_info)
        else:
            gpu_info_list.append({'error': "No NVIDIA GPUs detected"})
    except pynvml.NVMLError as e:
        gpu_info_list.append({'error': f"NVML Error: {str(e)}"})
    except Exception as e:
        gpu_info_list.append({'error': f"Error retrieving GPU info: {str(e)}"})
    finally:
        try:
            pynvml.nvmlShutdown()
        except:
            pass
    
    return gpu_info_list

def print_gpu_info():
    """
    Print the GPU information for all GPUs in a formatted manner.
    """
    gpu_info_list = get_gpu_info()
    system_info = platform.machine()
    
    print("GPU Information:")
    if 'error' in gpu_info_list[0]:
        print(f"Error: {gpu_info_list[0]['error']}")
    else:
        for gpu_info in gpu_info_list:
            print(f"\nGPU {gpu_info['id']}:")
            print(f"  Name: {gpu_info['name']}")
            print(f"  Driver Version: {gpu_info['driver_version']}")
            print(f"  Total Memory: {gpu_info['memory_total']}")
            print(f"  Used Memory: {gpu_info['memory_used']}")
            print(f"  Free Memory: {gpu_info['memory_free']}")
            print(f"  Memory Utilization: {gpu_info['memory_utilization']}")
            print(f"  GPU Utilization: {gpu_info['gpu_utilization']}")
            print(f"  Temperature: {gpu_info['temperature']}")
    
    print(f"\nSystem GPU Info: {system_info}")

if __name__ == "__main__":
    print_gpu_info()
