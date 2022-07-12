'''
There are two numbers: Less and Greater.
Knowing the Step, or the Amount of array numbers, 
you need to find the values of numbers from the array:
L ; L+S ; L+2S + ... + L+(A-2)S + L+(A-1)S,
where the first number is L and the last is G = L+(N-1)S.
Knowing the value of S {A} we will find the value of A {S}.
S = (G-L)/(A-1) & A = 1 + [(G-L)/S].
'''

def limitsOfTask():
    L,G = map(int,input("Enter Lower & Greater numbers : ").split())
    if L >= G: L,G = G,L
    return G,L

def questionnaire(G,L):
    Q = input("Would you like to specify the Step or Amount of numbers in the array? [ S & A ] : ")
    
    if any(Q.capitalize() in urAnswer for urAnswer in ["S","Step"]):
        S = float(input("Specify Step : "))
        A = int(1 + ((G-L)/S))
        print("The Amount of numbers : ", A)
    elif any(Q.capitalize() in urAnswer for urAnswer in ["A","Amount"]):
        A = int(input("Specify the Amount of numbers : "))
        S = float((G-L)/(A-1))
        print("Step : ", S)
    else:
        raise TypeError("error: another answer entered".upper())
    return G,L,A,S

def arrayFillingLogic(G,L,A,S):
    arrayFloat = []
    for number in range(0,A):
        arrayFloat.append(round((L+(number)*S),2))
    if arrayFloat[-1] == G:
        return arrayFloat
    else:
        raise TypeError(f"error: {*arrayFloat,} task is unsolvable".upper())

if __name__== '__main__':
    G,L = limitsOfTask()
    G,L,A,S = questionnaire(G,L)
    arrayFloat = arrayFillingLogic(G,L,A,S)[::-1]
    print(', '.join([str(parameter) for parameter in arrayFloat]))