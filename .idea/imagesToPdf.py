from PIL import Image

def imagesToPdf(pictures, new_pdf):
    all_pics = [Image.open(pic) for pic in pictures]
    ready_pics = [pic.convert('RGB') for pic in all_pics]
    ready_pics[0].save(new_pdf, save_all = True, append_images = ready_pics[1:])

# Test code:
pics_list = [r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\violinPicture.jpg", r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\kitty.jpg"]
pdf_name = r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\newPdfFile.pdf"
imagesToPdf(pics_list, pdf_name)

print("Files have been converted to one PDF!")