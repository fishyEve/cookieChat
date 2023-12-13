#Author: Estella Mercado
#Assignment: Final Project - Group Project Chat Application
#Course: csc328
#Fall 2023

#import statements
import json
import datetime

#Function Name: sendingPromptMessage
#Description: This function will allow a prompt message to be sent over to the server/client
#			Note! This is just for prompt messages and prompt messages only, this function does not include timestamps etc.
#Parameters: nickname - string, nickname/retry/ready/prompt input from the server/client
#Return Value: bytePromptMessage - the prompt message/nickname encoded to be sent to the server/client along with the length in bytes
def sendingPromptMessage(prompt):

	#converts the prompt text into a json string
	promptJString = json.dumps(prompt)

	#gets the length of the json prompt string
	promptLength = len(promptJString)

	#converts the length of the json prompt string into two bytes
	bytePromptLength = promptLength.to_bytes(2, "big")

	#converts the actual json prompt string into bytes
	bytePrompt = promptJString.encode()

	#actually builds bytePromptMessage with length and encoding
	bytePromptMessage = bytePromptLength + bytePrompt

	#return statement
	return bytePromptMessage
	#end of sendingPromptMessage function

#Possible use cases of sendingPromptMessage function: 
#Client: footSocks.sendall(sendingPromptMessage(nickname))
#Server: connect.sendall(sendingPromptMessage('READY')

#Function Name: totallyReadingBytes(yourSocket, numBytes)
#Description: This function will ensure that all the bytes from a nickname/nickname message is being read
#Parameters: yourSocket - the socket in use where bytes were sent
#			numBytes - the necessary number of bytes to be read
#Return Value: myBytes - byte string of the encoded name value
def totallyReadingBytes(yourSocket, numBytes):
	
	#makes sure that all bytes being sent over the socket are read
	myBytes = b'' #current number of bytes

	while len(myBytes) != numBytes: #loops to make sure the socket receives the correct amount of bytes
		myBytes = myBytes + yourSocket.recv(numBytes - len(myBytes))
		if (len(myBytes)) == 0: break #breaks from the loop if length of myBytes = 0

	#return statement
	return myBytes
	#end of totallyReadingBytes function

#totallyReadingBytes is a helper function for the totallyReadingPrompt function
#client/server does not need to use this- IT IS ONLY A HELPER FUNCTION!

#Function Name: totallyReadingText(yourSocket)
#Description: This function will allow the correct reading of the sent prompt/chats from the client/server
#Parameters: yourSocket - the socket in use where bytes will be read from
#Return Value: textString - decoded string value of the sent prompt/chats
def totallyReadingText(yourSocket):

	#gets the length of the prompt to be read in bytes
	textLength = int.from_bytes((totallyReadingBytes(yourSocket, 2)), 'big') #only reads two bytes at first to get length

	#gets the correct number of bytes to be read
	textBytes = totallyReadingBytes(yourSocket, textLength)

	#converts the bytes read into a string
	textString = textBytes.decode()

	#return statement
	return textString
	#end of totallyReadingPrompt function

#Possible use cases for this are when reading: userNickname = totallyReadingText(yourSocket)
#												print(totallyReadingText(yourSocket))

#Function Name: sendingChats
#Description: This function will allow the client and server to be able to send messages to one another
#Parameters: nickname - string, nickname of the user
#			message - string, the actual message the user is sending: example: "What's up!"
#Return Value: finalMessage - the encoded message value to be sent along with the list of 
def sendingChats(nickname, message):

	#Gets current time in order to timestamp the message
	timeStamp = datetime.datetime.now()
	
	#converts the datetime object into a string
	strTimeStamp = str(timeStamp)

	#Converts the inputs nickname and message with timestamp to a dictionary
	messageDict = {'Timestamp': strTimeStamp, 'Nickname': nickname, 'Message': message}

	#Turns messageDict into a json string
	jsonMessage = json.dumps(messageDict)

	#gets the length of the json chat string
	jsonMessageLength = len(jsonMessage)

	#converts the length of the json chat message into two bytes
	byteLength = jsonMessageLength.to_bytes(2, "big")

	#Turns json string into bytes
	byteMessageStr = jsonMessage.encode()

	#creates the actual final message in bytes to be sent over to the socket
	byteMessage = byteLength + byteMessageStr

	#return message
	return byteMessage 
	#end of sendingMessages function

#Possible use cases: footSocks.sendall(sendingChats(nickname, 'bro'))

#end?
