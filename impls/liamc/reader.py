#!/usr/bin/env python3
#Can use a regexp module in python 
import re
#Reader class to navigate the abstract tree
#Need to implement something that prevents the entry of an empty string
class Reader:
    def __init__(self,tokens):
        self.position = 0
        self.tokenList = tokens
        self.open = ["(","[","{"]
        self.close = [")","]","}"]

    def next(self):
        self.position = self.position + 1
        if(self.position >= len(self.tokenList)): #Protection
            return 0
        else:
            return self.tokenList[self.position]

    def peek(self):
        return self.tokenList[self.position]
    
    def read_atom(self):
        tkn = self.peek()
        return tkn

    def read_form(self):
            #Get the first token, ie the first token of the token list
            tkn = self.peek()
            #Check the enums that contain the characters that should be considered similar to the { } and [ ] and ( )
            if (tkn in self.open):
                self.next()
                return self.read_list(tkn)

            elif (tkn in self.close):
                if (self.position == len(self.tokenList)-1):
                    return self.read_atom()
                else:
                    temp = self.read_atom()
                    self.next()
                    return temp
            else:
                str = self.read_atom()
                self.next()
                return str


    def read_list(self,type):
        list = [type]
        m=self.read_form()
        while (((m not in self.close)) and (self.position != len(self.tokenList))): #The second condition is necessary for when an input is incorrect
            list.append(m)
            m = self.read_form()
        
        if (self.position == len(self.tokenList)):
            return "error"
        else:
            print(list)
            return list

#read_str function that reads a string and creates a new Reader object

def read_str(s):
    #Tokenize string ie extract tokens (sub-strings here) and put them into a list
    l = tokenize(s)
    #Extracted list is stored in reader
    reader = Reader(l)
    #Let the reader read its own token list
    return reader.read_form()

def tokenize(s):
    #Use the regex library to tokenize the string

    tokens_raw = re.split("[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)",s) #~@ is a special character like {
    tokens = [token for token in tokens_raw if token != '']
    print(tokens)
    return tokens

def check(s): #Need to implement an efficient way to check the token list has the required parentheses, maybe by recursively counting them? or sorting the list then finding the number of parentheses
    if ((s[0]=='(') and (s[-1] == ')') ):
        return s
    else :
        return "EOF"