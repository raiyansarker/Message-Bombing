# Import Pyautogui using pip which will allow you to write something on the screen
# Import time to make the application sleep where needed
import pyautogui, time

# Taking 5 seconds gap to make sure your switch to the messaging application and click on the message box
# You can set the timer to anything you want
time.sleep(5)

# Set the variable of how many messages you want to send
amount = 1500
# Set the message
message = "What's up!"

# Loop to write again and again
for num in range(1, amount):
	# Messenger promts the reciver that you are sending the same message again and again. So in order to get rid of that notification, you can set a timer, just uncomment the below line and set the value as much as you like
	# time.sleep(1.5)
	# It will write the message
	pyautogui.typewrite(message)
	# It will send the message
	pyautogui.press("enter")