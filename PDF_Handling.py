from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from datetime import datetime
import time
from pathlib import Path



class PDF_Stuff:

	def __init__(self, filepath,output_dir,overwrite):

		self.infile = filepath
		self.output_dir = output_dir
		self.overwrite = overwrite

		# Open the pdf file and get the meta data
		with open(self.infile, "rb") as pdf_handler:
			# Get the data from the pdf file handler
			self.pdf = PdfFileReader(pdf_handler)

			# Get the document info
			self.info = self.pdf.getDocumentInfo()

			# Get the number of pages present in the pdf file.
			self.number_of_pages = self.pdf.getNumPages()


	# Get the meta data or the PDF doc info
	def getDocInfo(self):

		# Print the Pdf File Info  and the Creator information
		print("The Meta data of the Pdf file is : ", self.info)
		print("The Creator of Pdf file is : ", self.info.creator)

		# Print the Producer and the Title of the PDF file.
		print("The Producer of the Pdf file  is : ", self.info.producer)
		print("The Title of the Pdf file is : ", self.info.title)

		# Print the Subject and the Total No. of Pages of the PDF file.
		print("The Subject of the Pdf file is : ", self.info.subject)
		print("The total number of pages present in the Pdf file is  : ", self.number_of_pages)


	# Method to split the pdf file after the given page number
	def split_after(self, page_num):

		# Copy the total number of pages in PDF file to a local variable pdf_len
		pdf_len = self.number_of_pages
		outdir = self.output_dir
		overwrite = self.overwrite

		if (page_num > pdf_len):
			print("The page number {0} entered is greater than the total number of pages {1}".format(page_num, pdf_len))

			#   When page number is greater than the len of the file
			#   IndexError: list index out of range

		elif (page_num <= 0):
			print("Enter a valid page number between 1 and {0}".format(pdf_len - 1))

			# When page number is -33
			# UnboundLocalError: local variable 'outfile' referenced before assignment

		else:
			# Copy the input file path to a local variable infile
			infile = self.infile
			input_pdf = PdfFileReader(open(infile, "rb"))

			#Get the complete file name along with its path and split the text to take only the first part.
			fname = os.path.splitext(os.path.basename(infile))[0]

			# Initialize the PDF File Writers
			# For the first part before the split
			output_1 = PdfFileWriter()
			# For the Second Part after the split
			output_2 = PdfFileWriter()

			# Loop through the pages and add the page data to the output
			for page in range(page_num):

				# Get the data from the given page number
				page_data = input_pdf.getPage(page)

				# Add the page data to the pdf_writer
				output_1.addPage(page_data)

				# Frame the output file name
				output_1_name = '{}_page_{}_'.format(fname, page + 1)
				output_1_filename = Path(outdir,output_1_name)

			# Write the file data to the output file
			self.write_to_file(output_1_filename, output_1, overwrite)

			# Loop through the pages and add the page data to the output
			for page in range(page_num,pdf_len):

				# Get the data from the given page number
				page_data = input_pdf.getPage(page)

				# Add the page data to the pdf_writer
				output_2.addPage(page_data)

				# Frame the output file name
				output_2_name = '{}_page_{}_'.format(fname, page + 1)
				output_2_filename = str(Path(outdir, output_2_name))
			# Write the file data to the output file
			res = self.write_to_file(output_2_filename,output_2, overwrite)
			if (res):
				print("Splitted the PDF successfully")


	# Method to split the pdf at every given n pages.
	def split_at_every(self,step = 1):

		outdir = self.output_dir
		overwrite = self.overwrite

		# Copy the total number of pages in PDF file to a local variable pdf_len
		pdf_len = self.number_of_pages

		# Copy the input file path to a local variable infile
		infile = self.infile
		input_pdf = PdfFileReader(open(infile, "rb"))

		# Get the complete file name along with its path and split the text to take only the first part.
		fname = os.path.splitext(os.path.basename(infile))[0]

		# Get the list of page numbers in the order of given step
		# If there are 10 pages in a pdf, and the step is 2
		# page_numbers = [0,2,4,6,8]
		page_numbers = list(range(0,pdf_len,step))

		# Loop through the pdf pages
		for ind,val in enumerate(page_numbers):

			# Check if the index is last in the given page numbers
			# If the index is not the last one, carry on with the If block.
			if(ind+1 != len(page_numbers)):

				# Initialize the PDF Writer
				output_1 = PdfFileWriter()

				# Loop through the pdf pages starting from the value of current index till the value of next index
				# Ex : page numbers = [0,2,4,6,8]
				# If the current index is 0, loop from 1st page till the 2nd page in the pdf doc.
				for page in range(page_numbers[ind], page_numbers[ind+1]):

					# Get the data from the given page number
					page_data = input_pdf.getPage(page)

					# Add the page data to the pdf_writer
					output_1.addPage(page_data)

					# Frame the output file name
					output_1_name = '{}_page_{}_'.format(fname, page + 1)
					output_1_filename = Path(outdir, output_1_name)

				# Write the output content to the file and save it.
				res = self.write_to_file(output_1_filename, output_1, overwrite)
				if (res):
					print("Splitted the PDF successfully")

			else:

				output_final = PdfFileWriter()
				# output_final_filename = "Last_Pages"

				# Loop through the pdf pages starting from the value of current index till the last page of the pdf doc.
				# Ex : page numbers = [0,2,4,6,8]
				# If the current index is 8, loop from 8th page till the last page in the pdf doc.

				for page in range(page_numbers[ind], pdf_len):
					# Get the data from the given page number
					page_data = input_pdf.getPage(page)

					# Add the page data to the pdf_writer
					output_final.addPage(page_data)

					# Frame the output file name
					output_final_filename = '{}_page_{}_'.format(fname, page + 1)
					output_final_filename = Path(outdir, output_final_filename)


				# Write the output content to the file and save it.
				self.write_to_file(output_final_filename, output_final, overwrite)

	# Split the PDF file by page ranges
	def split_pages(self, page_range):
		""" Take a pdf file and copy a range of pages into a new pdf file

		Args:
			input_file: The source PDF file
			page_range: A string containing a range of pages to copy: 1-3,4
			out_file: File name for the destination PDF
		"""

		global app

		overwrite = self.overwrite
		# Get the input file and instantiate the PDF File Reader
		infile = self.infile
		input_pdf = PdfFileReader(open(infile, "rb"))

		# Get the Output File directory and frame the output file name
		outdir = self.output_dir
		fname = os.path.splitext(os.path.basename(infile))[0] + "_Ranges_"
		output_file_name = Path(outdir, fname)

		# Instantiate the PDF File Writer
		output = PdfFileWriter()

		# https://stackoverflow.com/questions/5704931/parse-string-of-integer-sets-with-intervals-to-list
		page_ranges = (x.split("-") for x in page_range.split(","))
		range_list = [i for r in page_ranges for i in range(int(r[0]), int(r[-1]) + 1)]

		for p in range_list:
			# Need to subtract 1 because pages are 0 indexed
			try:
				output.addPage(input_pdf.getPage(p - 1))
			except IndexError:
				# Alert the user and stop adding pages
				app.infoBox("Info", "Range exceeded number of pages in input.\nFile will still be saved.")
				break
		# Send the content and file name to write
		res = self.write_to_file(output_file_name,output, overwrite)
		if(res):
			print("Splitted the PDF successfully")



	# Method to write the content to the file
	def write_to_file(self, file_name, file_content, overwrite):

		# overwrite = self.overwrite
		file_name = str(file_name)

		# If the File exists and the overwrite is False
		# Append the time stamp to the file name and save it.
		if os.path.exists(file_name + ".pdf") and not overwrite:

			# Get the current date and time
			now = datetime.now()
			print("The format of the time stamp is DD MM YYY HH MM SS")
			current_time = now.strftime("%d_%m_%Y_%H_%M_%f")

			# Append the current time stamp to the file name and save it.
			file_name = file_name + current_time + ".pdf"
			output_file = open(file_name, "wb")
			file_content.write(output_file)
			return True

		# If the file name exists and the overwrite is False
		# Then delete the exisiting file and create a new file
		elif os.path.exists(file_name + ".pdf") and overwrite:

			# Remove the exisiting file and sleep for 1 sec before saving the file.
			os.remove(file_name + ".pdf")
			time.sleep(1)

			output_file = open(file_name + ".pdf", "wb")
			file_content.write(output_file)
			return True

		else:
			# Write the output content to the file and save it.
			output_file = open(file_name + ".pdf", "wb")
			file_content.write(output_file)
			return True


	def rotate_entire_file(self,orientation,degree):

		# Copy the input file path to a local variable infile
		infile = self.infile
		fname = os.path.splitext(os.path.basename(infile))[0] +  '_' + str(degree) + '_' +orientation

		# Get the Output File directory and frame the output file name
		outdir = self.output_dir
		output_file_name = Path(outdir, fname)

		overwrite = self.overwrite
		pdf_len = self.number_of_pages

		input_pdf = PdfFileReader(open(infile, "rb"))
		pdf_writer = PdfFileWriter()


		if (orientation == "Clockwise"):
			print("Started rotating the PDF pages Clockwise ")
			for pagenum in range(pdf_len):
				page = input_pdf.getPage(pagenum)
				page.rotateClockwise(degree)
				pdf_writer.addPage(page)

		else:
			print("Started rotating the PDF pages Anti-Clockwise ")
			for pagenum in range(pdf_len):
				page = input_pdf.getPage(pagenum)
				page.rotateCounterClockwise(degree)
				pdf_writer.addPage(page)

		# Write the output content to the file and save it
		res = self.write_to_file(output_file_name, pdf_writer,overwrite)

		if(res):
			print("Successfully rotated the entire PDF file")


	# Split the PDF file by page ranges
	def rotate_pages(self, orientation, degree, page_range):
		""" Take a pdf file and copy a range of pages into a new pdf file

		Args:
			input_file: The source PDF file
			page_range: A string containing a range of pages to copy: 1-3,4
			out_file: File name for the destination PDF
		"""

		# Get the input file and instantiate the PDF File Reader
		infile = self.infile
		input_pdf = PdfFileReader(open(infile, "rb"))

		# Get the Output File directory and frame the output file name
		outdir = self.output_dir
		fname = os.path.splitext(os.path.basename(infile))[0] +  '_' + str(degree) + '_' +orientation
		output_file_name = Path(outdir, fname)

		overwrite = self.overwrite
		# Instantiate the PDF File Writer
		output = PdfFileWriter()

		# https://stackoverflow.com/questions/5704931/parse-string-of-integer-sets-with-intervals-to-list
		page_ranges = (x.split("-") for x in page_range.split(","))
		range_list = [i for r in page_ranges for i in range(int(r[0]), int(r[-1]) + 1)]

		# Need to subtract 1 because pages are 0 indexed
		# For the Clockwise Orientation, go to the if block , else, take the else block
		if (orientation == "Clockwise"):

			for pagenum in range_list:

				try:
					page = input_pdf.getPage(pagenum - 1)
					page.rotateClockwise(degree)
					output.addPage(page)
				except IndexError:
					# Alert the user and stop adding pages
					app.infoBox("Info", "Range exceeded number of pages in input.\nFile will still be saved.")
					break
		else:

			for pagenum in range_list:

				try:
					page = input_pdf.getPage(pagenum - 1)
					page.rotateCounterClockwise(degree)
					output.addPage(page)
				except IndexError:
					# Alert the user and stop adding pages
					app.infoBox("Info", "Range exceeded number of pages in input.\nFile will still be saved.")
					break

		# Send the content and file name to write
		res = self.write_to_file(output_file_name,output, overwrite)
		if(res):
			print("Successfully rotated the pages of PDF file")




