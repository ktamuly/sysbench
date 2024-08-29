# System Benchmark

## Overview

System Benchmark is a comprehensive tool designed to evaluate and report on various aspects of your system's performance. It provides detailed information about CPU, memory, disk, network, and GPU usage, helping you understand the capabilities and limitations of your hardware.

## Features

- **CPU Information**: Get detailed information about your CPU, including processor name, number of physical and logical cores, current frequency, and usage percentage.
- **Memory Information**: Retrieve data on virtual and swap memory, including total, available, used, and free memory, as well as usage percentage.
- **Disk Information**: Obtain details about disk partitions, total disk space, used and free space, and I/O statistics.
- **Network Information**: Gather information about your network, including hostname and IP address.
- **GPU Information**: Access comprehensive details about your NVIDIA GPUs, including name, UUID, memory usage, utilization, temperature, power usage, fan speed, and driver information.

## Requirements

- Python 3.6+
- NVIDIA GPU (for GPU information)
- NVIDIA drivers installed

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/system-benchmark.git
   cd system-benchmark
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script to generate and display a system report:
```
python src/report_generator.py
```

This will generate a report and print it to the console.
