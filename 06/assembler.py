#01
comp = {"": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100", "A": "0110000", "!D": "0001101",
        "!A": "0110011", "-D": "0001111", "-A": "0110011", "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
        "A-1": "0110010", "D+A": "0000010", "D-A": "0010011", "A-D": "0000111", "D&A": "0000000",
        "D|A": "0010101", "M": "1110000", "!M": "1110001", "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
        "D-M": "1010011", "M-D": "1000111", "D&M": "1000000", "D|M": "1010101"}
#02
dest = {"0": "000", "M": "001", "D": "010", "DM": "011", "A": "100", "AM": "101", "AD": "110", "ADM": "111"}
#03
jump = {"": "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}

#------A語言-------------
symbol = {"R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10,
          "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15, "SCREEN": 16384, "KBD": 24576}
#-----------------------
out = "111"
cnt=0
import os
filename = "input.asm"
output_filename = "mult.hack"
with open(output_filename, "w") as clear_file:
    clear_file.write("")

with open('input.asm', 'r',encoding='utf-8') as file:
    lines = file.readlines()
for line in lines:
     #這邊用startswith("/")排掉 不然輸出會有錯誤
     if not line.startswith("/"):
        if line.startswith("("):
            label = line[1:line.index(')')].strip()
            symbol[label] = cnt
        else:
            cnt += 1
cnt=0

#print(symbol)

for line in lines:
    if not line.startswith("/"):
        if line.startswith("@"):
            cnt=0
            parts = line.split("@")
            domain = parts[1].strip()
            if domain in symbol :
                binary_code = format(symbol[domain], '016b')
                # print(binary_code)
            elif domain.isdigit():
                binary_code = format(int(domain), '016b')
                # print(binary_code)
            else :
                continue

        elif  line.startswith("("):
            continue
        #-------A指令---------
#---------C指令--------
        #把76行 if else 並進去
        else :
            find=line.find("=")
            word= line.find(";")
            
            if find !=-1 and word!=-1:
                label=''
                two=''
                three=''
                label = line[0:find].strip()
                # print(label)
                dest_code = dest.get(label,"").strip()
                # print(dest_code)

                two = line[find+1:word].strip()
                comp_code = comp.get(two, "").strip()

                three = line[word+1:].strip()
                jump_code = jump.get(three, "").strip()


            elif find !=-1 and word==-1:
                label=''
                two=''
                three=''
                label = line[0:find].strip()
                # print(label)
                dest_code = dest.get(label,"").strip()
                # print(dest_code)
                 
                two = line[find+1:].strip()
                if two=='0' :
                    two =""
                comp_code = comp.get(two, "").strip()

                three = ""
                jump_code = jump.get(three, "").strip()    


            elif find ==-1 and word!=-1:
                label=''
                two=''
                three=''
                label = line[0:word].strip()
                # print(label)
                dest_code = dest.get(label,"").strip()
                # print(dest_code)
                two=""
                comp_code = comp.get(two, "").strip()

                three = line[word+1:].strip()
                jump_code = jump.get(three, "").strip()


            elif find ==-1 and word==-1:
                label=''
                two=''
                three=''
                label = line[0:word].strip()
                # print(label)
                dest_code = dest.get(label,"").strip()
                # print(dest_code)

                two=""
                comp_code = comp.get(two, "").strip()

                three = ""
                jump_code = jump.get(three, "").strip()    

        
            binary_code=(out+comp_code+dest_code+jump_code)
        print(binary_code)

        output_filename = "mult.hack"
        output_filepath = os.path.join(output_filename)

        with open(output_filepath, "a") as output_file:
            output_file.write(binary_code + "\n")

