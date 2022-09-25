#Euler's Project
#Prolem 2
#Maximilian Prietzel
#25.09.2022

def main(n=4000000): #Number which do'nt get passed
    i,j = 1,1 #Startnumbers of fibonacci
    erg = 0 #Collecting sum

    while j < n:
        if j % 2 == 0:  #if even add to the sum
            erg += j
        j += i
        i = j

    print(erg)
    return erg
 
if __name__ == "__main__":
    main()
