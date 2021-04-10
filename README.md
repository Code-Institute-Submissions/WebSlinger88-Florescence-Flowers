<div align="center">

<img src="media/florescence-logo.png"> <a name="top"></a>

</div>

<div align="justify">

Thanks for visiting Florescence Flowers!

Florescence Flowers is an ecommerce florist website. Users are able to purchase gorgeous bouquets online and get them delivered straight to their door.
Users are able to follow the four basic CRUD functions, Create, Read, Update, and Delete. This means that you can register an account, write user reviews,
add user ratings, view other's reviews / ratings, edit your reviews / ratings, and delete your reviews / ratings. On top of this the user is able to add / 
remove products to a shopping basket and securely checkout using the Stripe payment processing software and application programming interface.

Florescence Flowers is intended to provide great value to those who seek that special gift, for any occasion. The idea for Florescence Flowers originated 
from my love of plants and flowers. There are many plants and flowers within my household, and no matter what mood you're in, flowers always bring happiness
and joy to those who see and smell them. It is a well known fact that flowers bring cheer to those who're celebrating a special occasion, and flowers bring
comfort to those who're grieving. Flowers are emotionally diverse, they mean something to everybody, and that is why I have chosen to create Florescence Flowers.

Please browse Florescence Flower's catalogue of beautiful bouquets, we hope that you manage to find something gorgeous to satisfy your friends, family, or work colleague! You're able to purchase a bouquet quickly without the need to register an account, but if you do register, you'll be able to leave valuable reviews and ratings. You'll also be able to keep track of your purchases through your very own profile page.

Please note that this website is purely for educational purposes only.

</div>

---

## :books: **TABLE OF CONTENTS**

