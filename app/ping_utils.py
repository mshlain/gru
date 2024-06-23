import subprocess
import platform
import threading


def run_ping(host, output_area):
    """
    Runs ping command and updates output area in real-time
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    output = ""
    for line in process.stdout:
        output += line
        output_area.text_area("Console Output", value=output, height=400)

    for line in process.stderr:
        output += line
        output_area.text_area("Console Output", value=output, height=400)

    print(f"Process return code: {process.returncode}")

    return True
