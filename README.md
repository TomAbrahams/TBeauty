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

# References and work used.

Junying Gan, Lichen Li, & Yikui Zhai. (2014). Facial beauty prediction model based on self-taught learning and convolutional restricted Boltzmann machine. Machine Learning and Cybernetics (ICMLC), 2014 International Conference on, 2, 844-849.

Gan, Li, Zhai, & Liu. (2014). Deep self-taught learning for facial beauty prediction. Neurocomputing, 144, 295-303.

Rhodes, G. (2006). THE EVOLUTIONARY PSYCHOLOGY OF FACIAL BEAUTY. Annual Review of Psychology, 57, 199-226.

Kagian, Dror, Leyvand, Meilijson, Cohen-Or, & Ruppin. (2008). A machine learning predictor of facial attractiveness revealing human-like psychophysical biases. Vision Research, 48(2), 235-243.

Rainer Lienhart, haarcascade_frontalface_default.xml by Rainer Lienhart, 24x24 discrete,
 Imperial College London, predictor_68_face_landmarks.dat.bz2
"Facial landmarks with dlib, OpenCV, and python." , edited by Adrian Rosebrock, pyimagesearch, 3 Apr. 2017, www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/. Accessed 8 Nov. 2018.
Amaratunga, Thimira. "Extracting individual Facial Features from Dlib Face Landmarks." Codes of Interest: Extracting individual Facial Features from Dlib Face Landmarks, Codes of Interest, www.codesofinterest.com/2017/04/extracting-individual-facial-features-dlib.html. Accessed 10 Sept. 2018.
Women Teamwork Team Business, Pixabay, pixabay.com/en/women-teamwork-team-business-1209678/. Accessed 2018.
Women Girl Portrait Female Yong, Pixabay, https://pixabay.com/en/woman-girl-portrait-female-young-828610/. Accessed 2018.
Górecki, Jerzy. Girl Woman Portrait. . pixabay. pixabay.com/en/girl-woman-portrait-face-young-2215071/. Accessed 25 Nov. 2018.
Free Photo Face Woman Face Female Portrait woman. . Max Pixel. www.maxpixel.net/Face-Woman-Face-Female-Portrait-Woman-2159177. Accessed 25 Nov. 2018.
Woman Face. . Pixabay. www.pexels.com/photo/woman-face-157661/. Accessed 25 Nov. 2018.
Grayscale Photo of Woman in Black Scoop Neck Halter Dress. . Pixabay. www.pexels.com/photo/fashion-girl-women-model-60712/. Accessed 25 Nov. 2018.
Punk, Pablo. Woman in Brown Collard Shirt. . Pexels. www.pexels.com/photo/black-and-white-girl-portrait-beauty-108447/. Accessed 25 Nov. 2018.
Orbit Publishers. Woman Standing Near Orange Painted Wall. . Pexels. www.pexels.com/photo/woman-standing-near-orange-painted-wall-1152703/. Accessed 25 Nov. 2018.
Fillieul, Thierry. Woman in Red Tank Top. . Pexels. www.pexels.com/photo/woman-in-red-tank-top-638700/. Accessed 25 Nov. 2018.
Woman Face PNG image. . pngimg.com. pngimg.com/download/5646. Accessed 25 Nov. 2018.
Hoyer, Thea. Forest Dream Photo. . Unsplash. unsplash.com/photos/CrJyu9HoeBg. Accessed 25 Nov. 2018.
Belis, Tamara. Forest Dream Photo. . Unsplash. unsplash.com/photos/eDVQwVMLMgU. Accessed 25 Nov. 2018.
Zdrobău, Alexandru. Woman Behind Cherry Blossoms. . Unsplash. unsplash.com/photos/BGz8vO3pK8k. Accessed 25 Nov. 2018.
Whitson, Parker. HD Photo. . Unsplash. unsplash.com/photos/XTsnvYfzlTs. Accessed 25 Nov. 2018.
Collamer, Matt. Fairy Tale. . Unsplash. unsplash.com/photos/jJz7y8jOdB4. Accessed 25 Nov. 2018.
Nemati, Zohre. Beauty. . Unsplash. unsplash.com/photos/vMbUk7dWe9o. Accessed 25 Nov. 2018.
Tolokonov, Dmytro. Ethno. . Unsplash. unsplash.com/photos/W-6PUFGYtLc. Accessed 25 Nov. 2018.
Gray, Annie. Woman, Female, Lips and Blue HD. . Unsplash. unsplash.com/photos/f5nAQpPSFr0. Accessed 25 Nov. 2018.
Woodard, Averie. Reflection of a Female Music Fan. . Unsplash. unsplash.com/photos/th3rQu0K3aM. Accessed 25 Nov. 2018.
Woodard, Averie. Hair, Female, Woman, and Barbie HD. . Unsplash. unsplash.com/photos/4nulm-JUYFo. Accessed 25 Nov. 2018.
Cagle, Brooke. Woman, Female, Wood and Post HD. . Unsplash. unsplash.com/photos/1x2ja1HTe5g. Accessed 25 Nov. 2018.
Cagle, Brooke. HD photo. . Unsplash. unsplash.com/photos/8eMtf5_-m7I. Accessed 25 Nov. 2018.
Cagle, Brooke. Person, Woman, Engagement, and Wedding HD photo. . Unsplash. unsplash.com/photos/W7pk4FfrSY0. Accessed 25 Nov. 2018.
Gardner, Joe. Happy and Alone photo. . Unsplash. unsplash.com/photos/pAs4IM6OGWI. Accessed 25 Nov. 2018.
Gardner, Joe. Hat, Woman, Dress and Person HD Photo. . Unsplash. unsplash.com/photos/x2icoktCF20. Accessed 25 Nov. 2018.
Heffner, Tanja. Stood Up For a Date photo. . Unsplash. unsplash.com/photos/_3MT4pSthzE. Accessed 25 Nov. 2018.
Haddox, Ethan. Mock Magazine Cover Photo. . Unsplash. unsplash.com/photos/HkJM5g8IG3U. Accessed 25 Nov. 2018.
Magazine, Malvestida. Glitter Lips! . Unsplash. unsplash.com/photos/Z8hP6_fKO9U. Accessed 25 Nov. 2018.
Niparavičius, Rokas. Glodilocks. . Unsplash. unsplash.com/photos/r_lSD8eSV8g. Accessed 25 Nov. 2018.
Lexi, Christiansen. HD Photo. . Unsplash. unsplash.com/photos/AGHf5eY26Xg. Accessed 25 Nov. 2018.
Tamara, Bellis. HD Photo. . Unsplash. unsplash.com/photos/2Tv7-O13hgk. Accessed 25 Nov. 2018.
Heathcoat, Natalie. Me. photo. . Unsplash. unsplash.com/photos/QP1N1rK5QlA. Accessed 25 Nov. 2018.
Silvério, Gabriel. Nature is Beautiful Photo. . Unsplash. unsplash.com/photos/QJCtd5KGI9Y. Accessed 25 Nov. 2018.
Kirk, Sage. Freshlook 2018 Photo. . Unsplash. unsplash.com/photos/Wx2AjoLtpcU. Accessed 25 Nov. 2018.
Sessions, Morgan. Woman and Road Smoke Cloud Photo. . Unsplash. unsplash.com/photos/epRe09tKr_4. Accessed 25 Nov. 2018.
Rmah, Larm. Woman, Female, Shadow and Asian HD Photo. . Unsplash. unsplash.com/photos/GJnyw_HASdA. Accessed 25 Nov. 2018.
Nelson, Hannah. Woman Wearing Green and Black Top Standing Near White Wall Smiling in Front of Camera. . Pexels. www.pexels.com/photo/woman-wearing-green-and-black-top-standing-near-white-wall-smiling-in-front-of-camera-1086579/. Accessed 25 Nov. 2018.
Pixabay. Woman in Blond Hair. . Pexels. www.pexels.com/photo/attractive-beautiful-beauty-close-up-458718/. Accessed 25 Nov. 2018
2Happy. Just A Simple Russian Girl. . stockvault. www.stockvault.net/photo/121747/woman. Accessed 25 Nov. 2018.
Farve, Lucas. Sunrise_gr20_0. . unsplash. unsplash.com/photos/GzcI_rMNclY. Accessed 25 Nov. 2018.
Blackbird, Anter. Please Donate - Portrait of an Angel. . unsplash. unsplash.com/photos/TRGNLA5lfyQ. Accessed 25 Nov. 2018.
Stitt, William. Woman portrait. . unsplash. unsplash.com/photos/QdGlponzosk. Accessed 25 Nov. 2018.
Tasher, Aral. Young woman posing. . unsplash. unsplash.com/photos/RYCnmI4YfzY. Accessed 25 Nov. 2018.
Hashemirad, Bardia. Info. . unsplash. unsplash.com/photos/3P7jxpEgkC4. Accessed 25 Nov. 2018.
Sandh, Sandevil. Teen. . unsplash. unsplash.com/photos/rsEtPua0sgE. Accessed 25 Nov. 2018.
Arock, Chris. Long Forgotten. . unsplash. unsplash.com/photos/84uva6w9tyY. Accessed 25 Nov. 2018.
Loftus, Kal. Timberland 45th Anniversary. . unsplash. unsplash.com/photos/8Zv6hOS_STE. Accessed 25 Nov. 2018.
Martinez, Jose. Morning Breakfast Before the Morning Meeting. . unsplash. unsplash.com/photos/hsRBups9z9I. Accessed 25 Nov. 2018.
Lackmann, Eddy. Morning Breakfast Before the Morning Meeting. . unsplash. unsplash.com/photos/Q9uqrsQ1RjE. Accessed 25 Nov. 2018.
Loftus, Kal. Moody Evening. . unsplash. unsplash.com/photos/Q9uqrsQ1RjE. Accessed 25 Nov. 2018.
Loftus, Kal. Caught Up in the Moment. . unsplash. unsplash.com/photos/5LisWBFGKRc. Accessed 25 Nov. 2018.
Torsani, Derek. Caught Up in the Moment. . unsplash. unsplash.com/photos/4ng2Q432boo. Accessed 25 Nov. 2018.
Раскольников, Александр. Sister. . unsplash. unsplash.com/photos/4ng2Q432boo. Accessed 25 Nov. 2018.
Mabena, Nkululeko. Gogo Mabena. . unsplash. unsplash.com/photos/yrAJSeK-P4k. Accessed 25 Nov. 2018.
Ayme, Christopher. Angel Wings. . unsplash. unsplash.com/photos/_-cIF0UeMKk. Accessed 25 Nov. 2018.
Goodman, Autumn. Springtime Sweetness. . unsplash. unsplash.com/photos/0hZyqa7W5uI. Accessed 26 Nov. 2018.
Saavedra, Zulmaury. Face Girl. . unsplash. unsplash.com/photos/vh_pAs2FH_8. Accessed 26 Nov. 2018.
Lightscape. Gaze. . unsplash. unsplash.com/photos/NrfHclKeOOk. Accessed 26 Nov. 2018.
Henderson, Elijah M. Woman under “Nashville Music City” poster. . unsplash. unsplash.com/photos/khGqQIFS6VE. Accessed 26 Nov. 2018.
Smith, Timothy P. Music and Tattoos. . unsplash. unsplash.com/photos/60P1kPuRmjQ. Accessed 26 Nov. 2018.
Pietralunga, Davide. Music and Tattoos. . Eyes Speak. unsplash.com/photos/6DPiga695fg. Accessed 26 Nov. 2018.
Buscher, Noah. Cafe Gaze. . unsplash. unsplash.com/photos/AR7aumwKr2s. Accessed 26 Nov. 2018.
Romero, Raechel. Woman, Female, Sisters, and Friends. . unsplash. unsplash.com/photos/3W3wztKHwq8. Accessed 26 Nov. 2018.
Irene, Samantha. Woman, Female, Portrait, and Face HD. . unsplash. unsplash.com/photos/HJm_qOyCdLM. Accessed 26 Nov. 2018.
Catalog, Thought. Portrait of woman in spring/summer. . unsplash. unsplash.com/photos/1Nxq_3rp-PE. Accessed 26 Nov. 2018.
Perry, Sidney. Lost in Your Beauty. . unsplash. unsplash.com/photos/awatlXOqXCE. Accessed 26 Nov. 2018.
Afonso, Michael. Woman, Lady, Female, and Caucasian HD. . unsplash.  unsplash.com/photos/Z_bTArFy6ks. Accessed 2 Dec. 2018.
Crowe, Rachael. Floppy Hat and Plants Photo. . unsplash. unsplash.com/photos/tqar8J3fZ3o. Accessed 26 Nov. 2018.
Photo, Jose Ros. Blue Eyes ! . unsplash. unsplash.com/photos/wiXBJhMmcaM. Accessed 26 Nov. 2018.
Lucas, Caleb. Depth. . unsplash. unsplash.com/photos/2oLBwyl80QY. Accessed 26 Nov. 2018.
Annie, Spratt. Woman, Female, Smoke and Flare. . unsplash. unsplash.com/photos/DO9zk99PcUo. Accessed 26 Nov. 2018.
Walts, Savs. Aubs. . unsplash. unsplash.com/photos/P6GZCtjrX-c. Accessed 26 Nov. 2018.
Nix, Tyler. Portrait, Person, Woman, and Model. . unsplash. unsplash.com/photos/yrD-fArVNAo. Accessed 26 Nov. 2018.
Bana, Atikh. Woman, Female, Curl and Glamour. . unsplash. unsplash.com/photos/2c0midsQKe0. Accessed 26 Nov. 2018.