1. [Live Demo](#live-demo)  

2. [UX](#ux)
    * [User Stories](#stories)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
        * [Sketches](#sketches)
        * [Wireframes](#wireframes)
        * [Mockups](#mockups)
    * [Surface](#surface)

3. [Information Architecture](#architecture)
    * [Application Framework](#app-framework)
    * [CSS Framework](#css-framework)
    * [Database](#database)

4. [Existing Features](#existing)
    * [Navigation](#navigation)
    * [Search Flowers](#search)
    * [Sort Flowers](#sort)
    * [Home](#home)
    * [Featured Flowers](#featured)
    * [Varieties](#varieties)
        * [Carnations](#carnations)
        * [Gerbera](#gerbera)
        * [Lilies](#lilies)
        * [Roses](#roses)
    * [Occasions](#occasions)
        * [Birthday](#birthday)
        * [Celebration](#celebration)
        * [Romantic](#romantic)
        * [Sympathy](#sympathy)
        * [Thank You](#thanks)
    * [Colours](#colours)
        * [Blue](#blue)
        * [Orange](#orange)
        * [Pink](#pink)
        * [Red](#red)
        * [White](#white)
        * [Yellow](#yellow)
    * [Flower Details](#product-detail)
    * [Basket](#basket)
    * [Checkout](#checkout)
    * [Delivery](#delivery)
    * [Emails](#email)
    * [Log In](#log-in)
    * [Register](#register)
    * [Profile](#profile)
    * [Management](#manage)
        * [Add Flowers](#add-flowers)
        * [Edit Flowers](#edit-flowers)
        * [Delete Flowers](#delete-flowers)
    * [Ratings & Reviews](#review)
        * [Add Review](#add-review)
        * [Add Rating](#add-rating)
        * [Edit Review](#edit-review)
        * [Delete Review](#delete-review)
    * [Log Out](#log-out)

5. [Features left to Implement](#features-left)

6. [Technologies](#technologies)

7. [Testing](#testing)

8. [Deployment](#deployment)
    * [Deployment to Heroku](#heroku)
    * [Local Deployment](#local)

9. [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#thanks)

---

## :computer: **LIVE DEMO** <a name="live-demo"></a>

Please feel free to delve into a demo of Florescence Flowers's website.

You can live demo Florescence Flowers's website here: [Florescence Flowers](https://florescence-flowers.herokuapp.com/).

<div align="center">

![Responsive showcase image of Florescence Flowers website](media/ms4-showcase.png "Responsive showcase image of Florescence Flowers website")

</div>

---

## :sparkles: **UX** <a name="ux"></a>

<div align="justify">

The user experience (UX) is what a user of a particular product experiences when using that product. A UX designer's job is thus to create a product that 
provides the best possible user experience. We're going to provide some insight into the UX process here, focusing on the important Who, What and How?

Florescence Flowers, as previously stated, is an ecommerce florist website that's purpose is to provide users with an easy, approachable, stress-free way to 
shop for flowers, no matter what the occasion, and no matter who the recipitant. The hope is that anyone can visit, browse, purchase, and be satisfied with
their experience. Users will be able to create accounts and relay their personal experiences in the form of reviews and ratings.

Carry on below and read some of Florescence Flowers's user stories, and get a feel for what people originally wanted out of Florescence Flowers.

</div>

---

### **USER STORIES** <a name="stories"></a>

| **As a...**                    | **I want to...**                        | **So I can...**                                                    |
|:-------------------------------|:----------------------------------------|:-------------------------------------------------------------------|
| Potential Shopper              | View a selection of products            | Potentially buy some products                                      |
| Potential Shopper              | Search products                         | Find a specific product I'd like to buy                            |
| Potential Shopper              | Sort products                           | Find specific prices, ratings etc.                                 |
| Potential Shopper              | View individual products                | To view prices, descriptions and ratings                           |
| Potential Shopper              | Easily register an account              | Have a personal account to view order history etc.                 |
| Potential Shopper              | Easily login or logout                  | Access my personal account                                         |
| Shopper                        | Purchase a product                      | Own a new product                                                  |
| Shopper                        | Add reviews                             | Share my experiences                                               |
| Shopper                        | Edit reviews                            | Change my review if I've made a mistake or changed my mind         |
| Shopper                        | Delete reviews                          | Remove any unwanted reviews from the site                          |
| Shopper                        | Rate products                           | Help others easily understand how good a product may or may not be |
| Shopper                        | Edit ratings                            | Change my rating if my feelings change                             |
| Shopper                        | Not have others edit/delete my reviews  | Keep my reviews personal and my own                                |
| Shopper                        | Have my own profile page                | Have my order history and delivery details in one place            |
| Shopper                        | Recieve email confirmations             | Keep track of my orders and their order numbers / details          |
| Admin                          | Add a new product                       | Have a new product on the website to sell                          |
| Admin                          | Edit a product                          | Change any product details that may change                         |
| Admin                          | Delete a product                        | Remove a product from the website that has been delisted           |
| Admin                          | Set featured products                   | Display specific products on the home page                         |

---

### **STRATEGY** <a name="strategy"></a>

<div align="justify">

The strategy of the Florescence Flowers website is to provide a highly attractive, user-friendly, responsive ecommerce experience. Any prospective buyer will be able to easily navigate their way to purchasing a product from start to finish. They'll then be able to share their experiences in the form of ratings and reviews, and be able to keep track of their orders via email confirmations and profile pages. Our long term ambition is that Florescence Flowers builds an extensive library of products far beyond the current scope. Extra varieties and occasions will be added in the future as well as FAQs and newsletters. What's most important is that
people walk away with a feel-good vibe, and are happy with their visit to Florescence Flowers.

</div>

---

### **SCOPE** <a name="scope"></a>

<div align="justify">

The scope of Florescence Flowers is to provide a flawless user experience straight from the get-go. We want users to be highly engrossed in what they encounter. We
want users to be attracted to the layout, the colour scheme, the ease of navigation, and the simplicity of the registration process as well as the checkout process. Ultimately we want users to return time and time again, to find a new product and to be impressed with the ease of use.

</div>

---

### **STRUCTURE** <a name="structure"></a>

<div align="justify">

The structure of Florescence Flowers has been carefully thought-out to provide the best possible user experience. Everything from the layout to the navigation has been
structured for a friendly, easy to use, attractive approach. Please read below for a description of each page's structure.

* Each page has a Florescence Flowers logo situated at the top center of the screen. Surrounding this, you'll find navigation links which direct the user to each
page within the Florescence Flowers website. There are seven main navigation links (Home, Varieties, Occasions, Colours, Search, Accounts, Basket), many of which  being hoverable dropdown menus with additional links. When a user logs in, the Account link expands, showing additional links (Profile, Log Out), and with the loss of two links (Register, Log In). Admin users have an additional account option that is 'Manage'. Admin users will be able to add new products to the Florescence Flowers website by navigating to this link. There are eleven main pages in total, each with their own unique features. Each page contains a footer located at the bottom of the page. This footer includes developer information, copyright information, and links to the developer's social media. All pages feature a 'To Top Button' which navigates the user to the top of the page. This button is located in the bottom right-hand side of the screen.

* The Home page consists of bright colourful images and easy to read text. The Home page serves to provide information about the Florescence Flowers website and featured products.

* There are four Variety pages, each enabling the user to view specific flowers related to their respective variety. Each page consists of a navigation bar, a main header, a sort function, free delivery information, and a multitude of flower cards containing an image, a name, a price, and a rating. Admin users have the ability to edit and/or delete products from here.

* As it stands there are currently five different Occasions that our flowers relate to and they are: Birthday, Celebration, Romantic, Sympathy, and Thank You. If a user is looking for Valentines flowers, for example, then navigating to the Romantic Occasion will display flowers such as Red Roses. These occasions have been implemented in order to help the user distinguish between different flowers.

* As it stands there are currently six different Colour categories that our flowers fall into and they are: Blue, Orange, Pink, Red, White, and Yellow. If a user is searching for blue flowers, for example, then navigating to the Blue Colour category will display flowers that are blue and/or have blue in them. These Colour categories have been implemented in order to help the user distinguish between different flowers and to also make searching more efficient.

* The Log In page features a main heading, underneath the heading you'll find a register button for those who do not currently have an account. Below this you'll find a simple form consisting of three elements: Username field, a Password field, and a Log In button. There is a 'Remember me' checkbox and a 'Forgotten Password' link.

* The Register page looks almost identical to the Log In page. It has a few additional fields. It has an email field and a confirmation email/password field. There is a 'Log In' link for those who already have an account.

* The Product Detail page displays a single product (flower) which offers the user product information and the ability to add the product to a shopping basket. Here you will find product prices, ratings, descriptions, quantity selectors and navigation / submit buttons. The submit button adds a product to the basket. The navigation links direct the user to either the previous page or the basket page. The Product Detail page also includes user review forms and displays. When a user is logged into their account they have the ability to create, edit and delete reviews and ratings. Please note that users can only edit and delete their own reviews. Posted reviews are visible to the public at any time. User ratings are accumulated into an average rating which is displayed within each product's card / Product Detail page.

* The Basket page offers the ability to see what products a user has in their basket. Product image, variety, colour, price and quantity are all shown here. The ability to update the product quantity is present here, as well as the ability to remove the item from the basket completely. A Grand Total is displayed at the bottom of the page along with any calculated delivery costs. A user can either navigate to the previous page or navigate on to the checkout page.

* The Checkout page includes all of the information shown in the Basket page but it also includes a Stripe payment form. This form consists of many fields, Name, Email, Phone, Address, Bank Card Number, to name a few... Once the form has been submitted using the 'Complete Order' button, the user is directed to the Checout Complete page.

* The Checkout Complete page holds all of a user's order information. Order Number, Order Date, User Details, Order Details, and Order Costs are all found here. This page and all of it's details are available to view via the user's Profile page.

* The Profile page holds all historical orders that a user has made. Order Number, Date, Product and Cost are all shown here. A user can click on an order number and that order's Checkout Complete page will be generated. A user's delivery details can also be saved here. This makes it much quicker for a user to purchase an item without having to enter their address every time.

* The Management page, or Add Product page, is where an Admin user can add additional products to the website. Upon arrival to the page the admin user is presented with a simple form to complete. This form is comprised of six text fields, a featured checkbox, and a select image button. A cancel button and an Add Flower button are present here.

* There is a simple Log Out page which offers the user an option of whether to log out or not.

</div>

---

### **SKELETON** <a name="skeleton"></a>

#### *Sketches* <a name="sketches"></a>

<div align="justify">

Florescence Flowers's website started on a piece of paper. Sketches were drawn out and a decent design was soon ready to leap into the digital world.
Here are links to images of the original sketches used to help develop this project:

* [Home Page Sketch](design/sketches/ms4-sketch-home.PNG)
* [Products Page Sketch](design/sketches/ms4-sketch-products.PNG)
* [Product Detail Page Sketch](design/sketches/ms4-sketch-productDetail.PNG)
* [Basket Page Sketch](design/sketches/ms4-sketch-basket.PNG)
* [Checkout Page Sketch](design/sketches/ms4-sketch-checkout.PNG)
* [Log In Page Sketch](design/sketches/ms4-sketch-login.PNG)
* [Register Page Sketch](design/sketches/ms4-sketch-register.PNG)
* [Profile Page Sketch](design/sketches/ms4-sketch-profile.PNG)
* [Add / Edit Page Sketch](design/sketches/ms4-sketch-addEdit.PNG)

</div>

#### *Wireframes* <a name="wireframes"></a>

<div align="justify">

After drawing up the sketches it was time to get them onto the screen. To do this, a wireframe was created using Balsamiq Wireframes 4. 
Wireframes are used to display what the creator ultimately envisions the website to look like, roughly! It acts as one of the first stepping stones of the journey.
Here are links to images of the original sketches used to help develop this project:

* [Desktop Home Page](design/wireframes/ms4-wireframe-home.PNG)
    * [Mobile Home Page](design/wireframes/ms4-mobile-wireframe-home.PNG)
    * [Mobile Navigation](design/wireframes/ms4-mobile-navigation-wireframe.PNG)

* [Desktop Products Page](design/wireframes/ms4-wireframe-products.PNG)
    * [Mobile Products Page](design/wireframes/ms4-mobile-wireframe-products.PNG)

* [Desktop Product Detail Page](design/wireframes/ms4-wireframe-productDetail.PNG)
    * [Mobile Product Detail Page](design/wireframes/ms4-mobile-wireframe-productDetail.PNG)

* [Desktop Basket Page](design/wireframes/ms4-wireframe-basket.PNG)
    * [Mobile Basket Page](design/wireframes/ms4-mobile-wireframe-basket.PNG)

* [Desktop Checkout Page](design/wireframes/ms4-wireframe-checkout.PNG)
    * [Mobile Checkout Page](design/wireframes/ms4-mobile-wireframe-checkout.PNG)

* [Desktop Log In Page](design/wireframes/ms4-wireframe-login.PNG)
    * [Mobile Log In Page](design/wireframes/ms4-mobile-wireframe-login.PNG)

* [Desktop Register Page](design/wireframes/ms4-wireframe-register.PNG)
    * [Mobile Register Page](design/wireframes/ms4-mobile-wireframe-register.PNG)

* [Desktop Profile Page](design/wireframes/ms4-wireframe-profile.PNG)
    * [Mobile Profile Page](design/wireframes/ms4-mobile-wireframe-profile.PNG)

* [Desktop Add / Edit Page](design/wireframes/ms4-wireframe-addEdit.PNG)
    * [Mobile Add / Edit Page](design/wireframes/ms4-mobile-wireframe-addEdit.PNG)

</div>

#### *Mock Ups* <a name="mockups"></a>

<div align="justify">

Finally with the basics down on paper and screen, it was time to start shaping things up. After wireframes, it's time to take things a little more seriously. 
Enter Adobe XD. Adobe XD is a powerful piece of software designed to assist artists worldwide. More detailed designs are now progressed, and sketches etc.. 
are now a thing of the past! below, you will find links to the original Florescence Flowers Mock-Ups. You can clearly see how the project has evolved.

* [Desktop Home Page](design/mockups/ms4-mockup-home.PNG)
    * [Mobile Home Page](design/mockups/ms4-mobile-mockup-home.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-home.PNG)
    * [Mobile Navigation](design/mockups/ms4-mockup-mobile-navigation.PNG)

* [Desktop Products Page](design/mockups/ms4-mockup-products.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-products.PNG)
    * [Mobile Products Page](design/mockups/ms4-mobile-mockup-products.PNG)

* [Desktop Product Detail Page](design/mockups/ms4-mockup-productDetail.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-productDetail.PNG)
    * [Mobile Product Detail Page](design/mockups/ms4-mobile-mockup-productDetail.PNG)

* [Desktop Basket Page](design/mockups/ms4-mockup-basket.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-basket.PNG)
    * [Mobile Basket Page](design/mockups/ms4-mobile-mockup-basket.PNG)

* [Desktop Checkout Page](design/mockups/ms4-mockup-checkout.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-checkout.PNG)
    * [Mobile Checkout Page](design/mockups/ms4-mobile-mockup-checkout.PNG)

* [Desktop Log In Page](design/mockups/ms4-mockup-login.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-login.PNG)
    * [Mobile Log In Page](design/mockups/ms4-mobile-mockup-login.PNG)

* [Desktop Register Page](design/mockups/ms4-mockup-register.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-register.PNG)
    * [Mobile Register Page](design/mockups/ms4-mobile-mockup-register.PNG)

* [Desktop Profile Page](design/mockups/ms4-mockup-profile.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-profile.PNG)
    * [Mobile Profile Page](design/mockups/ms4-mobile-mockup-profile.PNG)

* [Desktop Add / Edit Page](design/mockups/ms4-mockup-addEdit.PNG)
    * [Tablet Home Page](design/mockups/ms4-tablet-mockup-addEdit.PNG)
    * [Mobile Add / Edit Page](design/mockups/ms4-mobile-mockup-addEdit.PNG)

</div>

