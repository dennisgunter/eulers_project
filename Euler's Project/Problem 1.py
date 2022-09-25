#Euler's Project
#Prolem 1
#Maximilian Prietzel
#25.09.2022

def main(n=1000): #Number which do'nt get passed
    erg = 0 #collecting the sum
    for i in range(1,n):
        if i%3 == 0 or i%5 == 0:
            erg += i
            print(i)

    print(erg)
    return erg

if __name__ == "__main__":
    main()

