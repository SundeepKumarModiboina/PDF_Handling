# PDF_Handling
Split, Merge, Add Watermark to the PDF

## Splitting the PDF
    Currently, two ways of splitting the PDF file has been implemented.

### 1. Splitting the PDF file after the given "n" page number
       Ex : If the input PDF file has 10 pages and if the given page number is 5, the Split after given page number 
            makes a split after the 5th page and creates two PDF files.
            The first PDF file contains the pages from the 1st page to 5th page.
            The second PDF file contains the pages from 6th page to the last page.
            
#### 2. Splitting at every nth page.

        Ex 1: In a PDF file of 10 pages, if given nth page is 2, then splitting happens for every 2 pages.
              So, 5 files will be created, 1st file has 1-2 pages, 2nd file has 3-4 pages, 3rd file has 5-6 pages,
              4th file has 7-8 pages and 5th file has 9-10 pages
             
        Ex 2: In a PDF file of 10 pages, if the given nth page is 3, then splitting happens for every 3 pages.
              Here 4 files are created, 1st file has 1-3 pages, 2nd file has 4-6 pages, 3rd file has 7-9 pages and the
              4th file will have the 10th page.
