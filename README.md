# cookieChat

************************************************************
                         COOKIE CHAT  
Authors: Kenneth Au, Estella Mercado, Eve Collier
Assignment: Final Project - Chat Server
Course: CSC 328 Fall 2023
************************************************************

Cookie Chat is a chat server created by three sleepy college students for a final network programming project in Fall of 2023

COOKIE CHAT SERVER INSTRUCTIONS:
  1. To run Cookie Chat's server, go to the terminal. On the command line type in: "python3 server.py <portNumber> (where port number is a valid port between 10000 - 65535)
  2. When a user is ready to shut the server down, all they need to do is hit ctrl-c on their keyboard. This command will prompt the server to shut down in five seconds.

COOKIE CHAT CLIENT INSTRUCTIONS:
  1. To run Cookie Chat's client, go to the terminal. On the command line, type in: "python3 client.py <hostname> <portNumber> (hostname is localhost on ACAD, port number is still a valid port  between 10000 - 65535)
  2. Enter a nickname. Once your nickname is validated, you're ready to start cookie chatting!
  3. Once a client is ready to disconnect, the user merely needs to hit ctrl-c on their keyboard to exit the cookie chatroom

HOW TO BUILD COOKIE CAT: 
To successfully run Cookie Chat, the server must first be started up. To start the server, simply type ./server <portnum> into the command line, the program will take EXACTLY two arguments. Once the server is on and ready, it is ready to accept client connections. To connect a client, a user needs to type ./client <servername>, <portnum>. When a client is ready to disconnect, the user merely needs to hit cntrl-C on their keyboard. When a user is ready to disconnect the server, the user needs to hit cntrl-C, and then the server will shut down in a few seconds.

 
FILE MANIFSET
----------------
client.py: this is the code for the client side of the program

server.py: this is the code for the server side of the program

library.py: this file contains numerous helper functions implemented in both the client and the server


RESPONSIBILITY MATRIX
-------------------------------------------------------------------------------------------------
|           Kenneth               |              Estella           |            Eve             |
| ------------------------------  | ------------------------------ | ----------------------------
|    Wrote server code            |    Wrote library code          |    Wrote client code       |
|    Debugging program            |    Debugging program           |    Debugging program       |
|    Wrote Makefile               |    Drew ALL diagrams           |    Wrote ReadMe            |
-------------------------------------------------------------------------------------------------


TASKS INVOLVED (correspondence to section 3 of original program design document):                                                                                                                        
  General Subtasks                                                                                              
      - Program Design (Estella, Kenneth, & Eve) - 30 hours                                                                                                                                              
      - Charts/Diagram design (Estella) - 4 hours                                                                                                                        
      - Team Organization/Coordination (Eve) - 2 hours                                                                                                                                        
      - Creation of test cases for program development (Kenneth) - 2 hours                                                                                                        
      - Creation of readMe file (Eve) - 5 hours                                                                                                                            
      - 

      
  Server Subtasks  
  ----------------                                                                                                                                                                                             - Handle connections from MULTIPLE clients (Kenneth) - 4 hours                                                                                                                                     
      - Creation of list with all connected client's nicknames (Kenneth) - 1 hour                                                                                                      
      - Log all connected clients with time stamps to logfile (Kenneth) - 4 hours                                                                                                    
      - Read name sent by client and validate it, send 'READY' if its valid and 'RETRY' if not to client (Kenneth) - 7 hours                                                              
      - Read message sent by a client, all messages recieved from a client to all OTHER connected clients (Kenneth, Eve & Estella) - 10 hours                                                
      - Server debugging (Eve & Estella) - <blank> hours             

      
  Client Subtasks  
  -----------------                                                                                                                                                                                            - Connect the client to the running server (Eve) - 1 hour                                                                                                                                                                                                                                                   
      - Prompt user to enter nickname, if unique, recieve 'READY' from server and allow entry into chat, if not unique, recieve 'RETRY' from server and prompt again, keep doing so until nickname is unique (Eve) - 3 hours                                                                                                                                                                  
      - take input in an infinite loop and send the input to the server, these are the messages. Read a message from the server, that is the message sent to all other clients. Break out of the infinite loop on ctrl-C, then send the client a message indicating they're leaving the chat and send the server a 'BYE' message indicating a client is disconnecting (Eve) - 10 hours                


      
  Library Subtasks                   
  -----------------                                                                                                                                                                                            - Function that ensures ALL bytes of a message are sent AND include a timestamp (Estella) - 10 hours                                                                                               
      - Function that ensures ALL bytes of a prompt are sent (Estella) - 7 hours                                                                                                                         
      - Function that ensures ALL bytes of text are read (Estella) - 5 hours                                                                                                                  



PROTOCOL (section of section 8 revision of original program design document):
  * The client side will be started by running the client program with a specified host name and port number as command line arguments.
  * When the client program connects to the server, it will recieve a "HELLO" message from the server indicating a successful connection. (MAYBE DELETE THIS IDK IF WE DO THIS)
  * If the connection is unsuccessful, the program closes
  * After successful client-server connection, the user on the client side will be prompted to select a nickname in the chat application.
  * 



ASSUMPTIONS
  add later

THE DEVELOPMENT PROCESS
  The first problem the Cookie Chat team ran into was creating a proper application design before the start of the actual code development process. There was a struggle to think of all details necessary to implement in the specs for this project. With the library, there was a struggle to implment JSON (JavaScript Object Notation), as none of our group members had used it in the past and it was a whole new thing to learn. With the client, there was an issue handling how to read a message pushed to all clients EXCEPT the client that sent the message in the first place.
  With the server, there was a major issue figuring out how to fork properly such that the server could handle multiple client connections. It took four days to figure out how to properly fork and handle multiple clients connecting to the server at once, however, after that occurance, the server then ran into the issue of successfully pushing one client's message to all other connected clients. 

STATUS
  laterrrr




