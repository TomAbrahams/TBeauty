# TBeauty

Instead of tackling what is universal beauty, we propose to attempt to create profiles based on training data for individual understanding of beauty, while maintaining efficiency.
This paper describes a fully-functional software system that creates an individual machine learning algorithm based off a profile to allow users to get an accurate assessment of what they would classify and score beauty. The system would take data and use facial landmarks in order to assess this. The system can be changed to allow automatic search of new images to proactively select the ones that have high scores for any individual user. The project uses an existing 68-point landmark detection algorithm proposed by Rainer Lienhard to identify the facial landmark points (a so called facial mask) from images that will be feed into various machine learning algorithms.


# Easiest Method (Recommended)
A pre made VM for virtual box with all items ready to go!
https://drive.google.com/file/d/1nR-2ziV7M5Gc6fhIDjlM8uRvutPK87ls/view?usp=sharing

Inside the VM is an image that shows what needs to be done.
1. Login to the VM with username being student, and password being student 
2.Open Two Terminals
3. Instructions for Terminal 1 and type the following
  3a. cd
  3b. cd TBeauty/beyond
  3c. source envname/bin/activate
  3d. cd tryingflask/
  3e. python routes.py
4. Instructions for Terminal 2 and type the following
  4a. cd
  4b. cd TBeauty/beyond
  4c. source envname/bin/activate
  4d. cd dlibtesting
  4e. python servArrayThread.py
5.Open the Mozilla Firefox and type in the following address 127.0.0.1:5000
6. Click on Train Algorithm
7. And enter an email, and score the pictures with 1 being least beautiful and 5 being most.

# Advanced Method
The user manual to install the pre-reqs, with a step by step guide.
https://docs.google.com/document/d/15VIUz23H1cENw7gDKFNauCM-lxr3O0vhaYWUwwmVqUA/edit?usp=sharing
