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
            
def Pr(Text, Profile):
    probability = 1
    for i in range(len(Text)):
        probability = probability * Profile[Text[i]][i]
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    max_probability = 0
    most_probable = Text[:k]
    n = len(Text)
    for i in range(n - k + 1):
        kmer = Text[i: i + k]
        probability = Pr(kmer, Profile)
        if probability > max_probability:
            max_probability = probability
            most_probable = kmer
    return most_probable
    
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
    return BestMotifs


teste = {'A':[0.4, 0.3, 0.0,  0.1,  0.0,  0.9], 'C':  [0.2,  0.3,  0.0,  0.4,  0.0,  0.1], 'T': [ 0.3,  0.1,  0.0,  0.4,  0.5,  0.0], 'G': [0.1,  0.3,  1.0,  0.1,  0.5,  0.0],}
print(Pr("AAGTTC",teste))