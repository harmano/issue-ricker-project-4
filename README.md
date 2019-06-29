# The Cookbook
The Issue Ticker is a simple, yet unique form of submitting and viewing local bugs and features. The site comes with fully login and registering cabilbilties, a functioning cart and checkout page; all which allows users to securely purchase solutions with a few steps. On the home page, users have the option of posting a bug or feature with a simple form. After a bug or feature is posted and a solution is purchased, users will be emailed with the requisite documents for the solution. Also, at the end of the week, a public solution will be posted for the post with the most likes. There is also a simple community and profile page. 

## UX
The website is intended for software programmers having unresolved issues with a bug or feature. The Issue Ticker allows users to share their very own issues, while having the ability to discover new issues others have posted. Through a very sleek and user friendly interface, the Issue Ticker allows for quick uploads and purchases.

User Stories
* User 1: As an uploader, I want to click on the add button, so I can upload an issue
* User 2: As a viewer, I would maneuver the home page, so I could view other issues
* User 2: As a viewer, I would maneuver the community page, so I could site information
* User 2: As a viewer, I would maneuver the profile page, so I could see profile information
* User 3: As a buyer, I would click the purchase button, so I buy a solution
* User 4: As a user, I would click the register button, so I can sign up as a user



Mock Up
* Adding an issue: /static/media/add bug or feature.jpg
* Cart: /static/media/Cart.jpg
* Home: /static/media/Home after login.jpg
* Login: /static/media/Home.jpg
* Profile: /static/media/Profile.jpg
* Issue Detail: /static/media/specific bug.jpg


## Features
The Cookbook includes the following features:
* Purchasing: Users 3 can buy any solutions
* Adding an issue: User 1 can upload an issue
* Login: This allows all users to securely access the site by registering and then filling in login credentials,  also allows for resetting passwords 



### Features Left to Implement
* Search Bar
* A profile page with password changing capabilities 

## Technologies Used
Django 1.11
This project uses the Django framework, while utilizing various imports
*https://docs.djangoproject.com/en/2.2/releases/1.11/


Python
This project use the Python language to write code. 
* https://www.python.org/

HTML
This project uses HTML to create web pages.

Javascript
This project uses Javascript for animations and transitions.
* https://www.javascript.com/

Bootstrap 
This project uses bootstrap for css styling.
* https://getbootstrap.com/docs/4.3/layout/overview/

Materialize  
This project uses materialize for css styling.
* https://materializecss.com/

Stripe
This project uses stripe for purchasing 
*https://stripe.com/en-ca

## Testing
Delete Recipe:
* Go to “Home” page
* Press delete recipe 
* Recipe is deleted 

Add Issue:
* Go to “Home” page
* Click add button
* Submit an empty form and verify that an error message about the required fields appears
* Submit the  filled form 
* Redirects to “Home” page
* Issues Appears

Buy Page:
* Go to “Home” page
* Click on the buy button
* Verify that issue is stored in cart
* Redirects to home

View Issue:
* Go to “Home” page
* Click on issue 
* Verify that issue details appear

View Cart:
* Go to “Cart” page
* Click on checkout 
* Verify the checkout page appears

View Checkout:
* Go to “Checkout” page
* Click on checkout 
* Submit an empty form and verify that an error message about the required fields appears
* Submit the  filled form 
* Redirects to “Home” page

## Deployment
This project was deployed through Heroku, and does not differ from other versions. 

### Content
* Login Jumbo photo: https://static1.squarespace.com/static/5695456940667a42fbdabb9d/56ac4b2542f5526b480dda65/5a32c76fc8302501781e177f/1513353265770/christopher-gower-291246.jpg?format=1500w
* Home Jumbo photo: https://www.techdonut.co.uk/sites/default/files/what-is-screen-resolution_1042807015.jpg
* Post detail photo: https://image.flaticon.com/icons/svg/356/356934.svg
* Add issue photo: https://umaine.edu/umss/wp-content/uploads/sites/458/2018/06/Forms-icon.png

