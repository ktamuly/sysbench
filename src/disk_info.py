import psutil
import shutil

def get_disk_info():
    """
    Retrieve detailed disk information.
    
    Returns:
        dict: A dictionary containing various disk details.
    """
    disk_info = {}
    
    # Get partitions
    partitions = psutil.disk_partitions()
    disk_info['partitions'] = []
    
    for partition in partitions:
        partition_info = {
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'fstype': partition.fstype,
            'opts': partition.opts
        }
        
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            partition_info.update({
                'total': f"{usage.total / (1024**3):.2f} GB",
                'used': f"{usage.used / (1024**3):.2f} GB",
                'free': f"{usage.free / (1024**3):.2f} GB",
                'percent': f"{usage.percent}%"
            })
        except PermissionError:
            # This can happen if the disk isn't ready or you don't have permission
            partition_info.update({
                'total': 'N/A',
                'used': 'N/A',
                'free': 'N/A',
                'percent': 'N/A'
            })
        
        disk_info['partitions'].append(partition_info)
    
    # Get total disk usage
    total, used, free = shutil.disk_usage("/")
    disk_info['total_disk'] = {
        'total': f"{total / (1024**3):.2f} GB",
        'used': f"{used / (1024**3):.2f} GB",
        'free': f"{free / (1024**3):.2f} GB",
        'percent': f"{used * 100 / total:.2f}%"
    }
    
    # Get disk I/O statistics
    io_counters = psutil.disk_io_counters()
    if io_counters:
        disk_info['io_stats'] = {
            'read_count': io_counters.read_count,
            'write_count': io_counters.write_count,
            'read_bytes': f"{io_counters.read_bytes / (1024**2):.2f} MB",
            'write_bytes': f"{io_counters.write_bytes / (1024**2):.2f} MB",
            'read_time': f"{io_counters.read_time} ms",
            'write_time': f"{io_counters.write_time} ms"
        }
    else:
        disk_info['io_stats'] = {
            'read_count': 'N/A',
            'write_count': 'N/A',
            'read_bytes': 'N/A',
            'write_bytes': 'N/A',
            'read_time': 'N/A',
            'write_time': 'N/A'
        }
    
    return disk_info

def print_disk_info():
    """
    Print the disk information in a formatted manner.
    """
    disk_info = get_disk_info()
    
    print("Disk Information:")
    print("\nTotal Disk Usage:")
    print(f"Total: {disk_info['total_disk']['total']}")
    print(f"Used: {disk_info['total_disk']['used']}")
    print(f"Free: {disk_info['total_disk']['free']}")
    print(f"Usage: {disk_info['total_disk']['percent']}")
    
    print("\nPartitions:")
    for partition in disk_info['partitions']:
        print(f"\nDevice: {partition['device']}")
        print(f"Mountpoint: {partition['mountpoint']}")
        print(f"File System Type: {partition['fstype']}")
        print(f"Options: {partition['opts']}")
        print(f"Total: {partition['total']}")
        print(f"Used: {partition['used']}")
        print(f"Free: {partition['free']}")
        print(f"Usage: {partition['percent']}")
    
    print("\nDisk I/O Statistics:")
    print(f"Read Count: {disk_info['io_stats']['read_count']}")
    print(f"Write Count: {disk_info['io_stats']['write_count']}")
    print(f"Read Bytes: {disk_info['io_stats']['read_bytes']}")
    print(f"Write Bytes: {disk_info['io_stats']['write_bytes']}")
    print(f"Read Time: {disk_info['io_stats']['read_time']}")
    print(f"Write Time: {disk_info['io_stats']['write_time']}")

if __name__ == "__main__":
    print_disk_info()
