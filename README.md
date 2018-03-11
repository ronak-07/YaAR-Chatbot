YaAR-Chatbot
====================
A basic chatbot implementation using AIML.

Running Instructions
-----------------------
	python chatbot.py
		
Examples: 

	To know about the eateries in BITS Hyderabad
	    WHAT ARE THE EATERIES IN BITS HYDERABAD
	    
	To know the temperature in Hyderabad
		Give me the temperature in Hyderabad
		
	To google about BITS Pilani Hyderabad Campus
		google BITS Pilani Hyderabad Campus
		
	To google images of BITS Pilani Hyderabad Campus
		images of BITS Pilani Hyderabad Campus

Capabilities
---------------

Can give you information about:

- Eateries of BITS Pilani Hyderabad Campus along with complete menu.
- Weather of any location in the world
- Search anything on Google
- Can search images.
- Can carry out complete conversation (Uses all ALICE AIML files for this).

Dependencies - Installation Instructions
-----------------------------------------

- Pillow - "pip install Pillow"
- py-aiml - "pip install aiml"
- requests - "pip install requests"
- Selenium - "pip install selenium"
- Chrome WebDriver - Download from "https://sites.google.com/a/chromium.org/chromedriver/downloads" and add to path
- darksky - "pip install darksky"


Other Details
-----------------
- The Knowledge-base is stored in "bot_brain.brn" file
- Uses ALICE AIML files if response is not found in basic_chat.aiml
- The conversation between the bot and the user is stored in "bot_response.txt" file
- Since it doesn't uses any sort of ML to answer, responses depends a lot on the syntax of query.
