from PIL import Image
from glob import glob
from easygui import indexbox, fileopenbox, enterbox, msgbox
import sys

"""
To Do: 1. Removing wrongly selected Image file from list
       2. Select Multiple files
       3. Edge cases
"""



def show_image_list(images):
    """
    Displays selected Image files in order
    """
    image_list = []
    for image in images:
        name = image.split("\\")
        image_list.append(name[-1])
        
    num = 1
    msg = ""
    for i in range(len(image_list)):
        msg += str(num) + ". " + image_list[i] + "\n"
        num += 1
    msgbox(msg, "Selected JPGs")

def main():
    image_list = [] #list to hold image file paths
    while 1:
        """
        Creating outline for GUI box
        """
        msg = "Select JPGs to convert to PDF \t\t\t\t\t\t\t "+ str(len(image_list)) + " selected"
        title = "JPG to PDF Converterer"
        choices = ["Select Images","Convert","Show Selected JPGs","EXIT"]
        choice = indexbox(msg,title,choices)
        
        if choice == 3:
            ## Exit when select exit button
            sys.exit()
            
        elif choice == 0:
            ## select image file
            image = fileopenbox() #filetypes="*.jpg", multiple=True)
            
            """
            check if file has .jpg extension
            if yes then append to the image list else re-selection option
            """
            if image.endswith('.jpg'):
                image_list.append(image) 
            else:
                msgbox("Selected File not PDF")
            
        elif choice == 1:
            flag = 0 ## check flag for success or not 

            if len(image_list) == 0: ## check if there is file selected or not
                msgbox("No Image file selected")
            else:
                filename = enterbox("Enter Output File Name") ## Filename for output PDF file
            
            if len(image_list) == 1:
                ## if only one image then open it, convert to RGB then save it as PDF
                Image.open(image_list[0]).convert('RGB').save(filename + ".pdf")
                flag = 1

            elif len(image_list) > 1:
                converted_image_list = [] ## list to hold converted images to rgb

                ## loop over all image files, convert and append to list
                for image in image_list:
                    converted_image_list.append(Image.open(image).convert('RGB'))
                
                ## get first image for the saving method
                img0 = converted_image_list[0]

                ## remove the first element from the list
                converted_image_list.pop(0)

                ## save the first image and append other images to it
                img0.save(filename + ".pdf", save_all=True, append_images=converted_image_list)

                flag = 1
            
            if flag == 1:    
                msgbox("Converted JPGs to PDF")
                sys.exit(0)


        elif choice == 2:
            if len(image_list) < 1:
                msgbox("No Files Selected", "Selected JPGs")
            else:    
                show_image_list(images = image_list)


if __name__ == "__main__":
	# calling the main function
	main()



