#!/usr/bin/env python3

def pr_str(malData):
    stringRepr = ""
    #Main switch which identifies whether the data is : a symbol OR a number OR a list
    #print(malData)
    match str(type(malData)):
        
        case "<class 'list'>":
            listType = malData[0]
            for i in range(len(malData)-1):
                result = pr_str(malData[i+1])
                if(stringRepr != ""):
                    stringRepr = stringRepr + " " + result 
                else:
                    stringRepr = stringRepr + result
            match str(listType):
                case '[':
                    stringRepr = "[" + stringRepr + "]"
                case '(':
                    stringRepr = "(" + stringRepr + ")"
                case '{':
                    stringRepr = "{" + stringRepr + "}"
                case _ :
                    return "EOF" 
             #Need to add metadata here because otherwise the {} and [] cannot be reconstructed
            return stringRepr
            
        case "<class 'int'>":
            #Detected an integer
            return str(malData)
        
        case "<class 'str'>":
            if (malData == "error"):
                return "EOF"
            else:
                return malData
        case _:
            return "EOF"