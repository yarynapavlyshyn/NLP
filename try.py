import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def get_input():
     sentences = []
     n = 0
     while True:
          s_n = input("s{}: ".format(n+1)) # here we don`t know if we will have an input so haven`t increase n yet
          if s_n:
               n += 1 # now we can increase
               sentences.append(s_n)
          else: break
     return sentences

# sentences, N = get_input()

def similarity_in_percents(s1, s2):
     vector1 = text_to_vector(s1)
     vector2 = text_to_vector(s2)
     cos = get_cosine(vector1, vector2)
     absolute_persentage = abs(cos*100)
     return absolute_persentage

def grid_of_similiarities(sentences):
     """
     Create a grid n*n where n is a number of sentences we need to compare to each other
     :param sentences: list(str)
     :return: list(list(int))
     """
     N = len(sentences)
     grid = [[None for j in range(N)] for i in range(N)]
     for r in range(N): # rows
          for c in range(N): # columns
               if grid[r][c] is None:
                    grid[r][c] = grid[c][r] = int(similarity_in_percents(sentences[c], sentences[r]))
     return grid

def print_Grid(grid):
    n = len(grid)
    for i in range(0,n):
        i_th_line = "s{}: ".format(i)
        for j in range(n-1):
            i_th_line += str(grid[i][j]) + ", "
        i_th_line += str(grid[i][n-1])
        print(i_th_line)


text1 = 'This is a foo bar sentence.'
text2 = 'This sentence is similar to a foo bar sentence .'
sents = [text1, text2]
grid = grid_of_similiarities(sents)
print_Grid(grid)