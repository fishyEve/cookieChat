#!/usr/bin/env python3
import sys
import socket
import signal
import datetime
import os
import select
from library import totallyReadingText
from library import sendingPromptMessage
from library import sendingChats

#/***************************************************************/
#/*Author:           Kenneth Ly Au                              */
#/*Creation Date:    December 11th, 2023                        */
#/*Due Date:         December 14th, 2023                        */
#/*Course:           CSC328 010                                 */
#/*Professor Name:   Dr. Schwesinger                            */
#/*Assignment:       Network Program Implementation             */
#/*Filename:         server.py                                  */
#/*                                                             */
#/*Purpose:          Creates a chat server using select         */
#/*                                                             */
#/*Comments:         Prepared by Kenneth Ly Au with thanks to   */
#/*                  Dr. Schwesinger, the Computer Science      */
#/*                  Graduate Assitant Atom.                    */
#/*                                                             */
#/*Speical Thanks:   Mercado, Estella - library                 */
#/*                  Collier, Eve - Client                      */
#/*                                                             */
#/*Possible Issues:  Name assignement might not work correctly  */ 
#/***************************************************************/

nameList = []
clientList = []

#/*************************************************************************/
#/*                                                                       */
#/* Function name: createChatServer                                       */
#/* Description:   creates the chat server                                */
#/* Parameters:    portNum: type int, import                              */
#/* Return Value:  None                                                   */
#/*                                                                       */
#/*************************************************************************/    
def createChatServer(portNum):
    #creates the server socket and waits for connetion
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:        # ADDED BY EVE - program crashes if port number is in use: we don't want that.
        server_socket.bind(("", portNum))
    except socket.error as message:  # ADDED BY EVE
        print("Bind failed. The port number is already in use, please try running again with a different one.") # ADDED>
        exit(-1)        # ADDED BY EVE
    server_socket.listen(10)
 
    clientList.append(server_socket)
    print("Cookie Chat server started on port " + str(portNum))
    while True:
        ready_to_read,ready_to_write,in_error = select.select(clientList,[],[],0)
        for sock in ready_to_read:
        #if a new connection request is received
            if sock == server_socket: 
                connectedSocket, addr = server_socket.accept()
                clientList.append(connectedSocket)
                name = checkForname(connectedSocket)
                nameList.append(name)
            # a message from a client, not a new connection
            else:
                # process data received from client,
                try:
                    message = totallyReadingText(sock)
                    print(message)
                    data = bytes(message, "utf-8")
                    if data:
                        # there is something in the socket
                        broadcast(server_socket, sock, name, message)
                    else:
                        # remove the socket that's broken
                        print("Client disconnected, did not like oreos")
                        if sock in clientList:
                            clientList.remove(sock)
                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, name, str(" is offline, doesn't like sugar cookies")) 
                # exception 
                except OSError as error:
                    print(error)
                    broadcast(server_socket, sock, name, str(" disconnected, doesn't like oatmeal cookies"))
                    server_socket.close()
                    sys.exit(-1)
                except KeyboardInterrupt:
                    print("Signal Interrupt")
                    serverSocket.close()
                    sys.exit(-1) 
            
#/*************************************************************************/
#/*                                                                       */
#/* Function name: logName                                                */
#/* Description:   logs the unqiue name and time joined                   */
#/* Parameters:    name: type string, import                              */
#/*                current_time: type time, import                        */
#/*                nameList: a list of names, import                      */
#/* Return Value:  None                                                   */
#/*                                                                       */
#/*************************************************************************/    
def broadcast (server_socket, sock, name, message):
    for socket in clientList:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                #socket.sendall(sendingChats(name, message))
                socket.sendall(sendingPromptMessage(message))
                print(name + ": " + message)
            except OSError as error:
                print(error)
                # broken socket connectedSocketion
                socket.close()
                # broken socket, remove it
                if socket in clientList:
                    clientList.remove(socket)
                    
#/*************************************************************************/
#/*                                                                       */
#/* Function name: logName                                                */
#/* Description:   logs the unqiue name and time joined                   */
#/* Parameters:    name: type string, import                              */
#/*                current_time: type time, import                        */
#/*                nameList: a list of names, import                      */
#/* Return Value:  None                                                   */
#/*                                                                       */
#/*************************************************************************/        
def checkForname(connectedSocket):
    name = totallyReadingText(connectedSocket)
    if(len(nameList) != 0):
        for index in range(0, len(nameList)):
            if(nameList[index] == name): 
                connectedSocket.sendall(sendingPromptMessage("RETRY"))
                checkForname(connectedSocket)
                break
            elif((index + 1) == len(nameList)):
                try:
                    current_time = datetime.datetime.now()
                    logName(name, current_time)
                    connectedSocket.sendall(sendingPromptMessage("READY"))
                except OSError as error:
                    print(error)
                    sys.exit(-1)
    else:
        nameList.append(name)
        current_time = datetime.datetime.now()
        logName(name, current_time)
        connectedSocket.sendall(sendingPromptMessage("READY"))
    return name
    
#/*************************************************************************/
#/*                                                                       */
#/* Function name: logName                                                */
#/* Description:   logs the unqiue name and time joined                   */
#/* Parameters:    name: type string, import                              */
#/*                current_time: type time, import                        */
#/*                nameList: a list of names, import                      */
#/* Return Value:  None                                                   */
#/*                                                                       */
#/*************************************************************************/    
def logName(name, current_time):
    try:
        fileName = open('log.txt', 'a')
        fileName.write(name + " joined the chat at " + str(current_time) + "\n")
    except OSError as error:
        print(error)
        sys.exit(-1)
    fileName.close()

#/*************************************************************************/
#/*                                                                       */
#/* Function name: logName                                                */
#/* Description:   logs the unqiue name and time joined                   */
#/* Parameters:    name: type string, import                              */
#/*                current_time: type time, import                        */
#/*                nameList: a list of names, import                */
#/* Return Value:  None                                                   */
#/*                                                                       */
#/*************************************************************************/    
def logMessage(name, message):
    try:
        current_time = datetime.datetime.now()
        fileName = open('log.txt', 'a')
        fileName.write(name + " said at " + str(current_time) + "\n")
    except OSError as error:
        print(error)
        sys.exit(-1)
    fileName.close()

#/*************************************************************************/
#/*                                                                       */
#/* Function name: logName                                                */
#/* Description:   logs the unqiue name and time joined                   */
#/* Parameters:    name: type string, import                              */
#/*                current_time: type time, import                        */
#/*                nameList: a list of names, import                */
#/* Return Value:  None                                                   */
#/*                                                                       */
#/*************************************************************************/            
if __name__ == "__main__" :
    n = len(sys.argv)
    if(n != 2):
        print("Incorrect amount of arguments\n")
    else:    
        portNum = int(sys.argv[1])
        createChatServer(portNum) 
    #openFile()
        
