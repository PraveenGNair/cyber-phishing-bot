# Cyber Phishing Bot using Machine Learning

### Steps for the project -
* Install all the required packages using the following command - ```pip install -r requirements.txt```.
Make sure your pip is consistent with the Python version you are using by typing ```pip -V```.

* Deploy the python flask App using heroku and update the app url link in ```popup.js``` file. Refer- https://stackabuse.com/deploying-a-flask-application-to-heroku/.
* (If you are using **anything other than** a Mac) Modify the localhost path in ```features_extraction.py``` to your localhost path (or host the application on a remote server and make the necessary changes). 
* Go to ```chrome://extensions```, activate developer mode, click on load unpacked and select the 'Extension' folder from our project.
* Now, you can go to any web page and click on the extension in the top right panel of your Chrome window. Click on the 'Safe of not?' button and wait for a second for the result.
* Done!

### Refer paper - http://ieeexplore.ieee.org/document/8256834/

#### Abstract -
* Our aim is to create an extension for Chrome which will act as middleware between the users and the malicious websites, and mitigate the risk of users succumbing to such websites.
* Further, all harmful content cannot be exhaustively collected as even that is bound to continuous development. To counter this we are using machine learning - to train the tool and categorize the new content it sees every time into the particular categories so that corresponding action can be taken.

A few snapshots of our system being run on a webpage -

![Google Safe](google.jpg)
_**Fig 1.** A safe website - www.google.com
