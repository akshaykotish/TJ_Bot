
class DTConverter(object):
    def __init__(self): 
        self.word = ""


    def Words2Num(self, data):
        output = 27

        for w in data:
            if(w.lower() == 'a'):
                output = output * 100 + 1
            elif(w.lower() == 'b'):
                output = output * 100 + 2
            elif(w.lower() == 'c'):
                output = output * 100 + 3
            elif(w.lower() == 'd'):
                output = output * 100 + 4
            elif(w.lower() == 'e'):
                output = output * 100 + 5
            elif(w.lower() == 'f'):
                output = output * 100 + 6
            elif(w.lower() == 'g'):
                output = output * 100 + 7
            elif(w.lower() == 'h'):
                output = output * 100 + 8
            elif(w.lower() == 'i'):
                output = output * 100 + 9
            elif(w.lower() == 'j'):
                output = output * 100 + 10
            elif(w.lower() == 'k'):
                output = output * 100 + 11
            elif(w.lower() == 'l'):
                output = output * 100 + 12
            elif(w.lower() == 'm'):
                output = output * 100 + 13
            elif(w.lower() == 'n'):
                output = output * 100 + 14
            elif(w.lower() == 'o'):
                output = output * 100 + 15
            elif(w.lower() == 'p'):
                output = output * 100 + 16
            elif(w.lower() == 'q'):
                output = output * 100 + 17
            elif(w.lower() == 'r'):
                output = output * 100 + 18
            elif(w.lower() == 's'):
                output = output * 100 + 19
            elif(w.lower() == 't'):
                output = output * 100 + 20
            elif(w.lower() == 'u'):
                output = output * 100 + 21
            elif(w.lower() == 'v'):
                output = output * 100 + 22
            elif(w.lower() == 'w'):
                output = output * 100 + 23
            elif(w.lower() == 'x'):
                output = output * 100 + 24
            elif(w.lower() == 'y'):
                output = output * 100 + 25
            elif(w.lower() == 'z'):
                output = output * 100 + 26

        
        #print(output)
        return output

    def Num2Words(self, data):
        output = ""
        
        while data != 0:
            value = int(data%100)
            
            if value == 1:
                output = "a" + output
            elif value == 2:
                output = "b" + output
            elif value == 3:
                output = "c" + output
            elif value == 4:
                output = "d" + output
            elif value == 5:
                output = "e" + output
            elif value == 6:
                output = "f" + output
            elif value == 7:
                output = "g" + output
            elif value == 8:
                output = "h" + output
            elif value == 9:
                output = "i" + output
            elif value == 10:
                output = "j" + output
            elif value == 11:
                output = "k" + output
            elif value == 12:
                output = "l" + output
            elif value == 13:
                output = "m" + output
            elif value == 14:
                output = "n" + output
            elif value == 15:
                output = "o" + output
            elif value == 16:
                output = "p" + output
            elif value == 17:
                output = "q" + output
            elif value == 18:
                output = "r" + output
            elif value == 19:
                output = "s" + output
            elif value == 20:
                output = "t" + output
            elif value == 21:
                output = "u" + output
            elif value == 22:
                output = "v" + output
            elif value == 23:
                output = "w" + output
            elif value == 24:
                output = "x" + output
            elif value == 25:
                output = "y" + output
            elif value == 26:
                output = "z" + output

            data = int(data/100)
            

        
        #print(output)
        return output

