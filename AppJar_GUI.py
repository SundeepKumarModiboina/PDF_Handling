from appJar import gui
from pathlib import Path
from PDF_Handling import PDF_Stuff
from PDF_Handling import PDF_Merging
import os


# To validate the inputs
def validate_inputs(input_file, output_dir, page_nums = None):
    """ Verify that the input values provided by the user are valid

    Args:
        input_file: The source PDF file
        output_dir: Directory to store the completed file
        page_nums: File A string containing a page_nums of pages to copy: 1-3,4
        file_name: Output name for the resulting PDF

    Returns:
        True if error and False otherwise
        List of error messages
    """
    errors = False
    error_msgs = []

    # Make sure a PDF is selected
    if Path(input_file).suffix.upper() != ".PDF":
        errors = True
        error_msgs.append("Please select a PDF input file")

    # Make sure a page_nums is selected
    # if page_nums < 1:
    #     errors = True
    #     error_msgs.append("Please enter a valid page page_nums")

    # Check for a valid directory
    if not(Path(output_dir)).exists():
        errors = True
        error_msgs.append("Please Select a valid output directory")

    # # Check for a file name
    # if len(file_name) < 1:
    #     errors = True
    #     error_msgs.append("Please enter a file name")

    return(errors, error_msgs)


# To handle the Split button press
def split_button_press(button):

	global app

	src_file = app.getEntry("Input_File")
	dest_dir = app.getEntry("Output_Directory")
	# out_file = app.getEntry("Output_name")

	split_type = app.getRadioButton("SplitType")
	page_range = app.getEntry(split_type)

	errors, error_msg = validate_inputs(src_file, dest_dir, page_range)
	if errors:
		app.errorBox("Error", "\n".join(error_msg), parent=None)

	else:
		# split_pages(src_file, page_range, Path(dest_dir, out_file))

		if button == "Split":

			print("Started the Splitting of the PDF")

			# Get the overwrite Check box value
			overwrite = app.getCheckBox("Overwrite")

			# Instantite the PDF_Stuff object with the destination directory and overwrite value
			obj = PDF_Stuff(src_file,dest_dir, overwrite)

			# Get the Split Type
			split_type = app.getRadioButton("SplitType")

			if( split_type == "Split After"):
				obj.split_after(page_range)

			elif( split_type == "Split at Every \"n\" pages"):
				# page_number  = app.getEntry("SplitEvery_Page")
				obj.split_at_every(page_range)

			elif( split_type == "Split By Page Ranges : 1,3,4-10"):
				# page_number  = app.getEntry("SplitRange_Page")
				obj.split_pages(page_range)
				pass

			else:
				pass
		else:
			app.stop()


# Entry fields to take the file paths
def split_file_handling():

	global app
	#  Frame for Handling the Files
	app.startLabelFrame("File Handling")
	app.setSticky("ew")
	app.setFont(20)

	# Input PDF File
	app.addLabel("Choose Source PDF File")
	app.addFileEntry("Input_File", 0, 1)


	# Out Directory to save the ouput PDF files
	app.addLabel("Select Output Directory")
	app.addDirectoryEntry("Output_Directory", 1, 1)

	infile = app.getEntry("Input_File")
	# Get the complete file name along with its path and split the text to take only the first part.
	dirname = os.path.dirname(infile)
	app.setEntry("Output_Directory", dirname)

	app.addLabel("Overwrite the existing output files")
	app.addCheckBox("Overwrite",2,1)

	app.setEntry("Input_File",r"C:\PyCharm Community Edition 2019.1.3\Projects\PyPDF2\Pandas_Tidy_Data.pdf")
	app.setEntry("Output_Directory",r"C:\Users\sundeepkm\Desktop\temp")

	# # Output PDF File Name
	# app.addLabel("Output file name")
	# app.addEntry("Output_name", 2, 1)

	app.stopLabelFrame()


