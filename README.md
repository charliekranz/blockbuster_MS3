
<img src="https://blockbuster-charliekranz.herokuapp.com/static/MS3-project-files/home.jpg">

# Block+Buster+Builder

Block+Buster+Builder seeks to give you all the fun of being a Movie Mogul with none of the hassle, legal costs or need for negotiations. Simply Build your Story using the Block+Buster Building Blocks, Title the Project, declare your Genre and then Cast your Masterpiece with some of the best talent in the business!
And if you get writer's block - simply  Randomize your Story Choices!

***

## UX (User Experience)

### User Stories
- #### First Time Visitor Goals
    1. As a First Time Visitor, I want to clearly understand the features and functionality of the website.
    2. As a First Time Visitor, I want to be able to quickly view Block+Buster and About content.
    3. As a First Time Visitor, I want to be able to easily register, login and logout.
    4. As a First Time Visitor, I want to be able to easily create, filter and edit my own Block+Buster Content.
    5. As a First Time Visitor, I want to be able to search Block+Buster content by Title, Story or Cast.

 - #### Returning Visitor Goals
    1. As a Returning Visitor, I want to be able to add, edit and delete Block+Buster Conent.
    2. As a Returning Visitor, I want to be able to search others' Block+Buster Conent.


- #### Frequent User Goals
    1. As a Frequent User, I want to be able to refer others to the website and encourage them to create Block+Busters.

static/MS3-project-files/MS3-wirefarmes-CharlieKranz-Block+Buster.pdf

## Design

- ### Branding 
    - The Block+Buster+Builder brand is an alliterative phrasing that has the dual purpose of evoking succesful films (Blockbusters) as well as the compartmentalized "block" construction which makes up the experience.
    - Clear iconography for all features and functions
    - Further "B" alliteration with the Build and Browse features

- ### Colours
    - Using a very simple, though unusual, Purple schematic
    - Additional colour variations to highlight functions: Delete (red) and Cancel (Gray)

- ### UI
    - Clean, simple UI
    - Larger screens allow for some 2 column layouts
    - Smaller screens use 1-column layout throughout and some font-size reduction

- #### Typography
    - Anton font formore compressed Block+Buster+Builder branded text
    - PT Mono monospace font for some featured text sections - to evoke the typewriter feel of a screenplay writer
    - Sans Serif for body and smaller text


## Features

### Existing Features

- __Brand and Navigation Bar__

  - The brand and navigation bar displays the site name and gives users the ability to navigate throughout the site
  - The navigation bar displays navigation options based on the uswers's current state 
    - Logged-in Users will see the Build and Logout Options (Login and Register options will be hidden)
    - Logged-out Users will see the Login and Register options (Logout and Build will be hidden)


- __Home Page__

  - TBC 
  - TBC 


- __Browse Page__

  - TBC 
  - TBC  


- __MyBB Page__

  - TBC 
  - TBC  


- __Build Page__

  - TBC 
  - TBC  

<img src="https://blockbuster-charliekranz.herokuapp.com/static/MS3-project-files/build.jpg">


- __Edit Page__

  - TBC 
  - TBC 


- __Login Page__

  - TBC 
  - TBC  


- __Logout Page__

  - TBC 
  - TBC  


- __Register Page__

  - TBC 
  - TBC  


- __About Page__

  - TBC 
  - TBC  


- __Modals__

    -

- __Footer__

  - TBC 
  - TBC 


### Features Left to Implement

- Allow users to recover password
- Paginate - would like to Paginate every 30 Blockbusters
- Re-index db to include username which would allow users to search by usernames
- Username search functionality would also allow me to use Jinga templating to give users a "Share your BBs" link atop MyBB page
- My friend Ronan mentioned a Python library that allows for pluralisation of text, which I'd like to invstigate. Failing that some more complex programming to use appropriate singular and/or plural string for story sections.
- Possibly add option for people to suggest Block+Buster story content, movies to use as inspiration or new actors to cast section
- An age-range sort function for actors
- Twitter and Facebook share options (possibly)
- Would like to add a disclaimer about removing old BB content occassionally
- Might allow for longer titles and force linebreak/wrap if no space before end of BB accordion


## Technologies used 

