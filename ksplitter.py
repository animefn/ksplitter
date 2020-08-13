import sys
import argparse
import datetime


def aegiTimeTOds (timestr):
    h, m, sms = timestr.split(':')
    s,ms = sms.split(".")
    total_ds = int(ms) + ( int(h) * 3600 + int(m) * 60 + int(s)  ) * 100
    return total_ds

def str_TOkara_array(karaText, mode):
    if mode == "char":
        return k_array_char(karaText)
    if mode == "word":
        return k_array_word(karaText)
    if mode == "syl":
        return k_array_syl(karaText)



def k_array_char(karaText):
    karaSplit_array = []
    for letter in karaText:
        if letter in [" ","!","?",",",";",":"]:
            if len(karaSplit_array)>0:
                karaSplit_array [ len(karaSplit_array)-1 ] =  karaSplit_array [ len(karaSplit_array)-1 ]+letter
            else:
                karaSplit_array.append (letter)    
        else:
            karaSplit_array.append (letter)

    return karaSplit_array

def k_array_word(karaText):
    karaSplit_array = []
    array_nospace = karaText.split()
    for i in range(len(array_nospace)):
        karaSplit_array.append ( array_nospace[i] +" ")
    return karaSplit_array



def k_array_syl(karaText):
    karaString=""
    karaSplit_array = []
    ln = len (karaText)
    l=0
    while l < ln :
        letter = karaText[l]
        letter1=""
        if 0 <= l+1 < len(karaText):
            letter1 = karaText[l+1]
        
        
        if letter.lower() in "rymnhk":
            if letter1.lower()  in "aeiouō":
                karaSplit_array.append(letter+letter1 )
                l=l+2
            else:
               karaSplit_array.append(letter)
               l=l+1

        elif letter.lower() == "w":
            if letter1.lower()  in "aoō":
                karaSplit_array.append(letter+letter1 )
                l=l+2
            else:
               karaSplit_array.append(letter) 
               l=l+1
        #if letter == "y":
        elif letter.lower() == "t":
            if letter1.lower() in "aeoō":
                karaSplit_array.append(letter+letter1 )
                l=l+2
            elif letter1.lower() == "s":
                if 0 <= l+2 < len(karaText):
                    letter2=karaText[l+2]
                    karaSplit_array.append(letter+letter1+letter2 )
                l=l+3
            else:
               karaSplit_array.append(letter)
               l=l+1

        elif letter.lower() == "c":
            if letter1.lower() == "h":
                if 0 <= l+2 < len(karaText):
                    letter2=karaText[l+2]
                    karaSplit_array.append(letter+letter1+letter2 )
                l=l+3
            else:
               karaSplit_array.append(letter+letter1) 
               l=l+2
        
        elif letter.lower() == "s":
            if letter1.lower() in "aueoō":
                karaSplit_array.append(letter+letter1 )
                l=l+2
            elif letter1.lower() == "h":
                if 0 <= l+2 < len(karaText):
                    letter2=karaText[l+2]
                    karaSplit_array.append(letter+letter1+letter2 )
                l=l+3
            else:
               karaSplit_array.append(letter) 
               l=l+1
        elif letter.lower() == "f":
            if letter1 == "u":
                karaSplit_array.append(letter+letter1 )
                l=l+2
            else:
               karaSplit_array.append(letter) 
               l=l+1

        elif letter.lower() in "aeiou":
            if letter1.lower()  in "aeiou":
                karaSplit_array.append(letter)
                l=l+1
            else:
                #this should not happen it is only the case above, nothing is supposed to end with these letter
                karaSplit_array.append(letter)
                l=l+1

        elif letter == "{":
            nxindx=1
            if len(karaSplit_array) > 0:
                karaSplit_array [ len(karaSplit_array)-1 ] =  karaSplit_array [ len(karaSplit_array)-1 ]+letter
            else:
                karaSplit_array.append(letter)
            if l+nxindx < len(karaText):
                ltr=karaText[ l+nxindx  ]
                while ltr != "}":
                    ltr=karaText[ l+nxindx  ]
                    
                    karaSplit_array [ len(karaSplit_array)-1 ] =  karaSplit_array [ len(karaSplit_array)-1 ]+ltr
                    nxindx=nxindx+1
                    if not (l+nxindx < len(karaText)):
                        break

            l=l+nxindx

        elif letter in [" ","!","?",",",";",":","}"]:
            if len(karaSplit_array)>0:
                karaSplit_array [ len(karaSplit_array)-1 ] =  karaSplit_array [ len(karaSplit_array)-1 ]+letter
                l=l+1
            else:
                karaSplit_array.append (letter)
                l=l+1    
        else:
            if letter1.lower() in "aeiou":
                karaSplit_array.append (letter+letter1)
                l=l+2
            else:
                karaSplit_array.append (letter)
                l=l+1

    return karaSplit_array


