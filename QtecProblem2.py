testString = 'tadadattaetadadadafa'

count = 0
for i in range(0,testString.__len__() - 3):
    if((testString[i]=='d') and (testString[i+1]=='a') and (testString[i+2]=='d') and (testString[i+3]=='a') ):
        count+=1

print(f"Here the pattern (dada) appears in text ({testString}) {count} times.")
