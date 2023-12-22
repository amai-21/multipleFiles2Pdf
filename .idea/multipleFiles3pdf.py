from PIL import Image

# Create a list of image paths
image_paths = ['doggie.jpg', 'kitty.jpg', 'piano.jpg']

# Open the first image and save it as a PDF.
pdf_path = 'output.pdf'
images = [Image.open(image_paths[0])]
images[0].save(pdf_path, save_all = True, append_images=[Image.open(path) for path in image_paths[1:]])