# GUI Method for adding different split types ( Split Type Radio Buttons )
def split_types_radio():

	global app

	#  Start the Splitting Types Frame
	app.startLabelFrame("Splitting Types")
	app.setSticky("ew")
	app.setFont(20)

	# Split After
	app.addRadioButton("SplitType", "Split After", 0, 0)
	app.addNumericEntry("Split After", 0, 1)
	# app.addNumericEntry("SplitAfter", 0, 1)

	# Split at every n page
	app.addRadioButton("SplitType", "Split at Every \"n\" pages", 1, 0)
	app.addNumericEntry("Split at Every \"n\" pages", 1, 1)
	# app.addNumericEntry("SplitEvery_Page", 1, 1)

	# Split by Page Ranges
	app.addRadioButton("SplitType", "Split By Page Ranges : 1,3,4-10", 2, 0)
	app.addEntry("Split By Page Ranges : 1,3,4-10", 2, 1)
	# app.addEntry("Split_Ranges", 2, 1)

	# Stop the Frame
	app.stopLabelFrame()


# To handle the Merge button press
def merge_button_press(button):

	global app

	files = ["Merge_File1","Merge_File2","Merge_File3","Merge_File4","Merge_File5"]
	src_files = []
	for file in files:
		if not app.getEntry(file) == "":
			src_files.append(app.getEntry(file))


	output_dir = app.getEntry("Output_Directory")
	# out_file = app.getEntry("Output_name")

	if(len(src_files) < 2):
		app.errorBox("Error", "".join("Please select atleast 2 PDF files"), parent=None)

	elif not (Path(output_dir)).exists():
		app.errorBox("Error", "".join("Please Select a valid output directory"), parent=None)

	else:
		# split_pages(src_file, page_range, Path(dest_dir, out_file))

		if button == "MERGE":

			print("Started the Merging of PDF Files")

			# Get the overwrite Check box value
			overwrite = app.getCheckBox("Overwrite")

			# Instantite the PDF_Stuff object with the destination directory and overwrite value
			obj = PDF_Merging(src_files, output_dir, overwrite)
			# Start the merging process
			obj.merge()

		else:
			app.stop()


# Entry fields to take the file paths for Merging
def Merge_file_handling():

	global app
	#  Frame for Handling the Files
	app.startLabelFrame("Merging the PDFs")
	app.setSticky("ew")
	# app.setFont(20)

	# Input PDF File
	app.addLabel("Input File 1 for Merging")
	app.addFileEntry("Merge_File1", 0, 1)

	app.addLabel("Input File 2 for Merging")
	app.addFileEntry("Merge_File2", 1, 1)

	app.addLabel("Input File 3 for Merging")
	app.addFileEntry("Merge_File3", 2, 1)

	app.addLabel("Input File 4 for Merging")
	app.addFileEntry("Merge_File4", 3, 1)

	app.addLabel("Input File 5 for Merging")
	app.addFileEntry("Merge_File5", 4, 1)

	app.addLabel("Overwrite the existing output file")
	app.addCheckBox("MergeOverwrite",5,1)

	# Out Directory to save the ouput PDF files
	app.addLabel("Merge Result Output Directory")
	app.addDirectoryEntry("Merge_OutDir",6,1)

	# app.setEntry("Merge_File1",r"C:\Users\sundeepkm\Desktop\temp\Pandas_Tidy_Data_Ranges_22_07_2019_14_01_668388.pdf")
	# app.setEntry("Merge_File2",r"C:\Users\sundeepkm\Desktop\temp\Pandas_Tidy_DataRanges22_07_2019_13_55_343386.pdf")
	# app.setEntry("Merge_OutDir",r"C:\Users\sundeepkm\Desktop\temp")

	app.stopLabelFrame()


# Entry fields to take the file for Rotating
def Rotate_handle_frames():

	global app
	#  Frame for Handling the Files
	app.startLabelFrame("Rotating the Pages of the PDF")
	app.setSticky("ew")
	# app.setFont(20)

	# Input PDF File
	app.addLabel("Input File for Rotating the Pages")
	app.addFileEntry("RotateInFile", 0, 1)

	# Out Directory to save the ouput PDF files
	app.addLabel("Output Directory for storing the Output")
	app.addDirectoryEntry("RotateOutFile",1,1)

	app.addLabel("Overwrite the existing output file, if present")
	app.addCheckBox("RotateOverwrite",2,1)


	app.setEntry("RotateInFile",r"C:\Harman\Sans\Python_Training\Classes\PyPDF2_Project\Page_Ranges.pdf")
	# app.setEntry("Merge_File2",r"C:\Users\sundeepkm\Desktop\temp\Pandas_Tidy_DataRanges22_07_2019_13_55_343386.pdf")
	app.setEntry("RotateOutFile",r"C:\Users\sundeepkm\Desktop\temp")

	app.stopLabelFrame()


