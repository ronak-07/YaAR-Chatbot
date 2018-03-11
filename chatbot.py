import aiml
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.verbose(False)
kernel.setBotPredicate("name", "Yaar")

output_log = open("bot_response.log","w+")

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

print("\nHi. This is Yaar. Ready to serve you.\n\nI have been designed to be a general conversationalist and also assist you for the following things:\n\n")
print("1. Eateries of BITS Pilani Hyderabad Campus along with complete menu\n")
print("2. Weather of any location in the world\n")
print("3. Search anything on Google\n")
print("4. Oh! I can also search images for you.\n")

print("A chatter-box at your service!\n\n\n")
# Press CTRL-C to break this loop
while True:
    message = raw_input("Enter your message to your Yaar:").lower()
    if message == "quit":
      kernel.saveBrain("bot_brain.brn") 
      exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        print(bot_response)
        output_log.write("User: " + message + "\n")
        output_log.write("Bot: "+message+"\n")
        # Do something with bot_response