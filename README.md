# Pre-Owned

Pre-owned is a webstore that sells pre-owned clothes, weather you want to by clothes that have already been owned by someone else previously because it’s better for the environment or because you can find more original pieces of clothing this is the store for you. The project is created for educational purpose only.

## UX

### Strategy 

The purpose of the project is to create a website for people who wants to by good quality modern clothes but that have been owned previously owned by someone else making it more affordable that buying new clothes and better for the environment. The target audience are people who are interested in fashion but also are concerned about the sustainability of the fashion industry and wants to lower their negative impact on the environment by buying pre-owned clothes. 

### Scope

Site owner’s goal: To create a website where fashion interested people can by clothes that they like without having the same impact on the environment that new clothes and that are affordable. 

User’s goal: To find modern clothes that have a lower impact on the environment and are more affordable by being pre-owned.  

#### User Stories 

As an anonymous user: 
-	I want to brows the products the company are offering.
-	I want to be able to sign up to become a registered user. 

As a registered user 
-	I want to be able to log in to my account. 
-	I want to be able to log out from my account. 
-	I want to be able to save products that I like to my profile so I can easily find them later. 
-	I want to be able to add and delete products to my shopping bag.
-	I want to be able to see my orders.
-	I want my information to be saved for my purchases so that I do not have to fill it in for every new purchase. 
-	I want to be able to by the products I have chosen. 
-	I should only be able to see my own profile page and favorites. 
-	I should only be able to change the profile information of my own profile.
-   I want to be able to get in contact with the site owner if I have any questions. 

### Structure 

The main purpose of the website is for people to by the clothes therefor this will be the most important to get access to on the website. Users that are not registered to the website can’t make a purchase, but they can still brows the clothes on the website to see if they find something they are interested in before having to sign up. The supporting content for registered users is that they can save favorites that they can see on their profile while logged in to their account and that they easily can contact the site owner if they have any questions to make the experience of the website as good as possible. 

### Skeleton 

