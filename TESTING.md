<div align="center">

<img src="media/florescence-logo.png"> <a name="top"></a>

# **FLORESCENCE FLOWERS TESTING** <a name="top"></a>

</div>

<div align="justify">

Within this markdown file, you shall find extensive test analysis and reporting for the Florescence Flowers website. This has been added in a separate file for its readability and user-friendly approach. You can return to Florescence Flowers's main readme file here: [README](https://github.com/WebSlinger88/Florescence-Flowers/blob/master/README.md).

You can also find an Excel spreadsheet (saved as PDF) containing extensive test analysis and reporting. This spreadsheet is intended to provide a more visual report. You can find a link to the Excel spreadsheet and downloadable PDF report here: [Florescence Flowers Testing Docs](#).

</div>

---

## :books: **TABLE OF CONTENTS**

1. [Testing](#testing)
    * [Navigation](#nav-test)
    * [Search Flowers](#search-test)
    * [Sort Flowers](#sort-test)
    * [Home](#home-test)
    * [Featured Flowers](#featured-test)
    * [Varieties](#varieties-test)
        * [Carnations](#carnations-test)
        * [Gerbera](#gerbera-test)
        * [Lilies](#lilies-test)
        * [Roses](#roses-test)
    * [Occasions](#occasions-test)
        * [Birthday](#birthday-test)
        * [Celebration](#celebration-test)
        * [Romantic](#romantic-test)
        * [Sympathy](#sympathy-test)
        * [Thank You](#thanks-test)
    * [Colours](#colours-test)
        * [Blue](#blue-test)
        * [Orange](#orange-test)
        * [Pink](#pink-test)
        * [Red](#red-test)
        * [White](#white-test)
        * [Yellow](#yellow-test)
    * [Flower Details](#product-detail-test)
    * [Basket](#basket-test)
    * [Checkout](#checkout-test)
    * [Checkout Complete](#complete-test)
    * [Delivery](#delivery-test)
    * [Emails](#email-test)
    * [Log In](#log-in-test)
    * [Register](#register-test)
    * [Profile](#profile-test)
    * [Management](#manage-test)
        * [Add Flowers](#add-flowers-test)
        * [Edit Flowers](#edit-flowers-test)
        * [Delete Flowers](#delete-flowers-test)
    * [Ratings & Reviews](#review-test)
        * [Add Review](#add-review-test)
        * [Add Rating](#add-rating-test)
        * [Edit Review](#edit-review-test)
        * [Delete Review](#delete-review-test)
    * [Log Out](#log-out-test)
    * [Other Features](#other-feat-test)

2. [Display Testing](#display-test)

3. [Code Validation](#validation)

4. [Other](#other)
    * [Image Size Reduction](#size)
    * [Spelling & Grammar](#spell)

---

## :test_tube: **TESTING** <a name="testing"></a>

<div align="justify">

### **NAVIGATION** <a name="nav-test"></a>

* Navigation bar present within all web pages.
* Navigation bar contains five links, across all web pages. Home, Varieties, Occasions, Colours and Search.
* Dropdown menu for varieties, occasions and colours work perfectly.
* Additional links for Account and Basket are present on all pages in the top right corner of the screen.
* Account link makes dropdown menu appear.
* Account dropdown menu has two options when not logged in: Log In & Register.
* Account dropdown menu has two options when logged in: Profile & Log Out.
* Account dropdown menu has three options when logged in: Manage, Profile & Log Out.
* All links load the correct pages.
* Hover.css animation works when mouse is hovered over nav links.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* Basket link displays and calculates price correctly.
* Search bar submit button loads results as expected.
* Footer's social links load correct pages as expected.
* Mobile Navigation hamburger icon appears when under 992px.
* When clicked, side nav menu appears below.
* All links within mobile nav work as expected. Dropdown menu for varieties, occasions and colours also works perfectly.
* Mobile Search icon appears when under 992px.
* Search icon makes search bar appear in mobile view.
* Mobile Account icon appears when under 992px.
* Mobile Basket icon & price appears when under 992px.
* All navigation bars and their content are responsive.

***No Issues were found whilst testing the Navigation functionality.***

---

### **SEARCH FLOWERS** <a name="search-test"></a>

* Am able to type into search box.
* Submit buttons works without issue.
* When typing known colour into box, correct flowers appear.
* When typing roses into box, correct flowers appear.
* When typing random word into box, 0 Flowers Found message appears, as expected.
* Search functionality is all responsive.

***No Issues were found whilst testing the Search Flowers functionality.***

---

### **SORT FLOWERS** <a name="sort-test"></a>

* Sort dropdown box appears when on any page that displays multiple product cards.
* There are twelve options to choose from. Price, Rating, Name, Variety Occasion, and Colour can all be viewed in ascending or descending order.
* Each option sorts the products correctly.
* Sort functionality is all responsive.

***No Issues were found whilst testing the Sort Flowers functionality.***

---

### **HOME PAGE** <a name="home-test"></a>

* All text and images are responsive.
* Bootstrap grid works as expected.
* Carousel scrolls through images as expected with correct interval.
* Carousel gets smaller as resolution decreases. Works well.
* Text is easy to read.
* Shop now button takes user to all products page.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.

***No Issues were found whilst testing the Home Page functionality.***

---

### **FEATURED FLOWERS** <a name="featured-test"></a>

* Featured Flower cards display iamges and text correctly.
* Featured Flower cards are responsive.
* Featured Flower cards average rating calculates and displays as expected.
* Featured Flower cards' images load the correct product detail page when clicked.
* Admin's update/remove buttons appear when logged in as admin.
* Clicking update link renders correct "Add Product" page.
* Clicking remove link makes modal message appear.
* Modal message cancel button returns admin user to home page.
* Modal message delete button completely removes product from database/website.
* Modal message is responsive.

---

### **VARIETIES** <a name="varieties-test"></a>

#### *All Flowers* <a name="products-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the database are shown on page when you select the "All Flowers" link under the Varieties nav link.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Carnations* <a name="carnations-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All Carnations within the Carnations category are shown correctly when on the Carnations Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Gerbera* <a name="gerbera-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All Gerbera within the Gerbera category are shown correctly when on the Gerbera Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Lilies* <a name="lilies-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All Lilies within the Lilies category are shown correctly when on the Lilies Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Roses* <a name="roses-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All Roses within the Lilies Roses are shown correctly when on the Roses Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

---

### **OCCASIONS** <a name="occasions-test"></a>

#### *Birthday* <a name="birthday-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Birthday occasion model are shown correctly when on the Birthday Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Celebration* <a name="celebration-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Celebration occasion model are shown correctly when on the Celebration Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Romantic* <a name="romantic-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Romantic occasion model are shown correctly when on the Romantic Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Sympathy* <a name="sympathy-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Sympathy occasion model are shown correctly when on the Sympathy Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Thank You* <a name="thanks-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Thank You occasion model are shown correctly when on the Thank You Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

---

### **COLOURS** <a name="colours-test"></a>

#### *Blue* <a name="blue-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Blue colour model are shown correctly when on the Blue Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Orange* <a name="orange-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Orange colour model are shown correctly when on the Orange Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Pink* <a name="pink-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Pink colour model are shown correctly when on the Pink Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Red* <a name="red-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Red colour model are shown correctly when on the Red Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *White* <a name="white-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the White colour model are shown correctly when on the White Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

#### *Yellow* <a name="yellow-test"></a>

* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* All flowers within the Yellow colour model are shown correctly when on the Yellow Page.
* Flower counter to left of screen displays correct amount of flowers.
* All is responsive.

---

### **FLOWER DETAILS** <a name="colours-test"></a>

* Whole page is responsive.
* Average Rating calculates and displays as expected.
* Admin user's "Update" link renders the correct page.
* Admin user's "Remove" link generates modal message.
* Modal message's cencel button removes the modal.
* Modal message's delete button completely removes product from website/database.
* Able to increase and decrease quantity using plus and minus buttons.
* Cannot submit quantity form if field is empty. Warning message appears.
* Add to basket button adds correct product and product quantity to shopping basket.
* Go back button returns user back to all products page.
* Basket button renders correct page.
* Toast message appears when adding products to the basket.
* Toast message includes all relevant information. Nothing is missing.
* Toast message disappears after 5 seconds thanks to functional javascript.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* If logged out, flower review message under subheading asks you to login to add review.
* If product hasn't been reviewed, a no review message is written in large font.
* If product does have reviews, no review message is not present.
* If product does have reviews, review box is shown that contains user name, date-time, rating and text content.
* If user is logged, in text field and rating dropdown box are visible with submit button below.
* If user is logged in and has previously posted a review, edit and delete icons are present.
* Edit and delete icons are not present for reviews left by other users.

***Extensive Review/Rating testing can be found [here](#review-test).***
***No Issues were found whilst testing the Product Detail Page functionality.***

---

### **BASKET** <a name="basket-test"></a>

* Whole page is responsive.
* Correct information is displayed.
* Able to increase and decrease quantity using plus and minus buttons.
* Clicking "Update" with an empty quantity form results in that product being removed from the basket. Previously, an error 500 occurred but code was added to forms.py so that this error did not occur.
* "Remove" button removes item from basket.
* "Remove" button causes toast message to appear. Correct message was displayed.
* Subtotal calculates as expected.
* Delivery cost calculates as expected.
* Free delivery when total is above the free delivery threshold, which is £30.
* Grand total calculates as expected.
* "Keep Browsing" button renders correct page.
* "Secure Checkout" button renders correct page.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.

***No Issues were found whilst testing the Basket Page functionality.***

---

### **CHECKOUT** <a name="checkout-test"></a>

* Whole page is responsive.
* Products I added to basket appear in a list to the right.
* Order summary counter calculates correctly.
* Image, Name, Variety, Colour and Quantity are all correct.
* Subtotal is calculated correctly.
* Delivery total is calculated correctly.
* Grand total is calculated correctly.
* Save to profile checkbox works.
* Checkout form populates fields because delivery information is saved to profile.
* Full Name does not populate.
* Stripe payment form works as expected.
* Errors appear if card info is entered incorrectly. As expected!
* Card payment warning at bottom next to "Complete Order" button calculates corrctly.
* "Update basket" button returns user to basket page as expected.
* "Complete Order" button renders correct page as expected.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.


***Only issue found whilst testing the Checkout Page was unpopulated Full Name field. Will add to Features to Implement.***

---

### **CHECKOUT COMPLETE** <a name="complete-test"></a>

* Whole page is responsive.
* Order number is present.
* Correct Date & Time of order is displayed.
* My delivery details are correct.
* My ordered products are correct.
* The order total, delivery cost and grand total are correct.
* "Back to flowers" button renders correct page.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.
* Email was received upon order completion.

***No Issues were found whilst testing the Checkout Complete Page functionality.***

---

### **DELIVERY** <a name="delivery-test"></a>

* Free delivery threshold is set to £30.
* Delivery always sets to £0 when total goes above £30.
* Add to basket toast informs user how much money is required to reach the free delivery threshold.
* Delivery percent is set to 15%.
* Delivery total is always calculated correctly. Tested with multiple purchases.
* Delivery total is displayed correctly in all relevant pages, including emails.

***No Issues were found whilst testing the Delivery functionality.***

---

### **EMAILS** <a name="email-test"></a>

* Emails are being received as expected when creating an account. Email confirmation email received.
* Emails are being received as expected when user requests a password reset.
* Emails are being received as expected when user purchases a product.
* Email confirmation email contains correct content. Confirmation link renders the correct page.
* Password reset email contains correct content. Password reset link renders the correct page.
* Order confirmation email contains correct content. All order info is accurate.
* All emails were recieved between five and ten seconds.

***No Issues were found whilst testing the Email functionality.***

---

### **LOG IN** <a name="login-test"></a>

* Whole page is responsive.
* Log In page's register link renders the correct page.
* Can type into username/password fields.
* Warning appears when submit button is clicked and fields are empty.
* Remember Me button not working as expected so will remove before deployment and add to Features to Implement.
* Form submit button renders correct page when form is valid.
* Invalid form results in error message as expected.
* Forgot Password link renders the correct page.
* Log In toast appears as expected when user logs in.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.

***Only issue found whilst testing the Log In functionality was that the 'Remember Me' checkbox wasn't remembering anything. Will add to Features to Implement.***

---

### **REGISTER** <a name="register-test"></a>

* Whole page is responsive.
* Register page's login link renders the correct page.
* Can type into all fields.
* Warning appears when submit button is clicked and fields are empty.
* Form submit button renders correct page when form is valid.
* Warning message appears when @ sign isn't present in email fields.
* Form submit button renders correct page when form is valid.
* Invalid form results in error message as expected.
* Error message appears if email/username is already used.
* Confirmation email toast appears when form is submitted.
* Email verification page is rendered as expected.
* Confirmation email is received within ten seconds.
* Confirmation email contains correct content and confirmation link renders correct page.
* Confirmation page link works as expected and renders correct page.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.

***No Issues were found whilst testing the Register functionality.***

---

### **PROFILE** <a name="profile-test"></a>

* Whole page is responsive.
* Username is displayed within main heading.
* Can type into all Delivery details fields.
* "Update Information" button works as expected and saves all info.
* Delivery details were already populated upon arival because "Save information" checkbox was clicked within Checkout page.
* All historical order details are displayed correctly.
* Order numbers can be clicked. Each order number renders the correct Checkout Complete page with detailed order information.
* Date and Time of all orders are accurate.
* Products purchased within Order Details are correct.
* Cost of products displayed are correct.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.

***No Issues were found whilst testing the Profile functionality.***

---

### **MANAGEMENT** <a name="manage-test"></a>

#### *Add Flowers* <a name="add-flowers-test"></a>

* Whole page is responsive.
* Can type into all fields and/or select dropdown boxes.
* Can select Featured Flowers checkbox.
* Select Image button allows admin to select image from local drive.
* Message appears when image is selected.
* avgRating field removed as not needed.
* avgRating field required set to False.
* Warning appears when submit button is clicked and fields are empty.
* When all fields are valid, new product appears in database and all relevant pages.
* When no image is selected, default image is used.
* Cancel button cancels adding process and renders correct page.
* Add Flower button renders current page incase additional products are to be added.
* Cannot type letters into INT field as expected.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.

***No Issues were found whilst testing the Add Flowers functionality.***

#### *Edit Flowers* <a name="edit-flowers-test"></a>

* Whole page is responsive.
* Can type into all fields and/or select dropdown boxes.
* Can select Featured Flowers checkbox.
* Select Image button allows admin to select image from local drive.
* Message appears when image is selected.
* avgRating field removed as not needed.
* avgRating field required set to False.
* Warning appears when submit button is clicked and fields are empty.
* When all fields are valid, product has been changed in database and all relevant pages.
* When no image checkbox is checked, default image is used.
* Cancel button cancels the editing process and renders correct page.
* Update Flower button renders correct page.
* Cannot type letters into INT field as expected.
* Clicking the remove checkbox and clicking submit removed the image and the default image is used.
* To Top Button appears when scroll down. Disappears at top of screen. When clicked, scrolls to top of screen. Works as expected.

***No Issues were found whilst testing the Edit Flowers functionality.***

#### *Delete Flowers* <a name="delete-flowers-test"></a>

* When any delete link is clicked, modal message appears.
* When cancel button is clicked, modal message disappears.
* When delete button is clicked, the product is permanently removed from the database/website.
* When delete button is clicked, toast message appears.

***No Issues were found whilst testing the Delete Flowers functionality.***

---

### **RATINGS & REVIEWS** <a name="review-test"></a>

#### *Add Review* <a name="add-review-test"></a>

* When not logged in, "Please Log In" message is displayed under "Flower Reviews" heading.
* When a product has no reviews, a no reivews message is displayed.
* When logged in, ratings dropdown box is present.
* When logged in, review textarea is present.
* When logged in, review submit button is present.
* Can type into textarea.
* Can only post a review if a rating is selected.
* Can click submit button and only post rating. Textarea can be empty. This is expected.
* When submit button is clicked, toast message appears.
* Posted reviews appear below rate / reviews fields.
* Everything is responsive.

#### *Add Rating* <a name="add-rating-test"></a>

* When not logged in, "Please Log In" message is displayed under "Flower Reviews" heading.
* When logged in, ratings dropdown box is present.
* Rating dropdown box works as expected. Can select options one to five.
* Can only post a review if a rating is selected.
* Can click submit button and only post rating. Textarea can be empty. This is expected.
* When submit button is clicked, toast message appears.
* Posted ratings appear below rate / reviews fields.
* All new ratings' average is calculated correctly and displayed properly in all areas expected.
* Everything is responsive.

#### *Edit Review* <a name="edit-review-test"></a>

* Only logged in users can edit reviews.
* Users cannot edit each other's reviews. You can only edit your own reviews.
* A Font Awesome user icon is located within the posted review. This is a link to edit a review. Link works as expected.
* Link makes rating downdown box appear and empty textarea appears also.
* Can type into new textarea.
* Dropdown options default at one. Options are one to five.
* Submit button successfully edits both rating and review. Old reviews and ratings are replaced.
* Everything is responsive.

#### *Delete Review* <a name="delete-review-test"></a>

* Only logged in users can delete reviews.
* Users cannot delete each other's reviews. You can only delete your own reviews.
* A Font Awesome trash icon is located within the posted review. This is a button to delete a review. Button works as expected.
* When trash icon is clicked, modal message appears.
* Clicking cancel button within the modal message simply cancels the deletion process as expected.
* Clicking the delete button removed the review from the product detail page completely and cannot be reversed.
* Toast message appears when a review is deleted.
* Everything is responsive.

---

### **LOG OUT** <a name="logout-test"></a>

* Log Out link is located in the Account dropdown menu, top right of the screen.
* Log Out link redners the correct page.
* The "No" button rejects the idea of logging out and returns the user to the Home page, logged in session.
* The "Yes" button will log the user out of their current session and redirect them to the Home page.
* Once logged out, a toast message appears.
* Everything is responsive.
* All works as expected.

---

### **OTHER FEATURES** <a name="other-feat-test"></a>

* Tested all Javascript to ensure all features perform to standard.
* Tested models, views and urls to ensure website performed as expected.
* Tested toasts to ensure messages are correct and success/info are used in the right setting.
* Tested toast's javascript setTimeout delay.
* Tested uploading different size images using the Add Flowers function. Wide images don't sit as well as expected.

</div>

---

## :tv: **DISPLAY TESTING** <a name="display-test"></a>

<div align="justify">

The Florescence Flowers website has been tested using an 18" Dell XPS laptop with Windows 10 + on an external 30" display as well as the following devices:

</div>

| **Browser Platform**                       | **Version**    
| -------------------------------------------|:---------------------------------------------:| 
| Google Chrome (Official Build) (64-bit)    | 89.0.4389.128
| Firefox (Windows 10)                       | 87.0
| Opera (Windows 10)                         | 75.0.3969.149
| Edge (Windows 10)                          | 89.0.774.75
| Google Chrome Android (Samsung Galaxy S8+) | 90.0.4430.66
| Google Chrome Android (OnePlus 7T Pro)     | 90.0.4430.66
| Safari iOS (Apple iPhone 7 Plus)           | 14.0
| Silk Android (Amazon Kindle Fire 5)        | 83.3.19.4103.106.30
| Internet Explorer 10                       | [Cloud Browser](https://www.ieonchrome.com/)
| Internet Explorer 11                       | [Cloud Browser](https://www.ieonchrome.com/)

<div align="justify">

All tests were positive and no issues found apart from Internet Explorer 10 & 11. Both browsers had extreme lag and many things didn't work and/or were 
displayed incorrectly. This is not a problem because Internet Explorer is now obsolete.

It is worth mentioning that the Florescence Flowers favicon image displays within the browser's tab for all HTML pages.

***Further insight into the display testing process is documented in an external file located [here.](#)***

</div>

---

## :heavy_check_mark: **CODE VALIDATION** <a name="validation"></a>

<div align="justify">

Florescence Flowers's code has been tested via the [W3C Markup Validation Service](https://validator.w3.org/), [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/), [JS Hint](https://jshint.com/), and [PEP8 Online](http://pep8online.com/).

* Duplicate attribute ID error was found during W3C Markup Validation. Found within the Add/Edit Product page. This error comes from the custom_clearable_file_input.html file which was part of the Boutique Ado videos. I tried removing #new-image id within custom_clearable_file_input.html and both add/edit.html files' javascript. It removed the error but the change image message disappeared completely. I returned the IDs to how they were and logging the error here.

There were no other reported problems using the HTML CSS, JS, & Python validation services.


***Further insight into the code validation process is documented in an external file located [here.](#)***

</div>

---

## :memo: **OTHER** <a name="other"></a>

<div align="justify">

### **IMAGE SIZE REDUCTION** <a name="size"></a>

* Much care was taken to reduce the image size of all images used in the Florescence Flowers website. All images were reduced in size using the [Tiny PNG](https://tinypng.com/) service.

### **SPELLING & GRAMMAR** <a name="spell"></a>

All of Florescence Flowers's textual content, including this Readme file, has been run through [Grammarly](https://www.grammarly.com) to check for any spelling and grammar mistakes.

</div>

---

***This document is for educational use***

---

[:arrow_up: Return to top?](#top)