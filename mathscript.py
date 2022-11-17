import math

SCRIPT = ""
import sys
if len(sys.argv) < 2:
    print("Please provide file")
    sys.exit()
with open(sys.argv[1]) as f:
    data = f.readlines()
data = [d.strip() for d in data if d[0] != '#']#Removing comments
if "--compile" in sys.argv:
    raise NotImplementedError("I haven't done this yet")
#Interpreted mode
vardict = {"pi":3.14}

def interpretmath(data: str) -> float:
    print(vardict)
    for k in vardict.keys():
        data.replace(k,str(vardict[k]))
    print(data)
    
    try:
        result = int(data)
    except:
        result = 0
        exec(f"result = {data}")
    try:
        result = float(result)
    except:
        raise ValueError("NO MATH")
    print(result)
    return result

for dataline in data:
    print(dataline)
    if dataline.split(" ")[0].strip() == "printout":
        outvar = dataline.split(" ")[1].strip()
        if outvar in vardict.keys():
            print(vardict[outvar])
        else:
            try:
                interpretmath(outvar)
            except Exception as e:
                print(f"ERROR! {str(e)}")
                sys.exit(1)
    else:
        execline = [d.strip() for d in dataline.split("=")]
        try:
            vardict[execline[0]] = interpretmath(execline[1])
        except Exception as e:
            print(f"ERROR! {str(e)}")
            sys.exit(1)
