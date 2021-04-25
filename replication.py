def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Text_slices = Text[i:i+k]
        freq[Text_slices] = 0
    for x in range(n-k+1):
        if Text[x:x+k] in freq:
            freq[Text[x:x+k]] = freq[Text[x:x+k]] + 1

    return freq

def FrequentWords(Text, K):
    maximum_words = []
    freq = FrequencyMap(Text, K)
    maximum_value = max(freq.values())
    for i in freq:
        if freq[i] == maximum_value:
            maximum_words.append(i)
    return maximum_words

def Reverse(Text):
    reversed = ""
    for i in range(len(Text)-1, -1, -1):
        reversed += str(Text[i])
    return reversed

def Complement(Text):
    complement = ""
    for i in Text:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return complement

def ReverseComplement(Text):
    pattern = Reverse(Text) 
    pattern = Complement(pattern) 
    return pattern

def PatternMatching(Pattern, Genome):
    positions = []
    for i in range (len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    positions.sort()
    return positions


vibrio_cholerae = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
thermotoga_petrophila = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"
texto_pequeno = "CTTGATCATCTTGATCATCTTGATCAT" 
padrão = "CCTACCACC"

print (PatternCount(thermotoga_petrophila, padrão))