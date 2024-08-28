import GPUtil
import platform

def get_gpu_info():
    """
    Retrieve detailed GPU information.
    
    Returns:
        dict: A dictionary containing various GPU details.
    """
    gpu_info = {}
    
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]  # Get the first GPU
            gpu_info['name'] = gpu.name
            gpu_info['driver'] = gpu.driver
            gpu_info['memory_total'] = f"{gpu.memoryTotal} MB"
            gpu_info['memory_used'] = f"{gpu.memoryUsed} MB"
            gpu_info['memory_free'] = f"{gpu.memoryFree} MB"
            gpu_info['memory_utilization'] = f"{gpu.memoryUtil * 100:.2f}%"
            gpu_info['gpu_utilization'] = f"{gpu.load * 100:.2f}%"
            gpu_info['temperature'] = f"{gpu.temperature} °C"
        else:
            gpu_info['error'] = "No GPU detected"
    except Exception as e:
        gpu_info['error'] = f"Error retrieving GPU info: {str(e)}"
    
    # Get basic system GPU information
    gpu_info['system_info'] = platform.machine()
    
    return gpu_info

def print_gpu_info():
    """
    Print the GPU information in a formatted manner.
    """
    gpu_info = get_gpu_info()
    
    print("GPU Information:")
    if 'error' in gpu_info:
        print(f"Error: {gpu_info['error']}")
    else:
        print(f"Name: {gpu_info['name']}")
        print(f"Driver: {gpu_info['driver']}")
        print(f"Total Memory: {gpu_info['memory_total']}")
        print(f"Used Memory: {gpu_info['memory_used']}")
        print(f"Free Memory: {gpu_info['memory_free']}")
        print(f"Memory Utilization: {gpu_info['memory_utilization']}")
        print(f"GPU Utilization: {gpu_info['gpu_utilization']}")
        print(f"Temperature: {gpu_info['temperature']}")
    
    print(f"System GPU Info: {gpu_info['system_info']}")

if __name__ == "__main__":
    print_gpu_info()
