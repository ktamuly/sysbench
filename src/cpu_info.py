import psutil
import platform
import cpuinfo

def get_cpu_info():
    """
    Retrieve detailed CPU information.
    
    Returns:
        dict: A dictionary containing various CPU details.
    """
    cpu_info = {}
    
    # Get basic CPU information
    cpu_info['processor'] = platform.processor()
    cpu_info['architecture'] = platform.machine()
    cpu_info['cores_physical'] = psutil.cpu_count(logical=False)
    cpu_info['cores_logical'] = psutil.cpu_count(logical=True)
    
    # Get CPU frequency
    try:
        cpu_freq = psutil.cpu_freq()
        cpu_info['frequency_current'] = f"{cpu_freq.current:.2f} MHz"
        cpu_info['frequency_min'] = f"{cpu_freq.min:.2f} MHz"
        cpu_info['frequency_max'] = f"{cpu_freq.max:.2f} MHz"
    except FileNotFoundError:
        cpu_info['frequency_current'] = 'N/A'
        cpu_info['frequency_min'] = 'N/A'
        cpu_info['frequency_max'] = 'N/A'
    
    # Get CPU usage
    cpu_info['usage_percent'] = psutil.cpu_percent(interval=1)
    
    # Get detailed CPU info using cpuinfo
    detailed_info = cpuinfo.get_cpu_info()
    cpu_info['brand_raw'] = detailed_info.get('brand_raw', 'N/A')
    cpu_info['vendor_id_raw'] = detailed_info.get('vendor_id_raw', 'N/A')
    cpu_info['hz_advertised_raw'] = detailed_info.get('hz_advertised_raw', 'N/A')
    cpu_info['l2_cache_size'] = detailed_info.get('l2_cache_size', 'N/A')
    cpu_info['l3_cache_size'] = detailed_info.get('l3_cache_size', 'N/A')
    
    return cpu_info

def print_cpu_info():
    """
    Print the CPU information in a formatted manner.
    """
    cpu_info = get_cpu_info()
    
    print("CPU Information:")
    print(f"Processor: {cpu_info['processor']}")
    print(f"Architecture: {cpu_info['architecture']}")
    print(f"Physical cores: {cpu_info['cores_physical']}")
    print(f"Logical cores: {cpu_info['cores_logical']}")
    print(f"Current Frequency: {cpu_info['frequency_current']}")
    print(f"Min Frequency: {cpu_info['frequency_min']}")
    print(f"Max Frequency: {cpu_info['frequency_max']}")
    print(f"Current Usage: {cpu_info['usage_percent']}%")
    print(f"Brand: {cpu_info['brand_raw']}")
    print(f"Vendor ID: {cpu_info['vendor_id_raw']}")
    print(f"Advertised Clock Speed: {cpu_info['hz_advertised_raw']}")
    print(f"L2 Cache Size: {cpu_info['l2_cache_size']}")
    print(f"L3 Cache Size: {cpu_info['l3_cache_size']}")

if __name__ == "__main__":
    print_cpu_info()