def arrTOk_str(karaSplit_array, timePerletter):
    finalKaraStr=""
    for syl in karaSplit_array:
        l = timePerletter * len(syl)
        k = "{\\k%s}" % l
        finalKaraStr += k+syl 
    return finalKaraStr




if __name__ == "__main__":
    #parsing args
    parser = argparse.ArgumentParser(description="does the k-split for aegisub karaoke (you have to adjust the timing by yourself after splitting)")
    
    parser.add_argument('-s','--selector',metavar = '', required=True, help='criteria of lines to apply the script on: all , actor or style')
    parser.add_argument('-sv','--selectorvalue',metavar = '', help='if you choose actor or style, specify the name here, use "" for names with spaces "op kara" ')
    #parser.add_argument('-p','--pattern',metavar = '', required=True, help='criteria of lines to apply the script on: all , actor or style')
    

    groupSelector = parser.add_mutually_exclusive_group()
    groupSelector.add_argument('-syl','--syllables',action='store_const',dest='mode',const='syl', help='makes splitting by romaji syl (default) [only pick one the three char,syl,word]')
    groupSelector.add_argument('-char','--characters',action='store_const',dest='mode',const='char', help='makes splitting after each character[only pick one the three char,syl,word]')
    groupSelector.add_argument('-word','--word',action='store_const',dest='mode',const='word' ,help='makes splitting after each word[only pick one the three char,syl,word]')
    parser.set_defaults(mode='syl')

    parser.add_argument('-f','--filename',metavar = '', required=True, help='rel or abs path for the .ass file')
    
    args = parser.parse_args()

    input_filepath = args.filename
    selector = args.selector
    selector_value = args.selectorvalue
    mode = args.mode
    
    
    if not ( selector in ["actor", "style", "all"] ):
        print('your selector (-s / --selector) has to be either "actor", "style", or "all", you entered: '+selector)
        print( "\n")
        print("exiting...")
        sys.exit(-1)
    if selector in ["actor", "style"]:
        if selector_value== None:
            print('your selector is not "all" for "actor", "style",you have to enter the name with -sv/ --selectorvalue = KaraName')
            print( "\n")
            print("exiting...")
            sys.exit(-1)
    if not ( mode in ["syl", "char", "word"] ):
        print('your splitting mode has to be either "syl", "char", or "word", you entered: '+ mode)
        print( "\n")
        print("exiting...")
        sys.exit(-1)

    
        #now we start real work, create output file
    f = input_filepath.split('.')[0]
    ext =  input_filepath.split('.')[1]
    d =  datetime.datetime.now().strftime("%d-%m-%Y-%H.%M.%S")

    out_f= open("%s_Koutput[%s].%s"%(f,d,ext),"w+",encoding='UTF8')
    #open input file and iterate over each of its lines to k-split it if applicable
    with open(input_filepath, "r",encoding='UTF8') as sub_file:
        counter = 0
        for line in sub_file:
            #input = "Dialogue: 0,0:00:00.00,0:00:05.30,Default,,0,0,0,,Tsuyo nara yuuki bashou da"
            #print(line)
            input = line.strip()
            
            if input.find("Dialogue") != -1:
                inputarray = input.split(',',9)

                if selector == "actor":
                    match = inputarray[4]
                elif selector == "style":
                    match = inputarray[3]
                elif selector == "all":
                    match = "True"
                    selector_value="True"
                

                
                if match.lower() == selector_value.lower() :
                    duration_ds = aegiTimeTOds(inputarray[2]) - aegiTimeTOds(inputarray[1])
                    karaRawText = inputarray[9]
                    #print (karaRawText)
                    text_len = len (karaRawText)
                    counter = counter +1
                    if text_len >0:
                        timePerletter=  int(duration_ds/ text_len)
                        karaSplit_array = str_TOkara_array(karaRawText, mode)

                        #finalKaraStr =  [0] + arrTOk_str(karaSplit_array, timePerletter)
                        finalKaraStr =""
                        
                        first_part = input.split(',', 9)
                        for x in range(9):
                            finalKaraStr += "%s," %first_part[x]
                        
                        finalKaraStr += arrTOk_str(karaSplit_array, timePerletter)

                    else:
                        finalKaraStr = input

                else:
                    finalKaraStr=  input

                out_f.write(finalKaraStr)
                out_f.write("\n")
            else:
                #concat to output file 
                input = line.strip()
                out_f.write(input)
                out_f.write("\n")

    print("found: %s lines matching your criteria" %(counter) )
    print("all done! wrote in file: %s_Koutput[%s].%s"%(f,d,ext) )
