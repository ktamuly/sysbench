import GPUtil
import platform

def get_gpu_info():
    """
    Retrieve detailed GPU information for all available GPUs.
    
    Returns:
        list: A list of dictionaries containing various GPU details.
    """
    gpu_info_list = []
    
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            for i, gpu in enumerate(gpus):
                gpu_info = {}
                gpu_info['id'] = i
                gpu_info['name'] = gpu.name
                gpu_info['driver'] = gpu.driver
                gpu_info['memory_total'] = f"{gpu.memoryTotal} MB"
                gpu_info['memory_used'] = f"{gpu.memoryUsed} MB"
                gpu_info['memory_free'] = f"{gpu.memoryFree} MB"
                gpu_info['memory_utilization'] = f"{gpu.memoryUtil * 100:.2f}%"
                gpu_info['gpu_utilization'] = f"{gpu.load * 100:.2f}%"
                gpu_info['temperature'] = f"{gpu.temperature} °C"
                gpu_info_list.append(gpu_info)
        else:
            gpu_info_list.append({'error': "No GPUs detected"})
    except Exception as e:
        gpu_info_list.append({'error': f"Error retrieving GPU info: {str(e)}"})
    
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
            print(f"  Driver: {gpu_info['driver']}")
            print(f"  Total Memory: {gpu_info['memory_total']}")
            print(f"  Used Memory: {gpu_info['memory_used']}")
            print(f"  Free Memory: {gpu_info['memory_free']}")
            print(f"  Memory Utilization: {gpu_info['memory_utilization']}")
            print(f"  GPU Utilization: {gpu_info['gpu_utilization']}")
            print(f"  Temperature: {gpu_info['temperature']}")
    
    print(f"\nSystem GPU Info: {system_info}")

if __name__ == "__main__":
    print_gpu_info()
