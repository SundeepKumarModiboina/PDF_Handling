from PyPDF2 import PdfFileReader, PdfFileWriter
import os


class PDF_Stuff:

	def __init__(self, filepath):

		self.infile = filepath
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
				output_1_filename = '{}_page_{}.pdf'.format(fname, page + 1)

			# Write the file data to the output file
			self.write_to_file(output_1_filename, output_1)

			# Loop through the pages and add the page data to the output
			for page in range(page_num,pdf_len):

				# Get the data from the given page number
				page_data = input_pdf.getPage(page)

				# Add the page data to the pdf_writer
				output_2.addPage(page_data)

				# Frame the output file name
				output_2_filename = '{}_page_{}.pdf'.format(fname, page + 1)

			# Write the file data to the output file
			self.write_to_file(output_2_filename,output_2)


	# Method to split the pdf at every given n pages.
	def split_at_every(self,step = 1):

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
					output_1_filename = '{}_page_{}.pdf'.format(fname, page + 1)

				# Write the output content to the file and save it.
				self.write_to_file(output_1_filename, output_1)

			else:

				output_final = PdfFileWriter()
				output_final_filename = "Last_Pages"

				# Loop through the pdf pages starting from the value of current index till the last page of the pdf doc.
				# Ex : page numbers = [0,2,4,6,8]
				# If the current index is 8, loop from 8th page till the last page in the pdf doc.

				for page in range(page_numbers[ind], pdf_len):
					# Get the data from the given page number
					page_data = input_pdf.getPage(page)

					# Add the page data to the pdf_writer
					output_final.addPage(page_data)

					# Frame the output file name
					output_final_filename = '{}_page_{}.pdf'.format(fname, page + 1)

				# Write the output content to the file and save it.
				self.write_to_file(output_final_filename,output_final)


	# Method to write the content to the file
	def write_to_file(self, file_name, file_content):

		# Write the output content to the file and save it.
		output_file = open(file_name, "wb")
		file_content.write(output_file)


if __name__ == '__main__':

	pdf_path = r"C:\PyCharm Community Edition 2019.1.3\Projects\PyPDF2\Pandas_Tidy_Data.pdf"

	# Create an object
	itr = PDF_Stuff(pdf_path)

	# Get the PDF file meta data
	itr.getDocInfo()

	# Split the PDF file after the given "n" page number.
	itr.split_after(15)

	# Split the PDF file at every given "n" pages
	# itr.split_at_every(2)




