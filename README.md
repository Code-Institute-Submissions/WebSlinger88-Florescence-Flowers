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

