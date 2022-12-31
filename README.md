**User Manual**

This user manual will provide an overview of the features and functionality of the MemoryBox application.

**Home page:** The home page is the default page when you open the application using the deployed application link. Home page includes the blogposts of all users and links to the main sections of the application such as Register, Login, Logout, Profile, My Posts, Friend Posts, Users, Post Entry and Search. If the user is not logged in, he will only be able to access the posts on home page, register page, and login page. If the user is logged in, he will also be able to access the My Posts, Friend Posts, Users, Post Entry and Search functionalities.

**Register page:** To create an account on the MemoryBox application, click on the "Register" link on the top right part of the home page. You will be directed to the register page, where you will need to enter your username, email address, first name, last name, password and password confirmation information. All the fields are mandatory and after entering all the information you can easily register by clicking the "Sign Up" button to complete the process.

**Login page:** To log in to the MemoryBox application, click on the "Login" link on the home page and enter your username and password. If you do not have a username then you may click the “Register” link as a shortcut that appears next to the “Need An Account” text below the “Login” button. After successfully providing the username and password credentials you will be logged in and will be able to view the “Friend Posts” section of the application. This redirection has been done in purpose for the user to be able to view related content from related users and not all the posts of all other users.

**Logout link:** You may use this link when you want to log-out of the application, after clicking the link you will see the “You have logged out” message.

**Profile page:** To view and update your personal information, click on the "My Profile" link on the home page, this page is only visible for logged in users. The profile page includes your username, first name, last name, e-mail address, last login time and profile picture. You can update your e-mail address, first name, last name and profile picture information by changing the information you need to change and clicking “Update Profile” button on the bottom of the page.

**Create blogpost:** To create a new blogpost, click on the "Post Entry" link on the home page. You will be directed to a form page where you can enter Title, Content, Link and Tags information and create a post by clicking the “Post” button. Tag information is not mandatory, however if you need to enter more than one tag, then you need to separate the tags by using comma as the delimiter.

**Search blogposts:** To search for blogposts on specific topics, you can use the search bar on the home page. Enter the keyword you want to search for and click the "search" button to view related posts about your keyword. The search has been done on both title and content information of the blogposts.

**Tag filtering:** You can create a blogpost with the tags you want the post to be associated with. You can view the tags of the blogposts with the blue colored tags next to the Link information of a post. If you want to filter all the related posts about that tag category you can do this by just clicking on the tag. For example, you can see all the “Messi” tagged items by clicking the “Messi” link on a post that has the tag “Messi”.

**Users page:** To view other users and to manage the following/unfollowing tasks about that users, you may click on the "Users" link on the home page. You will be able to view a list of users and their username, first and last names. When you click on the Detail button of a user, you may follow or unfollow that user depending on your connection and see the e-mail and last active date of that user in addition to the username and name information.

**Friend Posts page:** To view the posts of the users that you followed earlier you can access the “Friend Posts” link from the navigation bar. The users are also redirected to this page after their login is completed successfully. If you unfollow an other user you will not be able to view the posts of that user in this page.

**My Posts page:** To view your own posts that you created earlier you can use this page by clicking the “My Posts” link on the navigation bar or “My Own Posts” link on the right part of the web page. You can also update or delete your own posts by clicking on a post title where you will be redirected to the post detail page. 

**Comments:** You can add comments on the blogposts just by using the “Add Comment” button on the detail page of a blogposts. The detail pages are always accessible just by clicking on the title of a post.


---------------
You can access the deployed application here. http://54.89.208.162:8000
---------------
**System  Manual**

**Dockerisation in Local Environment**

If you want to dockerise and run the application in your local environment you should follow the below steps.
1.	In order to build the application you first need to install Docker on your machine. You can use the link below to install Docker Desktop, it has been mentioned that it is the easisest and recommended way of installing Docker Compose. Docker Desktop also includes Docker Engine and CLI which are the prerequisites of Compose.
Docker Compose Link: https://docs.docker.com/compose/install/
2.	To get started, you need to copy the folders of the application to your local environment.
 3.	Navigate to the root directory using command line and run the command  “docker-compose build”. This will help you build the necessary Docker images for the application. All the requirements have been detailed in requirements.txt file so you will not need to do anything special to install the related requirements except dockerising the application.
 4.	Run the application using the command “docker-compose up”. The containers will be up and running after the process is completed and the web application will be ready afterwards. 
 5.	You will be able to access the application using the “localhost:8000” link and you can access this link also by clicking the link next to the web container in Docker Desktop.
-----------

**Local Environment Requirements**

If you want to use your local environment without docker, **Django**, **Python** and **MySQL** should be installed to view the website in the local environment.

**Starting the web server**

You need to be in the directory that contains the manage.py file and type "py manage.py runserver" to start the web server.

After that you will be using the http address given at the end of the below sentence.

  "Starting development server at http://127.0.0.1:8000/"

When you open the localhost address above ( http://127.0.0.1:8000/ in this example) you will be able to see the home page of the application.
After completing the register process you will be able to view the home page with your username and password.
