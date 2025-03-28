import pyautogui
import time
import subprocess
import psutil
import os
import sys
import pyperclip

def find_discord_path():
    # Get the user's home directory
    user_home = os.path.expanduser("~")

    # Base path for Discord installation
    base_path = os.path.join(user_home, "AppData", "Local", "Discord")

    # Search for Discord.exe or Update.exe
    if os.path.exists(base_path):
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.lower() == "update.exe" or file.lower() == "discord.exe":
                    return os.path.join(root, file)

    raise FileNotFoundError("Discord executable not found. Please verify the installation path.")

# Call the function to find Discord
try:
    discord_path = find_discord_path()
    if "Update.exe" in discord_path:
        discord_path = f"{discord_path} --processStart Discord.exe"
    print(f"Discord executable path: {discord_path}")
except FileNotFoundError as e:
    print(f"{e}\nPlease check if Discord is installed and verify the AppData directory.")
    sys.exit(1)

# JavaScript code to enable experiment mode
javascript_code = """d=null,webpackChunkdiscord_app.push([[Symbol()],{},({c:e})=>d=Object.values(e)]),c=d,delete d,u=c.find((e=>e?.exports?.default?.getUsers)).exports.default,m=Object.values(u._dispatcher._actionHandlers._dependencyGraph.nodes),u.getCurrentUser().flags|=1,m.find((e=>"DeveloperExperimentStore"===e.name)).actionHandler.CONNECTION_OPEN();try{m.find((e=>"ExperimentStore"===e.name)).actionHandler.OVERLAY_INITIALIZE({user:{flags:1}})}catch{}m.find((e=>"ExperimentStore"===e.name)).storeDidChange();"""

# Function to check if Discord is running
def is_discord_running():
    for proc in psutil.process_iter(['name']):
        if "Discord" in proc.info['name']:
            return True
    return False

# Launch Discord
print("Launching Discord...")
subprocess.Popen(discord_path, shell=True)

# Wait for Discord to fully load
print("Waiting for Discord to load...")
while not is_discord_running():
    time.sleep(1)
time.sleep(3)  # Ensure UI is fully loaded

# Open developer console
print("Opening developer console...")
pyautogui.hotkey('ctrl', 'shift', 'i')
time.sleep(2)

# Paste JavaScript code
print("Pasting JavaScript code...")
pyperclip.copy(javascript_code)  # Copy code to clipboard
pyautogui.hotkey('ctrl', 'v')  # Paste into console
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('ctrl', 'shift', 'i')
print("Code pasted successfully! Experiment mode enabled.")
