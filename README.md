# GeekVerse

GeekVerse is an online B2C e-commerce store catering to users with an interest in geek merchandise, offering a diverse range from clothing to collectibles.

Users have the ability to browse and purchase a variety of products, add them to their wishlist, and contact support via the help center form.

The payment system implemented utilizes Stripe. It's crucial to emphasize that this website is designed for educational purposes only, and users are strongly advised not to enter any personal credit/debit card details when interacting with the site.

For testing purposes, a set of test card details can be used. A comprehensive list of these details can be accessed in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The link to the store can be found here - [GeekVerse](https://geek-verse-d354d8f466c1.herokuapp.com/).

![Site Mockup](https://media.discordapp.net/attachments/1158735657443786843/1158735756374855720/image.png)

## User Experience (UX)

A typical visitor to GeekVerse is likely to be an adult with a keen interest in purchasing geeky merchandise.

### User Stories

#### EPIC | Website Foundation and Core Features

- As a fan of geek culture, I want to easily explore a wide range of clothing and merchandise options.
- As a shopper, I want detailed product information to make informed decisions.
- As a customer, I want to express my fandom by wearing unique and creative designs.
- As a regular customer, I want to have an account for easy shopping and order tracking.

#### EPIC | Enhancing Shopping Experience and Promotions

- As a shopper, I want to easily manage my selected items in a shopping cart, see the total cost, and proceed to checkout when I'm ready to make a purchase.
- As a shopper, I want to create a wishlist of items I'm interested in purchasing in the future. This feature will allow me to easily keep track of products I like, monitor their availability, and seamlessly move them to my shopping cart when I decide to make a purchase.

#### EPIC | Streamlined Checkout and Customer Support

- As a customer, I want a seamless and secure checkout experience.
- As a fan of specific franchises, I want to easily find merchandise related to my favorite franchises.
- As a shopper, I want to stay updated on new arrivals and restocks.
- As a customer, I want to have convenient and reliable customer support options.

#### User stories not yet implemented

- As a potential buyer, I want to see reviews and ratings from other customers.
- As a shopper, I want to benefit from discounts and promotions.

### Design

I adhered to the black and white theme of Boutique Ado for the design of the website, appreciating its simplicity. However, I opted to deviate from the sharp corners in certain areas by adjusting the style to better suit my preferences.

#### Colour Scheme

Colour palette from Coolors

![Colour Scheme](https://cdn.discordapp.com/attachments/1158735657443786843/1158737800049475694/image.png)

The logo for the website features vibrant colors.

The colour scheme of the site is mainly white/grey. The colours chosen are quite neutral in order to showcase the products with minimal distraction.

Great care was taken to establish a good contrast between background colours and text at all times to ensure maximum user accessibility.

#### Imagery

The "GEEK" portion of the logo incorporates Anakin Skywalker as a background, while the "VERSE" section is represented by Yoda, creating a visually appealing and thematic design.

The home page showcases a carousel with five images, each dedicated to a specific brand, along with an additional one encompassing all brands. These images were carefully selected and edited by my partner, [Hanna Kronberg](https://www.linkedin.com/in/hanna-kronberg-534a2b199/), to enhance the visual appeal of the website.

#### Fonts

The primary font used for the body of the website is Roboto Slab, which has been imported from Google Fonts. In the event that, for any reason, the main font isn't imported correctly into the site, Sans Serif serves as the backup font.

#### Wireframes

<details>

<summary>Cart</summary>

![Cart]()
</details>

<details>

<summary>Checkout</summary>

![Checkout]()
</details>

<details>

<summary>Checkout Success</summary>

![Checkout Success]()
</details>

<details>

<summary>Help Center Answer</summary>

![Help Center Answer]()
</details>

<details>

<summary>Help Center Delete Question</summary>

![Help Center Delete Question]()
</details>

<details>

<summary>Help Center Dashboard</summary>

![Help Center Dashboard]()
</details>

<details>

<summary>Help Center</summary>

![Help Center]()
</details>

<details>

<summary>Help Center Question Detail</summary>

![Help Center Question Detail]()
</details>

<details>

<summary>Help Center Question Submitted</summary>

![Help Center Question Submitted]()
</details>

<details>

<summary>Home</summary>

![Home]()
</details>

<details>

<summary>Prodcuts Add Product</summary>

![Prodcuts Add Product]()
</details>

<details>

<summary>Products Delete Product</summary>

![Products Delete Product]()
</details>

<details>

<summary>Products Edit Product</summary>

![Products Edit Product]()
</details>

<details>

<summary>Products Product Detail</summary>

![Products Product Detail]()
</details>

<details>

<summary>Products</summary>

![Products]()
</details>

<details>

<summary>Profiles My Question Detail</summary>

![Profiles My Question Detail]()
</details>

<details>

<summary>Profiles My Questions</summary>

![Profiles My Questions]()
</details>

<details>

<summary>Profile</summary>

![Profile]()
</details>

<details>

<summary>Wishlist</summary>

![Wishlist]()
</details>

## Agile Methodology

GitHub Projects was employed to manage the development process, following an agile approach. You can find the project board and details by following this [link](https://github.com/users/KaiLangen96/projects/7).

The above mentioned epics were documented on the GitHub project as milestones. For each user story, a corresponding GitHub Issue was created, and it was then assigned to a milestone (epic). To ensure clarity on the completion of each user story, defined acceptance criteria were established. These acceptance criteria were further detailed into tasks, streamlining the execution of the user story.

## Database Schema

Two relational databases were utilized in the development of this site. SQLite was employed during production, and [ElephantSQL](https://www.elephantsql.com/) was implemented for the deployed Heroku version. Here is a visual representation of the relationships between the database models:

![Database Schema](https://cdn.discordapp.com/attachments/1158735657443786843/1158827242487550064/image.png?)

## Security Features and Defensive Design

### User Authentication

I've implemented function-based views in Django, incorporating the login_required decorators to control access as needed. If a user attempts to access a forbidden page, a PermissionDenied exception is triggered.

### Form Validation

In the event of incorrect or empty data being entered into a form, the form will not submit. Instead, a warning message will be displayed to the user, indicating which field raised the error.

### Database Security

The database URL and secret key, along with Stripe keys and webhook secret, are securely stored in the env.py file to mitigate the risk of unwanted connections to the database. Additionally, to enhance security, Cross-Site Request Forgery (CSRF) tokens have been implemented on all forms across the site.

### Custom error pages

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

400 Bad Request - GeekVerse is unable to handle this request.

403 Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.

404 Not Found - The page you're looking for doesn't exist. Return to the home page below.

500 Internal Server Error - GeekVerse is currently unable to handle this request.

## Features

### Header

![header](https://cdn.discordapp.com/attachments/1158735657443786843/1158799420666675231/image.png?)

#### Logo

- My partner, [Hanna Kronberg](https://www.linkedin.com/in/hanna-kronberg-534a2b199/), crafted a personalized logo for the website.

- The logo is strategically placed in the top-left corner of the navigation bar and serves as a clickable link, directing users to the home page for seamless navigation.

#### Navigation Bar

- The navigation bar is consistently displayed at the top of each page, providing links to access other pages on the website.

#### Search Bar

- The search bar is situated to the right of the navigation bar.
- On smaller screens, the bar initially shifts to the top of the page and subsequently transforms into a search icon. When clicked, it expands into the full search bar.
- A search query matches against text in the product's title or description, presenting the results on the product's page.

#### User Icon

- The User icon in the navigation menu functions as a dropdown, containing links for "Sign up" and "Log in."
- After a user signs in, their username is displayed beneath the user icon.
- The options to "Sign up" or "Log in" are replaced with the "Log out" option after a user logs in.
- Upon signing in, additional options such as 'My Profile,' 'My Wishlist,' and 'My Questions' become accessible within the User dropdown.

![Logged In](https://cdn.discordapp.com/attachments/1158735657443786843/1158799880576307200/image.png?)

- When the superuser signs in, additional options, specifically 'Add Product' and 'Help Center' become accessible within the User dropdown.

![superuser menu](https://cdn.discordapp.com/attachments/1158735657443786843/1158800130640715856/image.png?)

- The navigation bar is entirely responsive, transitioning into a hamburger menu when the screen size is reduced beyond a certain threshold.

#### Cart Icon

![cart](https://cdn.discordapp.com/attachments/1158735657443786843/1158800484623188008/image.png?)

- Positioned on the right side of the navbar, adjacent to the User icon, is the Cart Icon.
- When users add products to their cart, a toast message appears in the top right-hand corner of the screen. This message informs the user about the added item, providing a snapshot of the cart contents and the total cost.
- Clicking the cart icon directs the user to the shopping cart page, where a summary of the added items is displayed.

### Footer

![footer](https://cdn.discordapp.com/attachments/1158735657443786843/1158800591540191242/image.png?)

- The footer is consistently positioned at the bottom of every page.
- Within the footer section, there are links to social media platforms, including Facebook, Instagram, Twitter, and YouTube.
- A newsletter signup area, powered by Mailchimp, allows users to enter their email address for subscription to the mailing list.
- The Quick Links section offers easy access to key parts of the site, such as 'All Products,' 'Help Center,' 'Special Offers,' 'Privacy Policy,' and 'Terms of Service.'
- On the right side of the footer, the available payment methods are displayed. Research on the payment methods accepted by [Stripe](https://stripe.com/docs/payments/payment-methods/overview) informed this selection.
- To prevent users from navigating away from the site, clicking on any external links will open the respective website in another tab.

### Home Page

#### Call to Action Section

![Home page](https://cdn.discordapp.com/attachments/1158735657443786843/1158800967739904030/image.png?)

- The home page features a prominent call-to-action section that showcases a carousel of the available brands on the website.
- Clicking on the brand images within the carousel directs the user to the corresponding products categorized by the brand.
- Moreover, a New Arrivals Section has been integrated to showcase the latest additions. This section exhibits up to six of the newest arrivals for user visibility, along with a button that directs users to the products page filtered specifically by new arrivals.

### User Account Pages

#### Sign Up

![Sign Up](https://cdn.discordapp.com/attachments/1158735657443786843/1158801296481075370/image.png?)

#### Sign In

![Sign In](https://cdn.discordapp.com/attachments/1158735657443786843/1158801355037753354/image.png?)

#### Sign Out

![Sign Out](https://cdn.discordapp.com/attachments/1158735657443786843/1158801417016987658/image.png?)

- The Sign up, Log in, and Log out functionality on the website was implemented using Django allauth.
- Success messages are displayed to inform users about successful login or logout actions.
- During the account sign-up process, users are required to verify their email address by clicking on the authentication link sent to the provided email.
- For users who forget their password, a 'Forgot Password' link on the login page allows them to initiate a password reset process.

### Profile

![Profile Page](https://cdn.discordapp.com/attachments/1158735657443786843/1158801790133878914/image.png?)

#### Delivery Details

![Delivery Details](https://cdn.discordapp.com/attachments/1158735657443786843/1158801816281153627/image.png?)

- The delivery details section securely stores the user's delivery address and phone number.
- This stored information is utilized to automatically populate the delivery address field when the user is placing an order, streamlining the checkout process.
- If a user desires, they have the option to submit the fields on this page empty, allowing them to remove their details in this manner.

#### Order History

![Order History](https://cdn.discordapp.com/attachments/1158735657443786843/1158801847826534471/image.png?)

- The order history section presents a comprehensive list of every order the user has placed.
- Within the table, information such as the order number, order date, and the total cost is displayed for each order.
- Clicking on the order number provides a direct link to a summary page containing detailed information about that specific order.

#### My Questions

![My Qeestions](https://cdn.discordapp.com/attachments/1158735657443786843/1158802134586904729/image.png?)

- The page showcases a table containing a list of all the questions submitted by the user.
- Users have the option to click on "View" to access detailed information about a specific question.
- Additionally, users can click on "Delete" to remove a question directly from this interface.

#### My Question Detail

![My Question Detail](https://cdn.discordapp.com/attachments/1158735657443786843/1158802284227080234/image.png?)

- The page provides in-depth details for a specific question, including any associated answers if the question has been addressed.
- Users have the option to delete their questions directly from this page or navigate back to the "My Questions" section for a broader view.

### Products

![all products](https://cdn.discordapp.com/attachments/1158735657443786843/1158802430474076221/image.png?)

- When clicking the 'All Products' dropdown in the navbar the dropdown menu will show all the different sorting options.
- The 'All Products' link will display a list of all products from the database.

![Sorting](https://cdn.discordapp.com/attachments/1158735657443786843/1158802554604507226/image.png?)

- Clicking any of the sorting options will filter the products by the sorting option selected.

![products](https://cdn.discordapp.com/attachments/1158735657443786843/1158802723597205574/image.png?)

- Each product card on the page features an image of the product, along with its name, price, categories, and rating.
- If the user is a superuser, additional options such as edit and delete buttons are displayed for each product.
- The products page is designed to be fully responsive, dynamically adjusting the number of products displayed in each row based on the user's screen size.
- A sort box is conveniently placed on the products page, enabling users to organize all products by price or rating in ascending or descending order, as well as by title (A-Z).

![sort box](https://cdn.discordapp.com/attachments/1158735657443786843/1158802866069327994/image.png?)

### Product Detail

![Product Detail](https://cdn.discordapp.com/attachments/1158735657443786843/1158802977721692170/image.png?)

- Clicking on an individual product card directs the user to the full product details page.
- The link is implemented as a Bootstrap stretched link, allowing users to click anywhere on the card.
- The product detail page showcases essential information, including the product image, name, price, categories, rating, and a description.
- If the user is a superuser, additional functionalities such as edit and delete buttons are displayed.
- Quantity buttons are positioned beneath the product details, allowing users to adjust the quantity they wish to add to the cart.
- The plus and minus buttons facilitate an increase or decrease in the input value, with the minus button disabled when the value is 1 and the plus button disabled when the value is 49.
- If a user manually enters a negative number, 0 or a value greater than 49 and clicks anywhere on the page, the quantity automatically adjusts to 49 or 1.
- Clicking the 'Add to Cart' button adds the specified quantity of products to the cart.
- If a user attempts to add an item more than 49 times by adding it twice, they receive a notification stating that the maximum quantity in a single order is 49.
- Clicking the 'Keep Shopping' button redirects the user back to the store.

#### Add Product

![add product](https://cdn.discordapp.com/attachments/1158735657443786843/1158803080108834946/image.png?)

- The "Add Product" page is accessible to superusers through the 'Add Product' button in the user dropdown menu.
- If a non-superuser attempts to access the add product page (via URL modification), they are redirected to a custom 403 page with a message explaining that only store owners can add products.
- Superusers are required to complete all fields marked with an asterisk on the form. If any of these mandatory fields are left blank or contain only whitespace, an error message appears above the respective field, notifying the user of the issue.
- If a price with more than 6 digits is entered, the form will fail, and an error message will be displayed under the price field.
- Users have the option to upload a photo; if they choose not to, a default image will be displayed as the product image.
- Clicking the 'Add Product' button at the bottom of the form will create the product, provided there are no errors. Users will receive a success message, confirming that the product has been added successfully, and will be redirected to the product details page.

#### Edit Product

![edit product](https://cdn.discordapp.com/attachments/1158735657443786843/1158803227698016358/image.png?)

- Superusers have the option to edit a product by clicking the edit button on the product card or on the product detail page.
- The form opens with all fields prepopulated with the original content.
- The image field displays a thumbnail of the existing image and provides a checkbox option to remove it. Checking this checkbox will replace the image with the default image.
- If a non-superuser attempts to edit a product (via URL modification), they are redirected to a custom 403 page.
- Upon successful completion of the edit, the superuser receives a success message, confirming that the product has been updated successfully.

#### Delete Product

![delete product](https://cdn.discordapp.com/attachments/1158735657443786843/1158803403485478912/image.png?)

- Superusers have the option to delete a product by clicking the delete button on the product card or on the product detail page.
- A confirmation page appears, asking the superuser to confirm the deletion or cancel the operation.
- Upon successful deletion, the superuser receives a success message, confirming that the product has been deleted successfully.

### Cart

![shopping cart](https://cdn.discordapp.com/attachments/1158735657443786843/1158803728061702164/image.png?)

- Clicking on the shopping cart icon in the navigation bar redirects the user to the shopping cart page.
- On this page, the user can view the products they have added to their cart, along with details such as unit price, quantity, and subtotal for each item.
- Users can click on the product name to navigate directly to that product's detail page for more information.

#### Quantity Buttons

![Quantity buttons](https://cdn.discordapp.com/attachments/1158735657443786843/1158804346708971570/image.png?)

- The quantity input box on the shopping cart page displays the product quantity that the user has added to their cart.
- The plus and minus buttons associated with the input box allow users to increase or decrease the quantity value.
- The minus button is disabled when the quantity is set to 1, and the plus button is disabled when the quantity is set to 99, respecting the set limits.
- If a user manually enters a negative number, 0 or a value greater than 49 and clicks anywhere on the page, the quantity automatically adjusts to 49 or 1.

#### Update and Remove Buttons

![Update Delete buttons](https://cdn.discordapp.com/attachments/1158735657443786843/1158803909784121384/image.png?)

- Clicking the 'Update' button on the shopping cart page saves any changes made to the quantity and updates the item's subtotal accordingly.
- Additionally, clicking the 'Remove' icon button permanently removes the item from the user's cart.

#### Total Section

![Total section](https://cdn.discordapp.com/attachments/1158735657443786843/1158804097269514321/image.png?)

- At the end of the line items on the shopping cart page, there is a comprehensive summary of costs.
- The summary includes the total cost of the items in the cart, the delivery cost, and the grand total to be paid.
- Below the grand total, users will find a message indicating how much more they need to spend to qualify for free delivery, if they haven't met the free delivery threshold of $100.
- Beneath this information, there are two buttons. Users can proceed to checkout or return to the products page by clicking 'Continue Shopping.'

### Checkout

![checkout](https://cdn.discordapp.com/attachments/1158735657443786843/1158804464623419402/image.png?)

#### Details

- In the details section of the checkout process, users can input their contact details, delivery address, and card number.
- For guests, a link to create an account or log in is presented.
- If the user is signed in, a checkbox option allows them to save the delivery information. If delivery information is already saved, it is automatically filled in.
- If any required field is left empty, contains only whitespace, or includes text in the phone number field, an error message will prompt the user to 'Fill in the field' or 'match the format requested'.

#### Order Summary

- The order summary section provides a comprehensive list of all items about to be purchased, including quantity, subtotal, and a grand total.
- Next to the order summary title is a numerical indicator reflecting the total number of items included in the order.
- Users can click on the product image within the summary to navigate directly to that product's detail page for more information.

#### Payment

- Stripe handles the card payment process to ensure a secure transaction.
- Incorrect card numbers automatically trigger an invalid card number error.
- A loading screen appears during payment processing to prevent users from navigating away.
- A warning message at the bottom of the page informs the user of the amount their card is about to be charged.
- Even if the payment form doesn't submit correctly or the user closes the browser during the wait animation, the order is still created in the database through the webhook.
- After payment processing, the webhook searches the database to confirm the existence of the order. If it cannot find it, it will create one using the payment information.

#### Checkout Success

![checkout success](https://cdn.discordapp.com/attachments/1158735657443786843/1158804736179437598/image.png?)

- Upon successful order processing, the user is directed to the checkout success page, providing a summary of the completed order.
- Additionally, an email containing the order confirmation is sent to the user.
- At the end of the order summary, a 'Continue Shopping' button is available, allowing the user to return to the products page.

### Wishlist

![wishlist](https://cdn.discordapp.com/attachments/1158735657443786843/1158804936121913374/image.png?)

- The wishlist page showcases the products that the user has added to their wishlist.
- Each product entry includes a 'Remove' button, allowing the user to easily remove items from their wishlist.
- Upon successfully removing a product from the wishlist, the user receives a success message.
- The product name serves as a link, redirecting the user to the detailed information page for each product.
- A 'Keep Shopping' button is provided, linking to the page displaying all available products for further exploration.

### Help Center

![help center](https://cdn.discordapp.com/attachments/1158735657443786843/1158805092045176932/image.png?)

- Users can access the question form by clicking on the "Help Center" link located in the footer.
- To access the form, users need to be logged in or will be redirected to the login page.
- The form includes the user as "author", a drop-down menu allowing users to select a category for their question, providing clarity to the site owner about the nature of the inquiry and the 'Your Question' text field.
- The 'Your question' field must be filled out. If the form is submitted with this field left blank or containing only whitespace, an error message will appear, notifying the user of the issue.
- Upon form submission, the user is redirected to a page where they can review the submitted question.
- The submitted question is now added to their 'My Questions' page, where the user can track and review questions, including any answers if the question has been addressed.

#### Help Center Dashboard

![help center dashboard](https://cdn.discordapp.com/attachments/1158735657443786843/1158805228288749649/image.png?)

- When the site owner is logged in, the 'Help Center' option appears in the User drop-down menu.
- When the site owner navigates to the Help Center Dashboard page they can see a list of user questions sorted by question number.
- From here site owner can view or delete questions.

#### Help Center Question Detail

![help center question detail](https://cdn.discordapp.com/attachments/1158735657443786843/1158805327723114538/image.png?)

- The page displays detailed information about a specific question, including any provided answers.
- Three buttons are available, leading users to different actions:
  - 'Back to Dashboard' directs users back to the help center dashboard.
  - 'Answer Form' takes users to a form where they can provide an answer.
  - 'Delete Confirmation' leads to a confirmation page if the user wishes to delete the question.

#### Help Center Answer

![help center answer](https://cdn.discordapp.com/attachments/1158735657443786843/1158805433490874489/image.png?)

- The page displays the question along with a form for answering.
- The form includes a locked responder field indicating the logged-in superuser and a required answer text field.
- Two buttons are available:
  - 'Back to Dashboard' directs users back to the main dashboard.
  - 'Submit Answer' allows users to submit their answer.

#### Help Center Delete Question

![help center delete](https://cdn.discordapp.com/attachments/1158735657443786843/1158805621408288878/image.png?)

- Superusers or question owners have the option to delete a question by clicking the delete button on the help center dashboard.
- A confirmation page appears, asking the superuser to confirm the deletion or cancel the operation.
- Upon successful deletion, the superuser receives a success message, confirming that the product has been deleted successfully.

### Error Pages

Custom error pages have been crafted to provide users with more detailed information about encountered errors and guide them back to the site.

![404 error](https://cdn.discordapp.com/attachments/1158735657443786843/1158805878112272477/image.png?)

- 400 Bad Request - Fresh Nest is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - Due to an internal error we are unable to process this request.

## Business Model

## Marketing Strategy

### SEO

#### Keywords

![Keywords]()

#### External Links

#### Building Trust

The page footer incorporates links to the privacy policy, providing users with information about how their data is collected and processed, and the terms of service. Clicking on these links opens modals. Users can close the modals either by clicking the 'x' span at the top of the modal or by clicking anywhere outside the modal.

#### Sitemap and robots.txt

A sitemap file, listing important page URLs, was generated to enhance search engine understanding of the site's structure and facilitate navigation. The sitemap was created using xml-sitemaps.com.

Additionally, a robots.txt file was crafted to guide search engines on areas they are not allowed to access on the website. This practice contributes to improved SEO by enhancing the overall quality of the site.

### Content marketing

### Social Media Marketing

A Facebook business page has been established for organic social media marketing in conjunction with the main site. This platform serves as an effective channel for sharing updates about new product arrivals, complementing the content marketing strategy of the website.

![Facebook Page](https://cdn.discordapp.com/attachments/1158735657443786843/1158785376807305348/image.png)

### Email Marketing

Visitors to the site have the option to sign up for the newsletter without the need for an account. A signup box is conveniently placed in the footer of the site. This feature enables the business to share news, updates, and special offers, including information about new products. The newsletter service is implemented using Mailchimp.

## Testing

Testing and results can be found [here](/TESTING.md)

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App

- Sign in to [Heroku](https://dashboard.heroku.com/apps) or sign up if you don't have an account.
- Once on the main page, locate and click the "New" button at the top right. From the dropdown, choose "Create New App."
- Provide a unique and relevant name for your app.
- Choose your preferred region.
- Finally, click on the "Create App" button to complete the process.

### Attach the Postgres database

- Navigate to the Resources tab, and under add-ons, enter "Postgres" and choose the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Return to your IDE and install two additional requirements:
  - Run pip3 install `dj_database_url`
  - Run pip3 install `psycopg2-binary`
- Generate a requirements.txt file by entering `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the `env.py` file.
- In the `settings.py` file, import dj_database_url, comment out the default configurations within the database settings, and include the following:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

- Execute migrations and establish a superuser for the new database.
- Introduce an if statement in `settings.py` to execute the PostgreSQL database when utilizing the app on Heroku, or SQLite if otherwise.

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

- Create a file named "Procfile" in the main directory and include the following: `web: gunicorn project-name.wsgi:application`
- Include Heroku in the ALLOWED_HOSTS list in `settings.py` in the format ['app_name.heroku.com', 'localhost']
- Push these modifications to GitHub.

### Update Heroku Config Vars

Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                              |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                              |
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
| USE_AWS               | True (when AWS set up - instructions below)                                   |

### Deploy

- Note: Ensure that in Django settings, DEBUG is set to False.
- Navigate to the deploy tab on Heroku and establish a connection to GitHub, selecting the necessary repository.
- Scroll to the bottom of the deploy page and either click "Enable Automatic Deploys" for automatic deployments or "Deploy Branch" for manual deployments. Manually deployed branches require redeployment each time the repository is updated.
- Click "View" to observe the live and operational site.

The site is now accessible and functional.

## AWS Set Up

### AWS S3 Bucket

- Set up an AWS account.
- Navigate to the AWS Management Console's 'Services' tab, search for 'S3', and select it.
- Click 'Create a new bucket', assign it a name (matching your Heroku app name if possible), and choose the region closest to you.
- Under 'Object Ownership', choose 'ACLs enabled' and leave the Object Ownership as 'Bucket owner preferred'.
- Uncheck 'block all public access' and confirm that the bucket will be public.
- Click 'Create bucket'.
- Access the created bucket, go to the 'Properties' tab, and scroll down. Under 'Static website hosting', click 'edit', enable the Static website hosting option, copy the default values for the index and error documents, and click 'save changes'.
- Move to the 'Permissions' tab, find the CORS configuration section, and add the following code:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Within the 'Bucket Policy' section, select 'Policy Generator'.
- Opt for 'S3 Bucket Policy' from the type dropdown.
- In 'Step 2: Add Statements', incorporate the following settings:
  - Effect: Allow
  - Principal: *
  - Actions: GetObject
  - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the appearing popup.
- Paste the generated policy into the Permissions > Bucket Policy area.
- Append '/*' at the end of the 'Resource' key and save.
- Proceed to the 'Access Control List' section, click edit, enable List for Everyone (public access), and confirm the warning.

### IAM

- In the 'Services' menu, search for IAM and select it.
- On the IAM page, click 'User Groups' in the sidebar, then select 'Create group'. Assign a name and click 'Create'.
- Move to 'Policies', click 'Create New Policy', and go to the 'JSON' tab. Select 'Import Managed Policy'.
- Search for 'S3' and choose 'AmazonS3FullAccess'. Click 'Import'.
- Retrieve the bucket ARN from 'S3 Permissions' as mentioned above.
- Remove the '*' from the 'Resource' key and insert the following code into the area:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```

- Proceed to 'Next Tags' > 'Next Review' and then provide a name and description before clicking 'Create Policy'.
- Navigate to 'User Groups', open the created group, go to the 'Permissions' tab, and click 'Add Permissions', followed by 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You now need to generate a user for the group. Select 'users' from the sidebar and click 'Add user'.
- Assign a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you created.
- Continue clicking 'Next' until you reach the 'Create user' button and click it.
- Download the CSV file containing the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID, essential for the Heroku variables as mentioned above and in your env.py.

### Connecting S3 to Django

- Return to your IDE and install 2 additional requirements:
  - `pip3 install boto3`
  - `pip3 install django-storages`
- Update your requirements.txt file using `pip3 freeze --local > requirements.txt` and include storages in your installed apps.
- Introduce an if statement in `settings.py`

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

```

- Subsequently, insert the line
  - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to specify to Django the location of our static files in production.
- Generate a file named 'custom_storages' and import both our settings from django.con and the s3boto3 storage class from django storages.
- Establish the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- Within `settings.py`, append the following inside the if statement:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

- Additionally, insert the following at the beginning of the if statement:

```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

- Navigate to S3, access your bucket, and select 'Create folder'. Label the folder 'media' and click 'Save'.
- Within the folder, choose 'Upload', 'Add files', and then pick all the images used for your site.
- Under 'Permissions', choose 'Grant public-read access' and click upload.
- Django should automatically link your static files and media files to your S3 bucket.

## Forking this repository

- Find the repository at this [GeekVerse](https://github.com/KaiLangen96/geek-verse) link.
- At the repository's top, on the right side of the page, click "Fork" among the available buttons.
- You now have a duplicate of the repository.

## Cloning this repository

To clone this repository, follow the steps below:

1. Find the repository at this [GeekVerse](https://github.com/KaiLangen96/geek-verse) link.
2. Under **Code**, you'll see various cloning options: HTTPS, SSH, and GitHub CLI. Click on your preferred cloning option, and then copy the provided link.
3. Open your **Terminal**.
4. In the Terminal, navigate to the location where you want to create the local clone.
5. Type **'git clone'**, and then paste the URL copied from GitHub.
6. Type **'Enter'** to create the local clone.

## Languages

- HTML5
- CSS3
- Javascript
- Python

## Frameworks - Libraries - Programs Used

- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Authentication library used to create the user accounts
- [JQuery](https://jquery.com/)
- [PostgreSQL](https://www.postgresql.org/): Used as the database for this project.
- [SQLite](https://www.sqlite.org/index.html): Used as the database during production.
- [Stripe](https://stripe.com/ie): Used for the payments system.
- [AWS](https://aws.amazon.com/?nc2=h_lg): Used for file storage.
- [Heroku](https://dashboard.heroku.com/login): Used as the cloud based platform to deploy the site on.
- [Balsamiq](https://balsamiq.com/): Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/): Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/): Used for icons.
- [GitHub](https://github.com/): Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/): Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/): Used for HTML & CSS Validation.
- [Jshint](https://jshint.com/): Used to validate javascript
- [Coolors](https://coolors.co/): Used to create colour palette.
- [Favicon](https://favicon.io/): Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard): Used to create the database schema design
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Used to manage Django Forms
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling
- [Sitemap Generator](www.xml-sitemaps.com): Used to create sitemap.xml
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/): Used to create the site's privacy policy
- [Terms of Service Generator](https://www.termsofservicegenerator.net/): Used to create the site's terms of service.
- [Mailchimp](https://mailchimp.com/?currency=EUR): Used to create the newsletter signup functionality.

## Credits

### Media

- The logo and carousel images have been edited for my purpose by my partner [Hanna Kronberg](https://www.linkedin.com/in/hanna-kronberg-534a2b199/).
- Here are all original pictures:
  - [Marvel](https://cdn.wallpapersafari.com/23/69/hi3v6Y.jpg)
  - [DC-Comics](https://wall.alphacoders.com/big.php?i=241901)
  - [Star Wars](https://www.amazon.com/Open-Road-Brands-Disney-Collage/dp/B08V5MFV55?th=1)
  - [Harry Potter](https://wallpaper.dog/harry-potter-1920x1080-wallpapers)
  - All Brands
    - [Marvel](https://www.amazon.com/Trends-International-Marvel-Poster-22-375/dp/B06VW7GXKP)
    - [DC-Comics](https://www.europosters.se/poster/dc-comics-collage-v20290)
    - [Star Wars](https://artofthemovies.co.uk/products/star-wars-1977-ukquad-stylec-preawards-chantrell-01)
    - [Harry Potter](https://www.abystyle.com/en/harry-potter/5949-harry-potter-poster-deathly-hallows-915x61cm-5028486151653.html)

### Content

- All products are taken from official stores.
  - [Marvel](https://www.shopdisney.com/marvel-content/)
  - [DC-Comics](https://shop.warnerbros.co.uk/pages/dc)
  - [Star Wars](https://www.shopdisney.com/franchises/star-wars/)
  - [Harry Potter](https://harrypottershop.co.uk/)
  
- I do not sell any of these products. All information is gathered from those sources.

## Special Thanks

[Code Institude](https://codeinstitute.net/), for teaching me the languages needed to create this page.

[w3schools](https://www.w3schools.com/), for so many helpful pages and tools to support learning the languages.

[Django](https://docs.djangoproject.com/en/4.0/) and [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) docs, for a lot of helpful information.

[Stack Overflow](https://stackoverflow.com/), for a lot of help, especially regarding bug fixes.

[Hanna Kronberg](https://www.linkedin.com/in/hanna-kronberg-534a2b199/), for huge help with the design of the website.

[Antonio Rodríguez](https://www.linkedin.com/in/antonio-rodr%C3%ADguez-bb9b99b7/), as my mentor. Once again, he helped me a lot with getting started with the recipe website and creating the ERD.
