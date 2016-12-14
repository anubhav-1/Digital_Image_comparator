# Digital_Image_comparator

Our software is a Digital Image Comparator, which when given one image, can find out the image closest to it from a database.
This software is made for Debian based Linux Systems.
All image are manually added to the 'image_database' folder which will be successfully copied to the /home directory.

Just run the install.sh shell script and let the software set up everything for you.
Once done, you can add images to the database and search for the closest match of a test image of your choice.

Discalimer: This software uses probability based algorithm to find the closest image. In case there is no logically closest image, it would still output an image which it find to be the one with closest resemblance.
