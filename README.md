# PDF_Handling
Split, Merge and Rotate the PDF

## 1. SPLITTING THE PDF
       Currently, three ways of splitting the PDF file has been implemented.

### a. Splitting the PDF file after the given "n" page number
       Ex : If the input PDF file has 10 pages and if the given page number is 5, the Split after given page number 
            makes a split after the 5th page and creates two PDF files.
            The first PDF file contains the pages from the 1st page to 5th page.
            The second PDF file contains the pages from 6th page to the last page.
            
### b. Splitting at every nth page.

        Ex 1: In a PDF file of 10 pages, if given nth page is 2, then splitting happens for every 2 pages.
              So, 5 files will be created, 1st file has 1-2 pages, 2nd file has 3-4 pages, 3rd file has 5-6 pages,
              4th file has 7-8 pages and 5th file has 9-10 pages
             
        Ex 2: In a PDF file of 10 pages, if the given nth page is 3, then splitting happens for every 3 pages.
              Here 4 files are created, 1st file has 1-3 pages, 2nd file has 4-6 pages, 3rd file has 7-9 pages and the
              4th file will have the 10th page.
              
### c. Splitting at the given page ranges.

        Ex 1: In a PDF file of 10 pages, if the page range is given as 1,3,5-8, then pages 1, 3, 5, 6, 7 and 8 are extracted
        into a single output file.
        
## 2. MERGING the PDF's
    
        The provision of inputting 5 PDF files is given but atleast 2 PDF files must be given for Merging. 
        It merges the complete file one after the other.
        
## 3. ROTATING THE PDF PAGES
    
        For rotating the PDF file, the user has to input the Orientation of
        the rotation ( Clockwise or Anti-Clockwise ) and Degree of Rotation ( 90 / 180 / 270 / 360 ).
        Two ways of rotating the PDF pages has been implemented.
        
### a. Rotating the entire file at the given page ranges.        
        
        The entire PDF file will be rotated as per the user provided Orientation and Degree of Rotation and the resulatant output
        file will be saved at the user given location.
        
### b. Rotating the given page ranges of a file.

        The user provided page ranges of a PDF file will be rotated as per the user provided Orientation and 
        Degree of Rotation and the resulatant output file will be saved at the user given location.
        
        Ex 1: In a PDF file of 10 pages, if the page range is given as 1,3,5-8, then pages 1, 3, 5, 6, 7 and 8 are extracted
         and then rotated as per the user given inputs and the resultant output file will be saved at the given location.