* HTML and CSS programming languages
* [Balsamiq](https://balsamiq.com/) - wireframing tool
* [Slack](https://slack.com/) - networking and communications
* [GitHub](https://github.com/) - code repository
* [GitPod](https://www.gitpod.io/) - cloud dev environment
* [Bootstrap](https://getbootstrap.com/) - responsive sourcetoolkit with components and Javascipt plugins
* [fontawesome](https://fontawesome.com/v4.7.0/) - vector icons customisable through CSS
* [Google Fonts](https://fonts.google.com/) - open source web font collection
* [jQuery](https://jquery.com/) - add state to button
* [MongoDB](https://www.mongodb.com/) - database and collections
* [Heroku](https://dashboard.heroku.com/apps) - Cloud Applications
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - web application library
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - templating engine

## Testing 


- Navbar
    - Tested that navigation links linked to appropriate pages
    - Tested that nav links which should be visible were visible based on user session state
    - Tested that nav links which should be hidden were hidden based on user session state

- Homepage
    - Tested that buttons which should be visible were visible based on user session state
    - Tested that buttons which should be hidden were hidden based on user session state

- Register
    - Tested that Registrations were confined to the appropriate restrictions
    - Those restrictions being alpha/numeric characers only, and following the min-max count 

- Login 
    - Tested that Login always functioned properly, allowing only valid logins

- Logout 
    - Tested that logout always successfully logged-out users

- Build
    - Tested that all appropriate restrictions were enforced, namely
        - Stories must have all 4 parts selected
        - Randomization worked across all 4 story parts
        - Titles had to be eneterd with strict min/max values
        - A Genre had to be explicitly chosen
        - Cast had to have at least one person and no more than 3
    - If any of the above conditions were not met, tested that the approprite prompt appeared
        - Prompts included Modals for Min/Max cast
    - Tested that Publish button did correctly save to database

- Edit 
    - Tested that all the same Build functions were present as well as:
        - Cancel to reload the Blockbusters page
        - Update to save changes to database
        - Delete did delete Blockbuster with the defensive Modal to check before deleting

- Browse
    - Tested that Blockbusters from database did populate the Browse page
    - Tested that Blockbusters did appear in accordion card when clicked
    - Tested Search function for all indexes

- MyBB 
    - Tested that all user's own BlockBusters (and only theirs) were displayed

- About 
    - Tested that links to amazon.co.uk worked 
     

## TESTED on the Following:
    * Responsive devices on Google Developer Tools
    * iPhone 7, iPad Pro
    * OSX Browsers: Chrome, Safari


### Validator Testing

- HTML
  - No fatal errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fblockbuster-charliekranz.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JS 
   - JS validated but flags undefined and unused variables. All variables are defined and used so have ignored [https://jshint.com/](https://jshint.com/)
- Python
   - App.py is PEP8 compliant [Pep8 online](http://pep8online.com/)


## Debugging

- Accordion on blockbusters page were initially unable to target stories properly. Titles with spaces and/or a number at the start of title_name caused issues. Fixed by using ObjectId instead and adding a character to the start (BB).

- The selected casts weren't appearing as selected in the edit template. Using cast-checkbox class on edit template so that the selected cast appear chosen (thanks to Ronan for spotting that in particular)

- Edit template Updates were not sending cast selection changes. Changed Edit App Route from "cast_members": request.form.getlist("cast_members") to "cast_members": cast_members as request.form did not apply in this case. (Thanks to Ronan for spotting this)

- Caught missing else condition in edit_story.html which as preventing the Genre selection from properly displaying on edit.

### Unfixed Bugs 

- Register function delays after username chosen before password field can be accessed when using Safari for iOS

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

### Instructions
1. Save a copy of the github repository located at https://github.com/charliekranz/blockbuster_MS3 by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/charliekranz/blockbuster_MS3
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `block_buster`, with 10 collections called `cast` `character` `genres` `plot` `resolution` `setting` `stories` `storyblocks` `titles` and `users`. You will find example json structures for these collections in the [schemas](familyhubapp/data/schemas) folder.

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000`

## Heroku Deployment

To deploy Block+Buster+Builder to Heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.



## Credits 

### Content 

- This project was based on the TaskMaster Project from Code Institute Course
- Deployment steps taken (and modified) from AJGreaves Heroku Deployment Github Project (https://github.com/AJGreaves/familyhub/blob/master/README.md#heroku-deployment)
- Icons used throughout the website are from [Font Awesome](https://fontawesome.com/)
- Basic Randomize code (with some of own additional tweaks) - https://jsfiddle.net/aqpwcoju/1/
- RandomKeygen was used for random passwords https://randomkeygen.com/
- Getlist fix (partial ) found at https://stackoverflow.com/questions/53344797/how-create-an-array-with-checkboxes-in-flask


### Media

Charlize Theron  - https://en.wikipedia.org/wiki/Charlize_Theron#/media/File:Charlize-theron-IMG_6045.jpg
Judi Dench - https://en.wikipedia.org/wiki/Judi_Dench#/media/File:Judi_Dench_at_the_BAFTAs_2007_(cropped).jpg
Tilda Swinton - https://en.wikipedia.org/wiki/Tilda_Swinton#/media/File:Tilda_Swinton_by_Gage_Skidmore_(cropped).jpg
Sandrah Oh - https://m.media-amazon.com/images/M/MV5BMTMyNzYyNDE4MV5BMl5BanBnXkFtZTcwOTkxMDQ2NA@@._V1_.jpg

Dwayne - Johnson - <a href="https://en.wikipedia.org/wiki/Dwayne_Johnson#/media/File:Dwayne_Johnson_Hercules_2014_(cropped).jpg target="_blank">
Jackie Chan - <a href="https://upload.wikimedia.org/wikipedia/commons/8/8b/Jackie_Chan_July_2016.jpg target="_blank">
Will Smith - <a href="https://en.wikipedia.org/wiki/Will_Smith#/media/File:TechCrunch_Disrupt_2019_(48834434641)_(cropped).jpg target="_blank">
Lin-Manuel Miranda - <a href="https://en.wikipedia.org/wiki/Lin-Manuel_Miranda#/media/File:Lin-Manuel_Miranda_by_Gage_Skidmore.jpg target="_blank">
Samuel L. Jackson - <a href="https://en.wikipedia.org/wiki/Samuel_L._Jackson#/media/File:Samuel_L._Jackson_2019_by_Glenn_Francis.jpg target="_blank">
Viola Davis - <a href="https://en.wikipedia.org/wiki/Viola_Davis#/media/File:Viola_Davis_by_Gage_Skidmore.jpg target="_blank">
Meryl Streep - <a href="https://en.wikipedia.org/wiki/Meryl_Streep#/media/File:Meryl_Streep_December_2018.jpg target="_blank">
Melissa McCarthy - <a href="https://en.wikipedia.org/wiki/Melissa_McCarthy#/media/File:Melissa_McCarthy_in_2018_(cropped).jpg target="_blank">
Elliot Page - <a href="https://media.vanityfair.com/photos/60884831301e0fee4a0c978d/master/w_2560%2Cc_limit/elliot-page-interview-lede.jpg target="_blank">
Denzel Washington - <a href="https://www.thextraordinary.org/media/k2/items/cache/2e2c1711fe12b24ae23d95c35bfd21c2_L.jpg target="_blank">
Leonardo DiCaprio - <a href="https://media.vanityfair.com/photos/60255707b9f9b86e12a6600a/2:3/w_2185,h_3278,c_limit/1205143953" target="_blank">
Amy Adams - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Amy_Adams_UK_Nocturnal_Animals_Premiere_%28cropped%29.jpg/440px-Amy_Adams_UK_Nocturnal_Animals_Premiere_%28cropped%29.jpg target="_blank">
Joaquin Phoenix - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Joaquin_Phoenix_at_the_2018_Berlin_Film_Festival.jpg/440px-Joaquin_Phoenix_at_the_2018_Berlin_Film_Festival.jpg target="_blank">
Ryan Gosling - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Ryan_Gosling_in_2018.jpg/440px-Ryan_Gosling_in_2018.jpg
Emma Stone - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Emma_Stone_at_the_39th_Mill_Valley_Film_Festival_%28cropped%29.jpg/440px-Emma_Stone_at_the_39th_Mill_Valley_Film_Festival_%28cropped%29.jpg
Saoirse Ronan - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Saoirse_Ronan_at_BAFTA_2016_%281%29_%28cropped%29.jpg/440px-Saoirse_Ronan_at_BAFTA_2016_%281%29_%28cropped%29.jpg target="_blank">
Idris Elba - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Idris_Elba-4580_%28cropped%29.jpg/440px-Idris_Elba-4580_%28cropped%29.jpg target="_blank">
Michael B. Jordan - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/2018-05-12-_Cannes-L%27acteur_Michael_B._Jordan-2721_%2842075892224%29.jpg/440px-2018-05-12-_Cannes-L%27acteur_Michael_B._Jordan-2721_%2842075892224%29.jpg target="_blank">
Ralph Fiennes - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Ralph_Fiennes_from_%22The_White_Crow%22_at_Opening_Ceremony_of_the_Tokyo_International_Film_Festival_2018_%2831747095048%29.jpg/440px-Ralph_Fiennes_from_%22The_White_Crow%22_at_Opening_Ceremony_of_the_Tokyo_International_Film_Festival_2018_%2831747095048%29.jpg target="_blank">
Margot Robbie - <a href="https://upload.wikimedia.org/wikipedia/commons/5/57/SYDNEY%2C_AUSTRALIA_-_JANUARY_23_Margot_Robbie_arrives_at_the_Australian_Premiere_of_%27I%2C_Tonya%27_on_January_23%2C_2018_in_Sydney%2C_Australia_%2828074883999%29_%28cropped_2%29.jpg target="_blank">
Letitia Wright - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Letitia_Wright_by_Gage_Skidmore.jpg/ target="_blank">440px-Letitia_Wright_by_Gage_Skidmore.jpg target="_blank">
Peter Dinklage - <a href="https://media.newyorker.com/photos/5de59f9310863b0009e9d541/2:2/w_2178,h_2178,c_limit/Schulman-PeterDinklage.jpg target="_blank">
Catherine Keener - <a href="https://m.media-amazon.com/images/M/MV5BMjIwMzQ1Mzg1MF5BMl5BanBnXkFtZTcwNTE4MTU5MQ@@._V1_.jpg target="_blank">
Regina King - <a href="https://media.vanityfair.com/photos/5c61e52f50f462477e50ddb6/2:3/w_1332,h_1998,c_limit/t-regina-king-cover-oscar-issue.png target="_blank">
Steve Buscemi - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Steve_Buscemi_crop.jpg/440px-Steve_Buscemi_crop.jpg target="_blank">
Cate Blanchett - <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Cate_Blanchett_Cannes_2018_2_%28cropped%29.jpg/ 440px-Cate_Blanchett_Cannes_2018_2_%28cropped%29.jpg target="_blank">

