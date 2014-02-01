import xlrd
class ReadExcel:
	
	def readTweets(self):
		wb=xlrd.open_workbook('Tweets.xls')
		Obamash=wb.sheet_by_index(0);
		#Obamatweets=Obamash.col_values(4)
		obamaTuple= []
		obamaTweet=[]
		for rownum in range(Obamash.nrows):
			obamaTuple=(unicode((Obamash.cell(rownum,3).value)).encode('utf-8'),(Obamash.cell(rownum,6).value))
			obamaTweet.append(obamaTuple)
		
		

		Romneysh=wb.sheet_by_index(1);
		RomneyTuple=[]
		RomneyTweet=[]
		for rownum in range(Romneysh.nrows):
			RomneyTuple=(unicode((Romneysh.cell(rownum,3).value)).encode('utf-8'),(Romneysh.cell(rownum,6).value))
			RomneyTweet.append(RomneyTuple)
			
		return 	obamaTweet,RomneyTweet		