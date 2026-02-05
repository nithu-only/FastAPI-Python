#Import psutil library to get System Metrics
import psutil

def get_system_metrics():
    """
        This function gets the System metrics such as
        CPU info, Memory info, Disk info based on CPU Threshold.
    """

    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    cpu_threshold = 10

    status = "High CPU" if cpu_percent>cpu_threshold else "Healthy"

    return {
        "cpu_percentage": cpu_percent,
        "memory_percentage": mem_percent,
        "disk_percentage": disk_percent,
        "cpu_threshold": cpu_threshold,
        "status": status
    }