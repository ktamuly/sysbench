import psutil

def get_memory_info():
    """
    Retrieve detailed memory information.
    
    Returns:
        dict: A dictionary containing various memory details.
    """
    memory_info = {}
    
    # Get virtual memory information
    virtual_memory = psutil.virtual_memory()
    memory_info['virtual'] = {
        'total': f"{virtual_memory.total / (1024**3):.2f} GB",
        'available': f"{virtual_memory.available / (1024**3):.2f} GB",
        'used': f"{virtual_memory.used / (1024**3):.2f} GB",
        'free': f"{virtual_memory.free / (1024**3):.2f} GB",
        'percent': f"{virtual_memory.percent}%"
    }
    
    # Get swap memory information
    try:
        swap_memory = psutil.swap_memory()
        memory_info['swap'] = {
            'total': f"{swap_memory.total / (1024**3):.2f} GB",
            'used': f"{swap_memory.used / (1024**3):.2f} GB",
            'free': f"{swap_memory.free / (1024**3):.2f} GB",
            'percent': f"{swap_memory.percent}%"
        }
    except Exception as e:
        memory_info['swap'] = {
            'total': 'N/A',
            'used': 'N/A',
            'free': 'N/A',
            'percent': 'N/A'
        }
        print(f"Warning: Unable to retrieve swap memory information. Error: {str(e)}")
    
    return memory_info

def print_memory_info():
    """
    Print the memory information in a formatted manner.
    """
    memory_info = get_memory_info()
    
    print("Memory Information:")
    print("\nVirtual Memory:")
    print(f"Total: {memory_info['virtual']['total']}")
    print(f"Available: {memory_info['virtual']['available']}")
    print(f"Used: {memory_info['virtual']['used']}")
    print(f"Free: {memory_info['virtual']['free']}")
    print(f"Usage: {memory_info['virtual']['percent']}")
    
    print("\nSwap Memory:")
    print(f"Total: {memory_info['swap']['total']}")
    print(f"Used: {memory_info['swap']['used']}")
    print(f"Free: {memory_info['swap']['free']}")
    print(f"Usage: {memory_info['swap']['percent']}")

if __name__ == "__main__":
    print_memory_info()