Figma was used to create the wireframes, you can find them [here](https://www.figma.com/file/g7pvumQdDUknm1F5sEVoK9/MS4?node-id=0%3A1).

### Surface 

#### Colors 
For this project a simple color palette is chosen with black, white, dark grey and one mint green accent color. The reason behind choosing a simple color palette is for the clothes to be the focus point on the website. 

![Color Palette](media/color-palette.png)

#### Typography 

The font chosen for this project is Permanent Marker for the logo and Lato for the rest of the text on the website, the fallback font for both fonts is Sans-Serif Both fonts are found on Google Fonts.   

## Database Structure 

## Features 

### Existing Features

- Navbar
    - The navbar contains links to different parts of the website and the company logo. The navbar also contains a search field so the user can search for specific products on the website. The navbar is sticky so that the user always can navigate top different parts on the website. 
    - As a registered user you will have access to your profile, your favorites and your shopping bag.
- Footer
    - The footer contains links to social media and an about us section. 
- Home page 
    - Navbar (described under navbar)
    - Underneath the navbar are the logo, some text about the store and a link to the products page. 
    - Footer (described under footer)
- Products page
    - Navbar (described under navbar)
    - The products page contains images of the clothes and the title, price and size are displayed underneath the image.
    - Footer (described under footer)
- Selected product page 
    - Navbar (described under navbar)
    - Underneath the navbar an image of the selected product is presented and all the information about the product, the title size, price and color of the product.
    - On this page a button for adding the item from favorites are also presented.
    - On this page there is also a button for the user to add the product to their shopping bag. 
    - Footer (described under footer)
- My shopping bag page 
    - Navbar (described under navbar)
    - Underneath the navbar on this page all the products added to the user's bag are presented, information of the products. There also is a 
    link for the user to remove the item from the shopping bag. 
    - Underneath the items in the shopping bag there are field for the details nessesary for completing the purchase, shipping and payment details. And at the end above the footer a button to complete the burchase is presented. 
    - Underneath the items in the shopping bag a button to go to checkout is presented. 
    - Footer (described under footer)
- Checkout page 
    - On the checkout page to the left there is a form where the user have to fill out all the required infromation and a payment form where the user fills out their card details. Underneath the card retails is a complete order button. 
    - To the left is a order summary. 
    - When clicking on the button the user goes to the order success template where all the order information is presented. 
- My profile page
    - Navbar (described under navbar)
    - Under the navbar the information about the user is presented in a form where the user also can update their information. 
    - Next to the profile information is the user's orders presented. 
    - Underneath the profile information and the orders the messages that the user have sent to the site owners are avalible toghether with the responses that the users have recived. 
    - Footer (described under footer)
- My favorites page
    - Navbar (described under navbar)
    - Underneth the navbar on this page all the items that the users have added to their favorites page are shown. There is an image of the product, and a link to remove the product from favorites, the title, price and size of item. 
    - Footer (described under footer)
- Log in page 
    - Navbar (described under navbar)
    - Underneath the navbar the log in form is presented with a field for the user to fill in their email and passwod and a button on the bottom to log in to their account. 
    - Footer (described under footer)
- Register page
    - Navbar (described under navbar)
    - Underneath the navbar the form for new users is prsesented on this page. There is a field for the user to fill in their email, passwod and to confirm tha password that they have choosen, at the end of the form it is a button to register. 
    - Footer (described under footer) 
- Contact page 
    - Navbar (described under navbar)
    - Underneath the navbar the contact form is presented, the field for the user to ender in their message is presented and underneath a button to submit the form is avalible. 
    - Footer (described under footer)

### Possible Future Features 

## Thechnologies Used 

- [Django](https://www.djangoproject.com/) used to create the project.  
- [HTML5](https://en.wikipedia.org/wiki/HTML5) used to make the structure of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) used to add style to the project.
- [Python3](https://www.python.org/) used as the backend language.
- [JQuery](https://jquery.com/) used to create interactive elements.
- [Heroku](https://id.heroku.com/login) used to deploy the live website.
- [Bootstrap](https://getbootstrap.com/) used to style certain elements and to make the website responsive.
- [Font Awesome](https://fontawesome.com/) used for the icons in the footer.
- [Google Fonts](https://fonts.google.com/) was used to import the fonts used in the project.
- [Gitpod](https://gitpod.io/) used to develop the project.
- [Github](https://github.com/) used to store the source code for the project.
- [Figma](https://www.figma.com/) used to make wireframes for the project.
- [Stripe API](https://stripe.com/en-se) used for payments.
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) used to generate a django secret key.


## Testing

## Deployment

### Deploy to Heroku

1. Create an account on Heroku if you don't have one.
2. Log in to your Heroku account and to the right on the screen and choose **Create New App**.
3. Fill in a unique name in the app name text field.
4. Choose the region closest to you in the choose a region dropdown list.
5. Click on **Create App**.
6. Go to the recourese tab and in the search field search for postgres and choose **Heroku Postgres**. 
7. For plan choose 'Hobby Dev - Free' and click on **Submit Order Form**. 
8. Go back to your teminal and install Dj Database by typing `pip3 install dj_database_url` in you terminal. 
9. Install psycopg2-binary by typing `pip3 install psycopg2-binary` in your terminal. 
10. Freeze your requirements by typing `pip3 freeze > requirements.txt` in your terminal.
11. Import dj_database_url in settings.py.
12.  In database setting comment put the default configuration.
11. Replace the default database with dj_database_url.parse() and add in the database URL from Heroku.
You can find this in the Config Vars in the settings tab.
12. Migrate by typing `python3 manage.py migrate` in the terminal and if you have fixtures you can add them back in now. 
13. You need to create a new superuser by typing `python3 manage.py createsuperuser` in the terminal.
14. Uncomment the default database in settings.py and remove the Heroku database config.
15. Set an if statement to use Postegres when the app is running on Heroku, where the database URL is defined or the default database otherwise. 
16. Install gunicorn by typing `pip3 install gunicorn` in the terminal and freeze the requirements again. 
17. Create a Procfile and write `web: gunicorn your_app_name.wsgi:application` in it. 
18. Log in to heroku by typing `heroku login` in the terminal and log in. 
19. type `heroku config:set DISABLE_COLLECTSTATIC=1 --app your_app_name` to temporary disable collectstatic.
20. Add the hostname of your heroku app and `localhost` in `ALLOWED_HOSTS = []` in settings.py.
21. Add your changes by typing `git add .`, commit by typing `git commit -m"your_commit_message"` and push to guthub by typing `git push in the terminal`.
22. The type `git push heroku master` in the terminal to push to Heroku.
23. Go to your app in heroku and under the deploy tab Click on connect to github, serach for your repository, click on connect and then enable automatic deploys.

### Connect to Amazon Webservices
1. Follow the instructions [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) to create your Bucket in Amazon Webservices.
2. Then create a group and a user in AWS through IAM. You can find instructions on how to create user groups [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html) and how to add users [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html). 
3. Install boto3 by typing `pip3 inatall boto3` in the terminal
4. Install django storage by typing `pip3 install django-storages` in the terminal
5. Freeze your requirements by typing `pip3 freeze > requirements.txt` in your terminal.
6. Add storages to your installed apps in settings.py
7. Add these settings in youre settings.py 
```
    if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    AWS_STORAGE_BUCKET_NAME = 'pre-owned'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
8. On Heroku add AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, USE_AWS to True in the Config Vars and remove DISABLE_COLLECT_STATIC. 
9. Create a file Called custom_storages.py and add in
```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

    class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

    class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
10. Add this in settings.py
```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
11. Add your changes by typing `git add .`, commit by typing `git commit -m"your_commit_message"` and push to Heroku by typing `git push in the terminal`.
12. Now you can add your mediafiles to 3S. 
13. Confirm the email adress for your superuser in the admin or by the email confirmation link. 
14. Add stripe to the Heroku config vars add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY, you can find them on stripe under developers and the API keys. 

### Run code locally 

## Credits 

### Code 

### Media 

### Acknowledgments

