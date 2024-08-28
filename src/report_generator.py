import os
import json
from datetime import datetime
from cpu_info import get_cpu_info
from memory_info import get_memory_info
from disk_info import get_disk_info
from network_info import get_network_info
from gpu_info import get_gpu_info

def generate_report():
    """
    Generate a comprehensive system report including CPU, memory, disk, network, and GPU information.
    
    Returns:
        dict: A dictionary containing the full system report.
    """
    report = {
        'timestamp': datetime.now().isoformat(),
        'cpu': get_cpu_info(),
        'memory': get_memory_info(),
        'disk': get_disk_info(),
        'network': get_network_info(),
        'gpu': get_gpu_info()
    }
    return report

def save_report(report, filename='system_report.json'):
    """
    Save the generated report to a JSON file.
    
    Args:
        report (dict): The system report to save.
        filename (str): The name of the file to save the report to.
    """
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)

def print_report(report):
    """
    Print the generated report in a formatted manner.
    
    Args:
        report (dict): The system report to print.
    """
    print("System Report:")
    print(f"Timestamp: {report['timestamp']}")
    
    print("\nCPU Information:")
    print(f"Processor: {report['cpu']['processor']}")
    print(f"Cores: {report['cpu']['cores_physical']} physical, {report['cpu']['cores_logical']} logical")
    print(f"Current Frequency: {report['cpu']['frequency_current']}")
    print(f"Usage: {report['cpu']['usage_percent']}%")
    
    print("\nMemory Information:")
    print(f"Total: {report['memory']['virtual']['total']}")
    print(f"Available: {report['memory']['virtual']['available']}")
    print(f"Used: {report['memory']['virtual']['used']}")
    
    print("\nDisk Information:")
    print(f"Total: {report['disk']['total_disk']['total']}")
    print(f"Used: {report['disk']['total_disk']['used']}")
    print(f"Free: {report['disk']['total_disk']['free']}")
    
    print("\nNetwork Information:")
    print(f"Hostname: {report['network']['hostname']}")
    print(f"IP Address: {report['network']['ip_address']}")
    
    print("\nGPU Information:")
    if 'error' in report['gpu']:
        print(f"Error: {report['gpu']['error']}")
    else:
        print(f"Name: {report['gpu']['name']}")
        print(f"Memory Total: {report['gpu']['memory_total']}")
        print(f"Memory Used: {report['gpu']['memory_used']}")

if __name__ == "__main__":
    report = generate_report()
    print_report(report)
    save_report(report)
    print(f"\nFull report saved to {os.path.abspath('system_report.json')}")
