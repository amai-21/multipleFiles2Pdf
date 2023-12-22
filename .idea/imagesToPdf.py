#future additions:
#-user input for specific images that are to be converted to pdf's.
#-add an images to jpg, png, and various other image extension files.
#

from PIL import Image

def imagesToPdf(pictures, new_pdf):
    all_pics = [Image.open(pic) for pic in pictures]
    ready_pics = [pic.convert('RGB') for pic in all_pics]
    ready_pics[0].save(new_pdf, save_all = True, append_images = ready_pics[1:])

# Test code:
#pics_list = [r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\violinPicture.jpg", r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\kitty.jpg"]
#pdf_name = r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\newPdfFile.pdf"

#temporary string for future Pdf file location.
stringVariable = "C:\\Users\\andre\\OneDrive\\Pictures\\Screenshots\\"

#pics_list = ["C:Users\\andre\\Pictures\\Screenshots\\"]

#take user input from both command line and prompt. (Note from December 18, 2023).

print("Enter file name:\n")
#input
stringInput = str(input())

#combine stringVariable and stringInput.
stringVariable = stringVariable + stringInput

#driver code for stringVariable:
#print(stringVariable) --It works!--

#store stringVariable into a list":
pics_list = [stringVariable]

#driver code for pics_list:
#print(pics_list) --It works!--




# this code doesn't work... pics_list2 = pics_list + string
#pics_list = [r"C:Users\andre\Pictures\Screenshots"]

#driver code:




pdf_name = "C:\\Users\\andre\\OneDrive\\Pictures\\Screenshots\\newPdfFile.pdf"
imagesToPdf(pics_list, pdf_name)
#output
print("File has been converted.")

#or by default
string_default = input()

#output
print("Nothing happened.")



#pics_list = [r"C:\Users\andre\Pictures\Screenshots\project5.pdf\project5pdfScreenshotYes.png"]


#pdf_name = r"C:\Users\andre\Pictures\Screenshots\project5.pdf\project5.pdf"
#imagesToPdf(pics_list, pdf_name)

#print("Files have been converted to one PDF!")