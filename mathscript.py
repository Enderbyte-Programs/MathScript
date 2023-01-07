#!/usr/bin/env python3

from math import *
import shlex
import sys

vardict = {"pi":3.14}#Preloaded variables
def interpretmath(data: str) -> float:
    #print(vardict)
    for k in vardict.keys():
        
        data = data.replace(k,str(vardict[k]))
    #print(data)
    data = data.replace("^","**")
    try:
        result = int(data)
    except:
        #result = 0
        result = eval(data)
    #print(result)
    try:
        result = float(result)
    except:
        raise ValueError("NO MATH")
    #print(result)
    return result

def interpret(dataline,linen=0):
    #print(dataline)
    if dataline.strip() == "exit":
        sys.exit()
    try:
        if dataline.split(" ")[0].strip() == "printout":
            outvar = dataline.split(" ")[1].strip()
            if outvar in vardict.keys():
                print(vardict[outvar])
            else:
                try:
                    if "\"" in outvar:
                        print(" ".join(dataline.split(" ")[1:]).replace("\"",""))
                    else:
                        print(interpretmath(outvar))
                except Exception as e:
                    print(f"ERROR! (line {linen+1}) {str(e)}")
        elif dataline.split(" ")[0].strip() == "input":
            ddata = shlex.split(dataline)
            prompt = ddata[2]
            svar = ddata[1]
            while True:
                tinp = input(prompt+": ")
                try:
                    tinp = float(tinp)
                except:
                    print("Not A Number.")
                else:
                    vardict[svar] = tinp
                    break
        elif dataline.split(" ")[0].strip() == "dumpvar":
            print(vardict)
        else:
            execline = [d.strip() for d in dataline.split("=")]
            try:
                vardict[execline[0]] = interpretmath(execline[1])
            except Exception as e:
                print(f"ERROR! (line {linen}) {str(e)}")
    except:
        print(f"ERROR (line {linen}) Syntax Error")

if len(sys.argv) < 2:
    print("MathScript v4 (c) 2022-2023 Enderbyte Programs")
    while True:
        _i = input(">>> ")
        if _i.strip() != "":
            if _i == "dumpvar":
                print(vardict)
                continue
            interpret(_i,0)
with open(sys.argv[1]) as f:
    data = f.readlines()
data = [d.strip() for d in data if d[0] != '#']#Removing comments

dline = 0
for dataline in data:
    dline += 1
    interpret(dataline,dline)
