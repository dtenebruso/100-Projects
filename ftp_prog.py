#!/usr/bin/python3

from ftplib import FTP

class FTPClient():

	def connect_ftp(self, host, uname, passwd):

		ftp = FTP(host)

		try:
			ftp.login(uname, passwd)
			print("Connected to %s as %s"%(host, uname))
			ftp.cwd('/')
			ftp.dir()

			try:
				query = input("\n\nWhat file would you like to download : ")
				output = 'C:\\Users\\Me\\Documents\\test'

				with open(output, 'wb') as f:
					ftp.retrbinary('RETR ' + query, f.write)

				print("\nDownloading....")

				print("\nDownload Successful")

			except:
				print("\nDownload Failed")

			try:
				src_file = 'tester.txt'
				
				with open(src_file, 'rb') as upObj:
					ftp.storbinary('STOR ' + src_file, upObj, 1024)

				print("\nUploading...")

				print("\nUpload Successful")

			except:
				print("\nUpload Failed")



		except:
			print("Error connecting to ftp")
		
		ftp.quit()



if __name__ == "__main__":

	sess1 = FTPClient()

	sess1.connect_ftp('aPCwhere','dylant', 'secretpass')