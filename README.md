# cookieChat

************************************************************
                                             COOKIE CHAT  
Authors: Kenneth Au, Estella Mercado, Eve Collier                                                                                                                                                    
Assignment: Final Project - Chat Server                                                                                                                                                            
Course: CSC 328 Fall 2023
************************************************************

Cookie Chat is a chat server created by three sleepy college students for a final network programming project in Fall of 2023

COOKIE CHAT SERVER INSTRUCTIONS:
  1. To run Cookie Chat's server, go to the terminal. On the command line type in: "python3 server.py <portNumber>"
  2. When a user is ready to shut the server down, all they need to do is hit CTRL-C on their keyboard. This command will shut the server down

COOKIE CHAT CLIENT INSTRUCTIONS:
  1. To run Cookie Chat's client, go to the terminal. On the command line, type in: "python3 client.py <hostname> <portNumber>"
  2. Enter a nickname. Once your nickname is validated, you're ready to start cookie chatting!
  3. Once a client is ready to disconnect, the user merely needs to hit CTRL-C on their keyboard to exit the cookie chatroom

HOW TO BUILD COOKIE CHAT: 
To successfully run Cookie Chat, the server must first be started up. To start the server, simply type "python3 server.py <portnum> "into the command line, as specified above. Once the server is on and ready, it is ready to accept client connections. To connect a client, a user needs to type "python3 lient.py <hostname>, <portnum>", as specified above. When a client is ready to disconnect, the user merely needs to hit CTRL-C on their keyboard. When a user is ready to disconnect the server, the user needs to hit CTRL-C, and then the server will shut down instantly.

 
FILE MANIFSET
----------------
client.py: this is the code for the client side of the program

server.py: this is the code for the server side of the program

library.py: this file contains numerous helper functions implemented in both the client and the server

ClientFlowchart.png: this file contains the image of a flowchart entailing the client functionality

FinalProject_SequenceDiagram.pdf: this file contains the image of a sequential diagram for our program

ServerStateDiagram.png: this file contains the server state machine diagram

libraryFixed.py: this file contains what would have been the fix for our library. It included a totallyBytesFunction that read bytes and a python dictionary that uses JSON encoding. Unfortuntely, there was a bug, and not enough time to fix it. Details are included below in the development process section of this document.


RESPONSIBILITY MATRIX
-------------------------------------------------------------------------------------------------
|           Kenneth               |              Estella           |            Eve             |
| ------------------------------  | ------------------------------ | ----------------------------
|    Wrote server code            |    Wrote library code          |    Wrote client code       |
|    Debugging program            |    Debugging program           |    Debugging program       |
|    Wrote testcases              |    Drew ALL diagrams           |    Wrote ReadMe            |
-------------------------------------------------------------------------------------------------


TASKS INVOLVED (correspondence to section 3 of original program design document):                                                                                                                        
  General Subtasks                                                                                              
      - Program Design (Estella, Kenneth, & Eve) - 30 hours                                                                                                                                             
      - Charts/Diagram design (Estella) - 10 hours                                                                                                                        
      - Team Organization/Coordination (Eve) - 6 hours                                                                                                                                        
      - Creation of test cases for program development (Kenneth) - 4 hours                                                                                                        
      - Creation of readMe file (Eve & Estella) - 15 hours                                                                                                                            

      
  Server Subtasks  
      - Handle connections from MULTIPLE clients (Kenneth) - 14 hours                                                                                                                                   
      - Creation of list with all connected client's nicknames (Kenneth) - 3 hour                                                                                                      
      - Log all connected clients with time stamps to logfile (Kenneth) - 4 hours                                                                                                    
      - Read name sent by client and validate it, send 'READY' if its valid and 'RETRY' if not to client (Kenneth) - 7 hours                                                              
      - Read message sent by a client, push all messages recieved from a client to all OTHER connected clients (Kenneth) - 20 hours  
      - When a client disconnects, the server notifies all other clients that a client has left the chat (Kenneth) - 19 hours
      - Server debugging (Eve & Estella & Kenneth) - 12 hours                                                                                     
      - Signal handling on CTRL-C (Kenneth) - 2 hours                          

      
  Client Subtasks  
      - Connect the client to the running server (Eve) - 1 hour                                                                                                                                         
      - Prompt user to enter nickname, if unique, recieve 'READY' from server and allow entry into chat, if not unique, recieve 'RETRY' from server and prompt again, keep doing so until nickname is unique (Eve) - 7 hours                                                                                                                                                                  
      - take input in an infinite loop and send the input to the server, these are the messages (Eve) - 15 hours
      - Read a message from the server, that is the message sent from a different client (Eve) - 16 hours
      - Use signal handler to break out of the infinite loop on CTRL-C, then send the client a message indicating they're leaving the chat and send the server a 'BYE' message indicating a client is disconnecting (Eve) - 10 hours                   
      - Client debugging (Kenneth & Eve & Estella) - 16 hours


      
  Library Subtasks                   
      - Function that ensures a message (prompt) WITHOUT a timestamp is sent (like a user-supplied nickname) (Estella) - 10 hours                                                                       
      - Function that ensures a message WITH a timestamp and a nickname are sent (Estella) - 17 hours                                                                                                   
      - Function that ensures ALL bytes of text are read (Estella) - 13 hours                                                                                                                                 - A helper function for the above functions that reads BOTH prompt messages and chat messages (Estella) - 10 hours
      - Debugging (Estella & Eve) - 10 hours


