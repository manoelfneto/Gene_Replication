def Count (motifs):
    count = {}
    k = len(motifs[0])
    for i in "ACGT":
        count[i] = []
        for j in range(k):
            count[i].append(0)
    t = len(motifs)
    for x in range(t):
        for y in range(k):
            symbol = motifs[x][y]
            count[symbol][y] += 1
    return count

def Profile(Motifs):
    profile = {}
    matriz_count = Count(Motifs)
    profile = matriz_count
    for i in profile:
        for y in range(len(Motifs[0])):
            profile[i][y] = profile[i][y] / len(Motifs)
    return profile     
            
def Consensus(Motifs):
    consensus = ""
    count = Count(Motifs)
    for i in range(len(Motifs[0])):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][i] > m:
                m = count[symbol][i]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    final_sum = 0
    consensus = Consensus(Motifs)
    for x in range(len(Motifs)):
        for y in range(len(Motifs[0])):
            if consensus[y] != Motifs[x][y]:
                final_sum += 1
    return final_sum
            

teste = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
print(Score(teste))