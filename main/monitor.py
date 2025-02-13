import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def capture_packets(duration=10, interface="eth0", output_file="capture.pcap"):
    """Capture packets using tshark."""
    try:
        command = [
            "tshark",
            "-i", interface,
            "-a", f"duration:{duration}",
            "-w", output_file
        ]
        subprocess.run(command, check=True)
        print(f"Capture saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing packets: {e}")

def analyze_packets(input_file="capture.pcap"):
    """Analyze latency and protocols."""
    # Extract packet info with tshark
    command = [
        "tshark",
        "-r", input_file,
        "-T", "fields",
        "-e", "frame.time_epoch",
        "-e", "ip.proto",
        "-e", "ip.src",
        "-e", "ip.dst",
        "-e", "tcp.analysis.ack_rtt"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Parse data into DataFrame
    data = []
    for line in result.stdout.splitlines():
        fields = line.split('\t')
        if len(fields) == 5:
            time, proto, src, dst, rtt = fields
            data.append({
                "time": datetime.fromtimestamp(float(time)),
                "protocol": proto,
                "source": src,
                "destination": dst,
                "latency_ms": float(rtt)*1000 if rtt else None
            })
    
    df = pd.DataFrame(data)
    return df

def generate_report(df, output_csv="report.csv", output_png="latency.png"):
    """Generate CSV and graphs."""
    # Save to CSV
    df.to_csv(output_csv, index=False)
    
    # Plot latency
    plt.figure()
    df['latency_ms'].dropna().plot(kind='hist', bins=20)
    plt.title("TCP Latency Distribution (ms)")
    plt.savefig(output_png)
    plt.close()

if __name__ == "__main__":
    capture_packets(duration=30)
    df = analyze_packets()
    generate_report(df)
    print("Report generated: report.csv, latency.png")