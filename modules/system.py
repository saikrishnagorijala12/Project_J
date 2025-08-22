import os
import subprocess


# ------------------ System Commands ------------------
def handle_system(text):
    text_lower = text.lower()
    if "firefox" in text_lower:
        os.system("firefox &")
        return "Opening Firefox"
    elif "chrome" in text_lower:
        os.system("google-chrome &")
        return "Opening Chrome"
    elif "code" in text_lower or "vs code" in text_lower:
        os.system("code &")
        return "Opening VS Code"
    elif "terminal" in text_lower:
        os.system("gnome-terminal &")
        return "Opening Terminal"
    elif "shutdown" in text_lower:
        os.system("shutdown now")
        return "Shutting down system"
    elif "restart" in text_lower:
        os.system("reboot")
        return "Restarting system"
    elif "volume up" in text_lower:
        os.system("pactl set-sink-volume @DEFAULT_SINK@ +10%")
        return "Volume increased"
    elif "volume down" in text_lower:
        os.system("pactl set-sink-volume @DEFAULT_SINK@ -10%")
        return "Volume decreased"
    elif "ip" in text_lower:
        ip = subprocess.getoutput("hostname -I | awk '{print $1}'")
        return f"Your IP address is {ip}"
    elif "system info" in text_lower:
        info = subprocess.getoutput("neofetch --stdout")
        return info
    else:
        return "System command not recognized."