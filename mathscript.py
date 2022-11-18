from math import *
import shlex
import os
import sys
from platform import system
vardict = {"pi":3.14}#Preloaded variables
def interpretmath(data: str) -> float:
    #print(vardict)
    for k in vardict.keys():
        
        data = data.replace(k,str(vardict[k]))
    #print(data)
    
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
                    print(f"ERROR! (line {linen}) {str(e)}")
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
        else:
            execline = [d.strip() for d in dataline.split("=")]
            try:
                vardict[execline[0]] = interpretmath(execline[1])
            except Exception as e:
                print(f"ERROR! (line {linen}) {str(e)}")
    except:
        print(f"ERROR (line {linen}) Syntax Error")

def cinterpret(dataline) -> str:
    print(dataline)
    if dataline.split(" ")[0].strip() == "printout":
        outvar = dataline.split(" ")[1].strip()
        _bk = "\""
        if "\"" in outvar:
            return f'printf("{" ".join(dataline.split(" ")[1:]).replace(_bk,"")}\\n");'
        return f'printf("%g\\n",{outvar});'
    elif dataline.split(" ")[0].strip() == "input":
        ddata = shlex.split(dataline)
        prompt = ddata[2]
        svar = ddata[1]
        return f'double {svar} = input("{prompt}");'
    else:
        dlx = dataline.split("=")
        return f"double {dlx[0].strip()} = {dlx[1].strip()};"
    return ""

if len(sys.argv) < 2:
    print("MathScript interpreted v0.1 (c) 2022 Enderbyte Programs")
    while True:
        _i = input(">>> ")
        if _i.strip() != "":
            interpret(_i,0)
with open(sys.argv[1]) as f:
    data = f.readlines()
data = [d.strip() for d in data if d[0] != '#']#Removing comments
if "--compile" in sys.argv:
    try:
        with open("template.c") as f:
            tdata = f.readlines()
        SCRIPT = ""
        for dataline in data:
            SCRIPT += cinterpret(dataline) + "\n"
        print(SCRIPT)
        tdata = "\n".join(tdata).replace("//DATAHERE",SCRIPT)
        with open("temp.c","w+") as f:
            f.write(tdata)
        if system() == "Windows":
            lx = os.system("gcc -O temp.c -lm -o program.exe")#Set to exe if on windows
        else:
            lx = os.system("gcc -O temp.c -lm -o program")
        if lx != 0:
            raise OSError("Compilation Failure!")
        os.remove("temp.c")
        sys.exit()
    except Exception as e:
        print(f"Compile Error! {str(e)}")
        sys.exit(-1)
#Interpreted mode

dline = 0
for dataline in data:
    dline += 1
    interpret(dataline,dline)