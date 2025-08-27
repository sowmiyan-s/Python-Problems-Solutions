import os
import subprocess
import time
import webview
import threading

def start_streamlit():
    os.environ["BROWSER"] = "none"
    subprocess.Popen(["streamlit", "run", "model_builder_v2.py", "--server.headless", "true"])

def launch_gui():
    time.sleep(2)
    webview.create_window("ML Toolkit - Model Builder", "http://localhost:8501", width=1280, height=800)
    webview.start()

if __name__ == "__main__":
    threading.Thread(target=start_streamlit).start()
    launch_gui()
