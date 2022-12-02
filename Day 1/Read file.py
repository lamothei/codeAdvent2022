myfile = 'input.txt'
sum = 0
sumArray = []
with open(myfile) as fh:
    for n in fh:
        n = n.strip()
        
        if not n or n.startswith('#'):
            sumArray.append(int(sum))
            sum = 0
            continue
        sum = sum + int(n)
    sorted_list =sorted(sumArray)
    print ('biggest number is ', sorted_list[-1])

    lrgSumThree = int(sorted_list[-1]) + int(sorted_list[-2]) + int(sorted_list[-3])
    print("The three largest numbers summed together are", lrgSumThree)