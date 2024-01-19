# Inky-wHat-Morse-Cards
Generate random morse code cards for learning on Inky wHat display using raspberrypi

1) Install raspberry pi os with ssh enabled
2) SSH into the pi and turn on I2C and SPI
3) Install all the necessary libraries using the following link
curl https://get.pimoroni.com/inky | bash
4) Clone my project and CD into the project
git clone https://github.com/Preetambeeravelli/Inky-wHat-Morse-Cards.git
5) Clean and reset using the clean.py script
python clean.py --type what --colour red
change color to yellow if using inkyWhat yellow display
7) Run the randomMorseImage.py script
python randomMorseImage.py
