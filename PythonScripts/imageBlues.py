# A13
# Image Blues: program creates new image with a blue channel

import matplotlib.pyplot as plt

# Function to display an image and wait for user to close the window before proceeding
def show_and_wait(image):
    # Display the image
    plt.imshow(image)

    # Show the plot window without blocking script execution
    plt.show(block=False)

    # Wait for user to press Enter to continue
    input("Press Enter to continue...")

    # Close the plot window
    plt.close()


# Prompt user to enter input and output file names
userImg = input('Enter name of input file: ')               # imageAverages.png
userOutfile = input('Enter name of the output file: ')      # imageBlues.png

# Read the input image
img = plt.imread(userImg)

# Display the original image and wait for user input
show_and_wait(img)

# Create a copy of the original image with blue channel emphasized
img2 = img.copy()
img2[:, :, 1] = 0
img2[:, :, 0] = 0

# Display the modified image with emphasized blue channel and wait for user input
show_and_wait(img2)

# Save the modified image
plt.imsave(userOutfile, img2)
