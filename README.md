# key_counter

1. Open and run install.py. You should see "pynput" and "pygsheets" install successfully.

2. MAC ONLY: You'll need to go into System Settings -> Privacy and Security -> Input Monitoring, and enable Python IDLE and your Python interpreter to monitor input from your keyboard.

3. You should have received a link to the "Key Counter" Google Sheet from me, as well as a JSON file. Put the JSON file in the same folder as the Python files.

4. To make things easier, don't rename the Google Sheet or any of the sheets in it. Feel free to change any of the headings, however. You can also change the number of keys manually. Don't move any of the values out of their current cells, however - just change them.

5. Open config.py. You'll see a dictionary {} with lists [] inside of it. The defaults for the hotkeys are set at "q", "w", "e", and "r". Respectively, they decrease the losing key number, increase the losing key number, decrease the winning key number, and increase the winning key number. Change the value in the parentheses at the beginning of each line to map the commands to different hotkeys. Each and EVERY time you press a hotkey, the values will increase or decrease by 1.

6. Run config.py and open the "Key Counter" Google Sheet.

7. Spamming the hotkeys will put a delay on the changes (automatically through the Google Sheets API), but they will eventually load.