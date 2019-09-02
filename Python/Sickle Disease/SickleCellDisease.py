#program that simulates the effects of the single nucleotide polymorphism that leads to genetic disease
def translate(sequence):
        CODON = list()#creating list to append codons
        thisList = changer(sequence)        
        count = 0 
        for line in thisList:
                #creating codition
                if line == "ATT" or line == "ATC" or line == "ATA":
                        CODON.append('I')
                #creating codition or line == "TTA" or line == "TTG"
                elif line == "CTT" or line == "CTC" or line == "CTA" or line == "CTG":
                        CODON.append(' L')
                        
                elif line == "GTT" or line == "GTC" or line == "GTA" or line == "GTG":
                        CODON.append(' V')
                elif line == "TTT" or line == "TTC":
                        CODON.append(' F')
                elif line == "ATG":
                        CODON.append(' M')
                else:
                        CODON.append(' X')

        print (CODON)
#f.close()

#function that creates two text files
#one file is normal and the oter is mutated
normalFile = open("normalDNA.txt", "w+")#creating file for normal DNA
mutatedFile = open("mutatedDNA.txt", "w+")#creating file for mutated DNA
def mutate():

        with open("DNA.txt", "r")as open_file_DNA:#open text file to read from
                read_file_DNA = open_file_DNA.read()#reads the DNA file
                normal_DNA = read_file_DNA.replace("a", "A")#creating normal DNA structure
                mutated_DNA = read_file_DNA.replace("a", "T")#creates mutated DNA structure

                normalFile = open("normalDNA.txt", "w")
                normalFile.write(normal_DNA + "\n")#writes normal DNA structure in "normalFile.txt"

                mutatedFile = open("mutatedDNA.txt", "w")
                mutatedFile.write(mutated_DNA + "\n")#writes mutated DNA structure in "mutatedFile.txt"

mutate()

def changer(string):

        alist = list()
        text = ""
        

        for char in string:             # ATGADSATT
                text += char

                if len(text) == 3:                      #breaks after 3 characters are stored in text
                        alist.append(text)              #puts characters in list
                        text = ""                       #clears text again to continue with rest of line
                        string = string[3:]
                if len(string) < 3:
                        text = string + "X"
                        alist.append(text)      #stores in list called alist
                        break
                        
        
        return alist



    
sequence = input("Enter a sequence:")
translate(sequence.upper())
