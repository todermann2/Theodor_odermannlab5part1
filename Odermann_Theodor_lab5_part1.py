"""

This program will decode words that have been miswritten

"""

def main():
	#encoded_word = "WBLARF8TTS"
	#encoded_word = "L8KAOUL"
	#encoded_word = "E8N8N8"
	#encoded_word = "8TRA8DY T8LA"
	#encoded_word = "8TT LHA TILLTA LIMAS"	
	#encoded_word = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encoded_word = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	print(DecodeWord(encoded_word))



def DecodeWord(encoded_word):
	decoded_word = ''
	for x in encoded_word :
		if x == 'L' :
			decoded_word += 'T'
		elif x == 'T' :
			decoded_word += 'L'
		elif x == '8' :
			decoded_word += 'A'
		elif x == 'B' :
			decoded_word += 'A'
		elif x == 'A' :
			decoded_word += 'E'
		elif x == 'E' :
			decoded_word += 'B'
		else:
			decoded_word += x
	return decoded_word


#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
