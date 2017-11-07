import  random
##############
print("------------------------  WELCOME TO CRC ERROR DETECTION SIMULATOR -------------------------")
print("")

def xor(a, b):
	xored = []
	for i in range(1, len(b)):
		if a[i] == b[i]:
			xored.append('0')
		else:
			xored.append('1')

	return ''.join(xored)
############
def div(divident, divisor):
	l = len(divisor)
	arr = divident[0 :l]

	while l < len(divident):

		if arr[0] == '1':
			arr = xor(divisor, arr) + divident[l]

		else:
			arr = xor('0'*l, arr) + divident[l]
		l += 1

	if arr[0] == '1':
		arr = xor(divisor, arr)
	else:
		arr = xor('0'*l, arr)

	code_word = arr
	return code_word

#######################################


message=input("Enter data stream :")
while len(message)%16!=0:
    message="0"+message
print("message           :",message)
#CRC-8 = x8 + x2 + x + 1
crc="100000111"
print("CRC-8             :",crc)
new_msg=""
appended=""
for i in range(int(len(message)/16)):
    new_msg=message[i*16:(i+1)*16]
    appended=appended+new_msg+"00000000"
    #print("appended:",appended)

print("__________________________________________________________________________________________________________________")
final=""
new=""
for i in range(int(len(appended)/24)):
    #print("hello")
    appended_data=appended[i*24:(i+1)*24]###extracted appended_zeros from one word
    print(i+1," appended data word :",appended_data)
    remainder=div(appended_data,crc)
    print("Syndrome(remainder)   :",remainder)
    print("--------------------------------------------------------------------------------------------------------------")
    new= message[i*16:(i+1)*16]
    final=final+new+remainder

#print("Final Codeword Generated at Sender Side : ",final)
#################################################################
codeword=list()
for i in range(len(final)):
    codeword.append(int(final[i]))
print("...................................................................................................................................................................")
print("Final Codeword Generated at Sender Side : ",codeword)
print("...................................................................................................................................................................")
print("Data is ready for transmission.....")
print("_____________________________________________________________________________________________________________________________________________________________")
print("")
hop=int(input("Enter number of HOPS : "))
if hop==1:
    p=float(input("Enter user probability : "))
if hop==2:
    p = float(input("Enter 1st user probability : "))
    q = float(input("Enter 2nd user probability : "))
    pt=p*(1-q)+q*(1-p)
print("__________________________________________________________________________________________________")
final2=[]
final_2=""

for i in range(int(len(final)/24)):
    final1=final[24*i:(i+1)*24]
    #print("final 1:",final1)
    if hop==1:
        values=range(11)
       # p_rand=random.choice(values)/10
       # print("Random probability : ",p_rand)
        #if(p_rand<=p):
            #print("hello")
        for i in range(len(final1)):
           final2.append(int(final1[i]))

        print("Original Word         :", final2)

        for i in range(len(final2)):
            p_rand = random.choice(values) / 10
            if p_rand<p:
                if final2[i]==1:
                    final2[i]=0
                else:
                    final2[i]=1
        print("Data word with error  :",final2)
        #else:
        #for i in range(len(final1)):
         #   final2.append(int(final1[i]))
        #print("Data word without error :", final2)
    #print("final2:", final2)

    if hop==2:
        values = range(11)
        #p_rand = random.choice(values) / 10
        #print("random p=", p_rand)
        #if (p_rand <= pt):
        for i in range(len(final1)):
            final2.append(int(final1[i]))

        print("Original Word ", i + 1, " : ", final2)
        for i in range(len(final2)):
            p_rand = random.choice(values) / 10
            if p_rand<pt:
                if final2[i] == 1:
                    final2[i] = 0
                else:
                    final2[i] = 1
        print("Data word with error  :", final2)

        #else:
         #   for i in range(len(final1)):
          #      final2.append(int(final1[i]))
           # print("Data word without error :", final2)

    print("------------------------------------------------------------------------------------------------------------")
    for i in range(len(final2)):
        if final2[i]==1:
            final_2=final_2+'1'
        else:
            final_2=final_2+'0'
    final2=[]
print("__________________________________________________________________________________________________________________________________________________________________________")
print("Data after passing through Binary Symmetric Channel :",final_2)
print("__________________________________________________________________________________________________________________________________________________________________________")

##final_2 contains all data with+without error!!!!!remember it
print("")
print("___________________________________________________________")
print("*****************  error detection  **********************")
print("___________________________________________________________")
for i in range(int(len(final_2)/24)):
    #print("hello")
    e_final=final_2[i*24:(i+1)*24]###extracted 24 word which may or may not contain errorr!!!
    print("Data word ",i+1," : ",e_final)
    remainder=div(e_final,crc)
    print("Syndrome:",remainder)
    if remainder=="00000000":
        print("word ",i+1," accepted :)")
    else:
        print("word ", i + 1, " discarded :(")
    print("-----------------------------------------------------------------")
#####################################################################
#completed loc=145
n=input()


