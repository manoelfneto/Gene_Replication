import random

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

def CountWithPseudocounts(Motifs):
    pseudo = {}
    k = len(Motifs[0])
    for i in "ACGT":
        pseudo[i] = []
        for j in range(k):
            pseudo[i].append(1)
    t = len(Motifs)
    for x in range(t):
        for y in range(k):
            symbol = Motifs[x][y]
            pseudo[symbol][y] += 1
    return pseudo

def ProfileWithPseudocounts(Motifs):
    contPseudo = CountWithPseudocounts(Motifs)
    for i in range(len(Motifs[0])):
        su=0
        for symbol in "ACGT":
            su = su + contPseudo[symbol][i]
        for symbol in "ACGT":
            contPseudo[symbol][i] = contPseudo[symbol][i] / su
    profile = contPseudo
    return profile

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
    return BestMotifs

def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    k = len(Profile['A'])
    for i in range(t):
        motif = ProfileMostProbableKmer(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs

def RandomMotifs(Dna, k, t):
    t = len(Dna)
    l = len(Dna[0])
    RandomMotif =[]
    for i in range(t):
        r = random.randint(1,l-k) 
        RandomMotif.append(Dna[i][r:r+k])
    return RandomMotif

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs

def Normalize(Probabilities):
    probabil = {}
    soma = 0
    probabil = Probabilities
    for x in Probabilities:
        soma += Probabilities[x]
    for i in probabil:
        probabil[i] = probabil[i] / soma 
    return probabil

def WeightedDie(Probabilities):
    count = 0
    p = random.uniform(0,1)
    for keys,values in Probabilities.items():
        count = count +values
        if p < count:
            return keys

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def GibbsSampler()
        
entrada = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
print(WeightedDie(entrada))