# GUI Method for adding different split types ( Rotate Type Radio Buttons )
def rotate_types_radio():

	global app

	#  Start the Splitting Types Frame
	app.startLabelFrame("Rotating Types")
	# app.setLabelFrameFont(size=12, family="Verdana", underline=False, slant="roman")
	app.setSticky("ew")
	# app.setFont(20)

	# Rotate the Entire File
	app.addRadioButton("RotateType", "Rotate Entire File", 0, 0)

	# Rotate by Page Ranges
	app.addRadioButton("RotateType", "Rotate Specific Pages : 1,3,4-10", 1, 0)
	app.addEntry("Rotate_PageRanges", 1, 1)
	# app.addNumericEntry("SplitEvery_Page", 1, 1)

	app.addLabelOptionBox("Rotation Type", ["Clockwise", "Anti-Clockwise"], 2,0)
	app.addLabelOptionBox("Rotation Degree", [90,180,270,360], 2,1)


	app.getLabelWidget("Rotation Type").config(font="8")
	app.getLabelWidget("Rotation Degree").config(font="8")
	# Stop the Frame
	app.stopLabelFrame()


# To handle the Rotate button press
def rotate_button_press(button):

	global app

	src_file = app.getEntry("RotateInFile")
	dest_dir = app.getEntry("RotateOutFile")
	# out_file = app.getEntry("Output_name")

	rotate_type = app.getRadioButton("RotateType")
	if(rotate_type == "Rotate Entire File"):
		page_range = 10
	else:
		page_range = app.getEntry("Rotate_PageRanges")

	errors, error_msg = validate_inputs(src_file, dest_dir, page_range)
	if errors:
		app.errorBox("Error", "\n".join(error_msg), parent=None)

	else:
		# split_pages(src_file, page_range, Path(dest_dir, out_file))

		if button == "ROTATE":

			print("Started the Rotation of PDF file pages")

			# Get the overwrite Check box value
			overwrite = app.getCheckBox("RotateOverwrite")

			orientation = app.getOptionBox("Rotation Type")
			degree = int(app.getOptionBox("Rotation Degree"))

			print("Orientation : ", orientation)
			print("Degree : ", degree)


			# Instantite the PDF_Stuff object with the destination directory and overwrite value
			obj = PDF_Stuff(src_file,dest_dir, overwrite)

			if( rotate_type == "Rotate Entire File"):
				obj.rotate_entire_file(orientation,degree)
				pass

			elif( rotate_type == "Rotate Specific Pages : 1,3,4-10"):
				page_range  = app.getEntry("Rotate_PageRanges")
				obj.rotate_pages(orientation, degree, page_range)
				pass

			else:
				pass
		else:
			app.stop()


# To close the Application
def exit_app():

	global app

	app.stop()


def create_gui():

	global app
	# Create the GUI with Tabbed Interface
	# app = gui("PDF Splitter", useTtk=True)
	app.setTtkTheme("vista")
	app.setSize(1000, 500)
	app.startTabbedFrame("TabbedFrame")
	app.setTabbedFrameTabExpand("TabbedFrame", expand=True)
	# app.setTabbedFrameActiveBg("TabbedFrame", "red")

	# Tab for Splitting the PDF file
	app.startTab("SPLIT")
	split_file_handling()
	split_types_radio()
	app.addButtons(["Split", "Cancel"], split_button_press)
	app.stopTab()


	# Tab for Merging the PDF files
	app.startTab("MERGE")
	Merge_file_handling()
	app.addButton("MERGE", merge_button_press,5,0)
	app.addNamedButton("CANCEL", "STOP", exit_app,5,1)
	app.stopTab()

	# Tab for ROTATING the PDF files
	app.startTab("ROTATE")
	Rotate_handle_frames()
	rotate_types_radio()
	app.addButton("ROTATE", rotate_button_press,5,0)
	app.addNamedButton("CANCEL", "STOP1", exit_app,5,1)
	app.stopTab()

	# Tab for WATER MARK the PDF files
	# app.startTab("WATER MARK")
	# app.addButton("WATER MARK", None)
	# app.addNamedButton("CANCEL", "STOP2", exit_app)
	# app.stopTab()

	app.stopTabbedFrame()
	app.go()




if __name__ == "__main__":
	# Create the GUI with Tabbed Interface
	app = gui("PDF HANDLER", useTtk=True)
	create_gui()