PROTOCOL (section of section 8 revision of original program design document):
  * The server side will be started by running the server program with a specified port number as a command line argument. This is the syntax: python3 server.py <portNumber>
  * The client side will be started by running the client program with a specified host name and port number as command line arguments. This is the syntax: python3 client.py <hostname> <portNumber>
  * The client connects to the server, if the connection is unsuccessful, the program closes. 
  * After successful client-server connection, the user on the client side will be prompted to enter a nickname in the chat application. The client sends this nickname to the server.
  * The server reads the nickname sent by the client. If the nickname is unique, it sends 'READY' to the client, indicating the specific client is ready to enter the chat room. If the nickname is not unique, the server sends 'RETRY' to the client, to which the client will prompt the user to enter a different nickname.
  * Once a unique nickname is verified by the server, the server logs that nickname into a log file, then a string indicating that the specified client 'has joined the chat at', then the date and timestamp.
  * A user can send a message into the chat by typing it out and hitting enter. This message is sent to the server by the client. 
  * When the server recieves a message from the client, it sends that message to every client EXCEPT the client the message originates from.  
  * When a client reads a message that was pushed to them by the server, it prints that message out onto the screen for the user to read.
  * The server is always listening for messages from all connected clients. A client will ONLY read from the socket if there is data in it to be read. 
  * When a client is ready to leave the chat, they press CTRL-C. The client sends 'BYE' to the server.
  * When the server recieves 'BYE' from the client, it indicates that a client has left the chat room to all other connected clients.
  * When a user is ready to shut the server down, they just hit CTRL-C. The server shuts down instantly


ASSUMPTIONS                                                                                                                                                                                  
  - A message is no longer than 65,535 characters                                                                                                                                                         - The user knows how to run the server and the client (a user can learn by reading this readMe :D)
  - The user will message in English
  - The user will know have a host to connect their client to
  - The user will type their message into the command line and hit enter to send it

THE DEVELOPMENT PROCESS                                                                                                                                                                        
  The first problem the Cookie Chat team ran into was creating a proper application design before the start of the actual code development process. There was a struggle to think of all details necessary to implement in the specs for this project. With the library, there was a struggle to implment JSON (JavaScript Object Notation), as none of our group members had used it in the past and it was a whole new thing to learn. With the client, there was an issue handling how to read a message pushed to all clients EXCEPT the client that sent the message in the first place.
  With the server, there was a major issue figuring out how to fork properly such that the server could handle multiple client connections. It took four days to figure out how to properly fork and handle multiple clients connecting to the server at once. After that was solved, there was another issue: figuring out how to successfully pushing one client's message to all other connected clients as well as having an simple way for the client to know when to read and when to write to the socket...this was the big bad boss of the project, as it took us the entirety of the last week to figure this out. We decided to rewrite bits of the client, Kenneth even ended up writing three different servers at one point in an attempt to get multiple clients connected to the server. We also decided to cut out certain parts of the project (for example, making nicknames that were taken by a client that has disconnected avalible for another client to use). 
  This brings us to the most heartwrenching part of the development process: libraryFixed.py. As one can see, messages in cookieChat are displayed like so: "{\"Timestamp\": \"2023-12-13 18:39:49.894785\", \"Nickname\": \"eve\", \"Message\": \"hi\"}". There are a lot of quotation marks and '\'s throughout. Estella created libraryFixed.py to address this issue after attending Schwesinger's office hours on 12/13/23 (Taylor Swift's birthday) and getting some helpful advice on how to implement a solution. She used JSON encoding on a python dictionary and then pulled from those fields to build the chat message. The messages looked spetecular, it only had the timestamp, nickname, and message itself, no random '\'s and quotation marks. She implemented a totallyBytes function (as recommended by Schwesinger) that recieved bytes from the client which the server could then use to push to other clients. The only problem is that, for some reason, whenever a client disconncted from the server, all other clients and the running server would crash and have all sorts of tracebacks. We figured this was due to the user hitting ^C to exit cookieChat, however, there simply wasn't enough time to fix it. Due to this, we were faced with a tough decision: submit a program with beautiful output but with tracebacks everytime a single client disconnects from the server, or, submit a program with wacky-ish input but no tracebacks. A wise man by the name of Schwesinger once said, "If it segfaults, it's a zero". While the issue didn't cause a segfault, a traceback was close enough for us. If it weren't for the traceback, we would have used libraryFixed.py 
  
STATUS                                                                                                                                                                                                  
  - If a client tries to join the chatroom at the same time as another client, and the first client is not fully verified (meaning their nickname was already taken and they need to enter a different one) the program will crash.
  - If a client leaves the chat, the nickname they selected to use will still be unavalible
  - The server does not shut down in x amount of seconds on CTRL-C. It just instantly shuts down without warning any of the clients.
  - The server does not log messages to the logfile
  - Messages have the following form: "{\"Timestamp\": \"2023-12-13 18:39:49.894785\", \"Nickname\": \"eve\", \"Message\": \"hi\"}"
  - The server shoots tracebacks upon the user hitting CTRL-C UNLESS if all clients disconnect before the server shuts down
  - The server doesn't do anything with the 'BYE' message they recieve
  - Please have mercy