class PDF_Merging(PDF_Stuff):

	def __init__(self, infiles ,output_dir, overwrite):
		self.infiles = infiles
		self.output_dir = output_dir
		self.overwrite = overwrite

	def merge(self):

		overwrite = self.overwrite
		pdf_writer = PdfFileWriter()

		output_file = Path(self.output_dir, "Merged_PDF_")

		for path in self.infiles:
			pdf_reader = PdfFileReader(path)
			for page in range(pdf_reader.getNumPages()):
				pdf_writer.addPage(pdf_reader.getPage(page))

		res = PDF_Stuff.write_to_file(self, output_file, pdf_writer, overwrite )
		if(res):
			print("Successfully Merged")

		# with open(output_file, 'wb') as fh:
		# 	pdf_writer.write(fh)





# if __name__ == '__main__':
#
# 	# pdf_path = r"C:\PyCharm Community Edition 2019.1.3\Projects\PyPDF2\Pandas_Tidy_Data.pdf"
# 	pdf_path = r"C:\Harman\Sans\Temp\Docs\Neelima\Passport\Corrected_Passport.pdf"
#
# 	overwrite = False
# 	# Create an object
# 	itr = PDF_Stuff(pdf_path)
#
# 	# Get the PDF file meta data
# 	itr.getDocInfo()
#
# 	# Split the PDF file after the given "n" page number.
# 	# itr.split_after(15)
#
# 	# Split the PDF file at every given "n" pages
# 	# itr.split_at_every(2)
#
# 	# Rotate the pdf page by 180 clockwise
# 	itr.rotate(90,True,1)
#



