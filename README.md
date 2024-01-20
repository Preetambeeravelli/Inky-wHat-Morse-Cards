# Inky-wHat-Morse-Cards
Generate random morse code cards for learning on Inky wHat display using raspberrypi

1) Install raspberry pi os with ssh enabled
2) SSH into the pi and turn on I2C and SPI
3) Install all the necessary libraries using the following link
```curl https://get.pimoroni.com/inky | bash```
4) Clone my project and CD into the project
```git clone https://github.com/Preetambeeravelli/Inky-wHat-Morse-Cards.git```
5) Clean and reset using the clean.py script
```python clean.py --type what --colour red```
change color to yellow if using inkyWhat yellow display
7) Run the randomMorseImage.py script (This script executes successfully only when you run it from project root directory)
```python randomMorseImage.py```
8) I have used crontab to run the script in intervals, if you want to use it use randomMorseImageAutomated.py
   in your home directory type
   ```crontab -e```
9) Edit the file so that it looks like this (This means the script runs every 5 minutes)
   ```*/5 * * * * /path/to/python /path/to/your/script.py```
10) After edit it should look like this
   ```*/5 * * * * /usr/bin/python /home/.../Inky-wHat-Morse-Cards/randomMorseImageAutomated.py```
