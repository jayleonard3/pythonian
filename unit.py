import re


M_TO_FT = 3.28

class Converter:
    #Constant for conversion factors
    M_TO_FT = 3.28

    imperial = ['in','ft']
    metric = ['cm','m']

    unit_from = ''
    unit_to = ''
    converted_number = ''



    def convert(self, num, unit_from, unit_to):
        if unit_from == 'in':
            if unit_to == 'ft':
                return num / 12
            if unit_to == 'cm':
                return (num/12) / M_TO_FT * 100
            if unit_to == 'm':
                return (num/12) / M_TO_FT
        if unit_from == 'ft':
            if unit_to == 'in':
                return num * 12
            if unit_to == 'cm':
                return num / M_TO_FT * 100
            if unit_to == 'm':
                return num / M_TO_FT
        if unit_from == 'cm':
            if unit_to == 'in':
                return num/100 * M_TO_FT * 12
            if unit_to == 'ft':
                return num/100 * M_TO_FT
            if unit_to == 'm':
                return num/100
        if unit_from == 'm':
            if unit_to == 'in':
                return num * M_TO_FT * 12
            if unit_to == 'cm':
                return num * 100
            if unit_to == 'ft':
                return num * M_TO_FT


    #Processes input in the form of 123ft cm
    def parse(self, input_str):
        i = 0
        while input_str[i].isdigit() or input_str[i] == '.':
            i += 1
        
        num = input_str[0:i]
        j = i
        while input_str[j] != ' ':
            j += 1
        unit_from = input_str[i:j]
        unit_to = input_str[j+1:]
        print(str(self.convert(float(num), unit_from, unit_to)) + unit_to)
    
                     
            
def is_valid_input(string):
    return re.match(r'(\d*.\d*|\d*)(in|cm|ft|m)\s(in|cm|ft|m)',string) != None
    
        

if __name__ == '__main__':
    while(True):
        print('Enter conversion in the form <number><unit>  <unit>')
        print('Supported units: in, ft, cm, m')
        
        user_input = input()
        if(is_valid_input(user_input)):
            conv = Converter()
            conv.parse(user_input)
        else:
            print('Invalid Syntax')