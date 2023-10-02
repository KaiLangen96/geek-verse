# Testing

- [Testing](#testing)
  - [Validator Testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JSHINT](#jshint)
    - [Python Validation - Pycodestyle](#python-validation---pycodestyle)
    - [Lighthouse](#lighthouse)
  - [Device Testing](#device-testing)
  - [Browser Testing](#browser-testing)
  - [Manual Testing](#manual-testing)
    - [Site Navigation](#site-navigation)
    - [All Auth Pages](#all-auth-pages)
    - [Pages](#pages)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)

[Table of contents generated with markdown-toc](http://ecotrust-canada.github.io/markdown-toc/)

## Validator Testing

### HTML

All HTML pages underwent validation using the [W3C HTML Validator](https://validator.w3.org/). The results are displayed in the table below.

| Page                           | Logged Out | Logged In  |
|--------------------------------|------------|------------|
| Cart                           | No Errors  | No Errors  |
| Checkout                       | No Errors  | No Errors  |
| Checkout Success               | No Errors  | No Errors  |
| Help Center Answer             | N/A        | No Errors  |
| Help Center Delete Question    | N/A        | No Errors  |
| Help Center Dashboard          | N/A        | No Errors  |
| Help Center                    | N/A        | No Errors  |
| Help Center Question Detail    | N/A        | No Errors  |
| Help Center Question Submitted | N/A        | No Errors  |
| Home                           | No Errors  | No Errors  |
| Products Add Product           | N/A        | [Error](https://media.discordapp.net/attachments/1157660609073127524/1157684097565597818/image.png?ex=651b7b15&is=651a2995&hm=47c2b6651da0cd416029900010dcbc2bc2ca503702b1e778ca97abd6380e9737&=&width=709&height=676)  |
| Products Delete Product        | N/A        | No Errors  |
| Products Edit Product          | N/A        | [Error](https://media.discordapp.net/attachments/1157660609073127524/1157684738153271368/image.png?ex=651b7bae&is=651a2a2e&hm=b221dc962c605699e7e5c9c145ed4f6849d33efd1135f491a7c810a47092283b&=&width=710&height=676)  |
| Products Product Detail        | No Errors  | No Errors  |
| Products                       | No Errors  | No Errors  |
| Profiles My Question Detail    | N/A        | No Errors  |
| Profiles My Questions          | N/A        | No Errors  |
| Profile                        | N/A        | No Errors  |
| All Auth Login                 | No Errors  | No Errors  |
| All Auth Logout                | N/A        | No Errors  |
| All Auth Password Reset Done   | N/A        | No Errors  |
| All Auth Password Reset        | No Errors  | No Errors  |
| All Auth Sign Up               | No Errors  | No Errors  |
| All Auth Verification Sent     | N/A        | No Errors  |
| Wishlist                       | N/A        | No Errors  |
| 400.html                       | Not tested | Not tested |
| 403.html                       | Not tested | Not tested |
| 404.html                       | No errors  | Not tested |
| 500.html                       | Not tested | Not tested |

Note: I haven't been able to trigger errors to test all the error pages, but I'm confident that they function correctly. The errors received are tied to custom_clearable_file_input.html, and making changes to the [code](https://media.discordapp.net/attachments/1157660609073127524/1157684097292972144/image.png?ex=651b7b15&is=651a2995&hm=d62e15dc272349dfdce53c72ae9185514900e4779f104b3bd4fe791a57c54cf2&=) would lead to the field breaking. This problem is specifically linked to the custom_clearable_file_input.html line 14 to 16.

### CSS

No errors were found when passing my CSS files through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

*base.css*
![base.ccs validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157711697344209016/image.png?ex=651b94c9&is=651a4349&hm=677dfcd59ec0a083b0429261e35d4e5ce37189bb3bb3ba1907435228579cf9fc&)

*checkout.css*
![checkout.ccs validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157711816739270799/image.png?ex=651b94e6&is=651a4366&hm=b1634994f084a7d18af09d932d31768c93499194f78440dfe2f6126db833f955&)

*profile.css*
![profile.ccs validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157711535527952485/image.png?ex=651b94a3&is=651a4323&hm=262579691142c24ff57835053d3643849aa0f89f1528b336cd8e96481e262e7a&)

### JSHINT

All Javascript snippets were passed through [Jshint](https://jshint.com/) with no errors or warnings.

**Cart**
![Cart JS validation 1/2](https://cdn.discordapp.com/attachments/1157660609073127524/1157713788586430635/image.png?ex=651b96bc&is=651a453c&hm=73b022dc986ada9d7435c38307c21e4f33fc67a8cb227d8ba773e8c3c8c0be98&)
![Cart JS validation 2/2](https://cdn.discordapp.com/attachments/1157660609073127524/1157713974192775298/image.png?ex=651b96e8&is=651a4568&hm=4d83ec67478e75ad157f85239c3c21ce6f2a73c0e67a4f7d24851b1cc97a3742&)

**Image Selector**
![Image Selector JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157714119508639754/image.png?ex=651b970b&is=651a458b&hm=be92e0ab8bbe45903fa8f32a33c0c3ffc75b07d0d47664960c84ac72d1165f4a&)

**Quantity Input**
![Quantity Input JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157715029358039101/image.png?ex=651b97e4&is=651a4664&hm=826f3f963d65749fec322a2fa70f5b2b59fe8bbf13d49046bc9e5acb64a7b503&)

**Sort Selector**
![Sort Selector JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157715259658879116/image.png?ex=651b981b&is=651a469b&hm=af3a7ea01885e87c2e07b2b155f327ed6f34a4a9c39a1bf835d92ec90ad61d82&)

**Back to top - Button**
![Back to top - Button JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157715569496301740/image.png?ex=651b9865&is=651a46e5&hm=5a5a45046eb38acf104baa12d91f31d26fd876cb5dfacf9b04e621a87d9a2b1c&)

**All auth mail function**
![All auth mail function JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157715721162326197/image.png?ex=651b9889&is=651a4709&hm=7178a2a67fea082e50320dfcff81147d9d2e7af3bf804a3b0545db52554aab04&)

**Showing toasts**
![Showing toasts JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157715973537804435/image.png?ex=651b98c5&is=651a4745&hm=fb31852ae40684cd8c668f3210cad1a8f2513e2190250dbe1e3769de9359eb08&)

**Modal script**
![Modal script JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157716996889247865/image.png?ex=651b99b9&is=651a4839&hm=740d75ae31060b3534b59169809e3616444d993052f5dd35214e3fd2e09e070d&)

**Wislist**
![Wishlist JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157717140749692979/image.png?ex=651b99db&is=651a485b&hm=40367f0e41fc11c07d88a52c99b77544731ca541bd49b7d873f0cc5667ea9f64&)

**Countryfield.js**
![Countryfield.js JS validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157718728939679784/image.png?ex=651b9b56&is=651a49d6&hm=9cad0b0c4858c1ec4718d964697f33e642229d358d898f989060fd929dd4926d&)

**Stripe_elements.js**
![Stripe_elements.js validation](https://cdn.discordapp.com/attachments/1157660609073127524/1157720310771101809/image.png?ex=651b9ccf&is=651a4b4f&hm=ed3fe09695bed64c92a1d74bb5fdcfa2ee320fe9745dea78e959716118a87f6e&)

### Python Validation - Pycodestyle

Python testing was conducted utilizing Flake8 to verify the absence of syntax errors. Additionally I used [black](https://pypi.org/project/black/) as a recommendation from my weekly teacher, Kay, to format my code. Then I strategically employed # noqa where necessary, such as in the error handlers or on lines that were not subject to breakpoints. In the end I could run flake8 without any errors or warnings shown.

![Flake8](https://cdn.discordapp.com/attachments/1157660609073127524/1157728346126426122/image.png?ex=651ba44b&is=651a52cb&hm=a79c6761a8d6b13b5f2609fd47fdceb132d1e1842cecba4ad010de61026c8e1a&)

### Lighthouse

Lighthouse validation was run on all pages in order to check accessibility and performance. Many warnings were fixed including 'Background and foreground colours do not have a sufficient contrast ratio' and the below scores were achieved. Error pages such as 404.html were not able to be tested by lighthouse.

**Desktop:**
| Page                           | Performance  | Accessibility | Best Practices  | SEO |
|--------------------------------|:------------:|:-------------:|:---------------:|:---:|
| Cart                           |           97 |           100 |             100 | 100 |
| Checkout                       |           82 |            98 |             100 | 100 |
| Checkout Success               |           87 |           100 |             100 | 100 |
| Help Center Answer             |           87 |           100 |             100 | 100 |
| Help Center Delete Question    |           91 |           100 |             100 | 100 |
| Help Center Dashboard          |           90 |            98 |             100 | 100 |
| Help Center                    |           89 |           100 |             100 | 100 |
| Help Center Question Detail    |           90 |            98 |             100 | 100 |
| Help Center Question Submitted |          N/A |           N/A |             N/A | N/A |
| Home                           |           80 |           100 |             100 | 100 |
| Products Add Product           |           91 |           100 |             100 | 100 |
| Products Delete Product        |           91 |           100 |             100 | 100 |
| Products Edit Product          |           89 |           100 |             100 | 100 |
| Products Product Detail        |           89 |           100 |             100 | 100 |
| Products                       |           69 |           100 |             100 |  90 |
| Profiles My Question Detail    |           89 |            98 |             100 | 100 |
| Profiles My Questions          |           89 |            98 |             100 | 100 |
| Profile                        |           84 |            96 |             100 | 100 |
| All Auth Login                 |           93 |            98 |             100 | 100 |
| All Auth Logout                |           92 |           100 |             100 | 100 |
| All Auth Password Reset Done   |           92 |           100 |             100 | 100 |
| All Auth Password Reset        |           92 |           100 |             100 | 100 |
| All Auth Sign Up               |           92 |            98 |             100 | 100 |
| All Auth Verification Send     |           93 |           100 |             100 | 100 |
| Wishlist                       |           89 |           100 |             100 | 100 |

**Mobile:**
| Page                           | Performance  | Accessibility | Best Practices  | SEO |
|--------------------------------|:------------:|:-------------:|:---------------:|:---:|
| Cart                           |           75 |           100 |             100 | 100 |
| Checkout                       |           68 |            98 |             100 | 100 |
| Checkout Success               |           72 |           100 |             100 | 100 |
| Help Center Answer             |           73 |           100 |             100 | 100 |
| Help Center Delete Question    |           76 |           100 |             100 | 100 |
| Help Center Dashboard          |           74 |            98 |             100 | 100 |
| Help Center                    |           74 |           100 |             100 | 100 |
| Help Center Question Detail    |           74 |            98 |             100 | 100 |
| Help Center Question Submitted |          N/A |           N/A |             N/A | N/A |
| Home                           |           48 |           100 |             100 | 100 |
| Products Add Product           |           76 |           100 |             100 | 100 |
| Products Delete Product        |           75 |           100 |             100 | 100 |
| Products Edit Product          |           74 |           100 |             100 | 100 |
| Products Product Detail        |           56 |           100 |             100 | 100 |
| Products                       |           60 |           100 |             100 |  89 |
| Profiles My Question Detail    |           75 |            98 |             100 | 100 |
| Profiles My Questions          |           75 |            98 |             100 | 100 |
| Profile                        |           69 |            96 |             100 | 100 |
| All Auth Login                 |           71 |            98 |             100 | 100 |
| All Auth Logout                |           76 |           100 |             100 | 100 |
| All Auth Password Reset Done   |           76 |           100 |             100 | 100 |
| All Auth Password Reset        |           76 |           100 |             100 | 100 |
| All Auth Sign Up               |           76 |            98 |             100 | 100 |
| All Auth Verification Send     |           77 |           100 |             100 | 100 |
| Wishlist                       |           75 |           100 |             100 | 100 |

## Device Testing

The website underwent testing on a range of devices, including Desktop, Samsung Galaxy S22, and Huawei P20 lite, to ensure responsiveness across different screen sizes in both portrait and landscape modes. The website functioned according to its intended design. Additionally, responsive design was verified using Chrome developer tools on various devices, confirming the structural integrity held for different sizes.

## Browser Testing

The website underwent testing on Google Chrome, Firefox, Edge, and Opera browsers, with no issues identified.

## Manual Testing

### Site Navigation

**NavBar:**
| Element                          | Action                      | Expected Result                                             | Pass/Fail |
|----------------------------------|-----------------------------|-------------------------------------------------------------|-----------|
| Logo                             | Click                       | Redirect to home                                            | Pass      |
| Search Box Function              | Click Search                | Error message displays                                      | Pass      |
| Search Box Function              | Enter Text and Click Search | Search both the product's title and description for a match | Pass      |
| My Account Dropdown              | Click                       | Open profile dropdown                                       | Pass      |
| Sign Up Link                     | Click                       | Redirect to Sign Up page                                    | Pass      |
|                                  | Display                     | (Not visible if user in session)                            | Pass      |
| Login Link                       | Click                       | Redirect to login page                                      | Pass      |
|                                  | Display                     | (Not visible if user in session)                            | Pass      |
| Add Product Link                 | Click                       | Redirect to add_product page                                | Pass      |
|                                  | Display                     | (Only visible if superuser in session)                      | Pass      |
| Help Center                      | Click                       | Redirect to help_center_dashboard page                      | Pass      |
|                                  | Display                     | (Only visible if superuser in session)                      | Pass      |
| My Profile Link                  | Click                       | Redirect to user profile page                               | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| My Wishlist Link                 | Click                       | Redirect to user wishlist page                              | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| My Questions Link                | Click                       | Redirect to user questions page                             | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| Logout Link                      | Click                       | Redirect to logout confirm page                             | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| Cart Link                        | Click                       | Redirect to cart page                                       | Pass      |

**Mobile Top Header:**
| Element                          | Action                      | Expected Result                                             | Pass/Fail |
|----------------------------------|-----------------------------|-------------------------------------------------------------|-----------|
| Search Icon Button               | Click                       | Open up search box                                          | Pass      |
| Search Box Function              | Click Search                | Error message displays                                      | Pass      |
| Search Box Function              | Enter Text and Click Search | Search both the product's title and description for a match | Pass      |
| My Account Dropdown              | Click                       | Open profile dropdown                                       | Pass      |
| Sign Up Link                     | Click                       | Redirect to Sign Up page                                    | Pass      |
|                                  | Display                     | (Not visible if user in session)                            | Pass      |
| Login Link                       | Click                       | Redirect to login page                                      | Pass      |
|                                  | Display                     | (Not visible if user in session)                            | Pass      |
| Add Product Link                 | Click                       | Redirect to add_product page                                | Pass      |
|                                  | Display                     | (Only visible if superuser in session)                      | Pass      |
| Help Center                      | Click                       | Redirect to help_center_dashboard page                      | Pass      |
|                                  | Display                     | (Only visible if superuser in session)                      | Pass      |
| My Profile Link                  | Click                       | Redirect to user profile page                               | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| My Wishlist Link                 | Click                       | Redirect to user wishlist page                              | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| My Questions Link                | Click                       | Redirect to user questions page                             | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| Logout Link                      | Click                       | Redirect to logout confirm page                             | Pass      |
|                                  | Display                     | (Only visible if user in session)                           | Pass      |
| Cart Link                        | Click                       | Redirect to cart page                                       | Pass      |

**Main Nav:**
| Element                          | Action                        | Expected Result                                                 | Pass/Fail |
|----------------------------------|-------------------------------|-----------------------------------------------------------------|-----------|
| All Products Dropdown            | Click                         | Open All Products dropdown                                      | Pass      |
| By Price Link                    | Click                         | Redirect to products page filtered by price                     | Pass      |
| By Rating Link                   | Click                         | Redirect to products page filtered by rating                    | Pass      |
| All Products Link                | Click                         | Redirect to products page                                       | Pass      |
| Brands Dropdown                  | Click                         | Open Brands dropdown                                            | Pass      |
| Marvel Link                      | Click                         | Redirect to products page filtered by marvel                    | Pass      |
| DC Comics Link                   | Click                         | Redirect to products page filtered by dc_comics                 | Pass      |
| Star Wars Link                   | Click                         | Redirect to products page filtered by star_wars                 | Pass      |
| Harry Potter Link                | Click                         | Redirect to products page filtered by harry_potter              | Pass      |
| All Brands Link                  | Click                         | Redirect to products page filtered by brands                    | Pass      |
| Clothing Dropdown                | Click                         | Open Clothing dropdown                                          | Pass      |
| New Arrivals Link                | Click                         | Redirect to products page filtered by clothing,new_arrivals     | Pass      |
| Shirts Link                      | Click                         | Redirect to products page filtered by shirts                    | Pass      |
| Sweaters Link                    | Click                         | Redirect to products page filtered by sweaters                  | Pass      |
| Hoodies Link                     | Click                         | Redirect to products page filtered by hoodies                   | Pass      |
| Jackets Link                     | Click                         | Redirect to products page filtered by jackets                   | Pass      |
| Accessories Link                 | Click                         | Redirect to products page filtered by accessories               | Pass      |
| All Clothing Link                | Click                         | Redirect to products page filtered by clothing                  | Pass      |
| Collectibles Dropdown            | Click                         | Open Collectibles dropdown                                      | Pass      |
| Marvel Link                      | Click                         | Redirect to products page filtered by collectibles,marvel       | Pass      |
| DC Comics Link                   | Click                         | Redirect to products page filtered by collectibles,dc_comics    | Pass      |
| Star Wars Link                   | Click                         | Redirect to products page filtered by collectibles,star_wars    | Pass      |
| Harry Potter Link                | Click                         | Redirect to products page filtered by collectibles,harry_potter | Pass      |
| All Collectibles Link            | Click                         | Redirect to products page filtered by collectibles              | Pass      |
| Special Offers Dropdown          | Click                         | Open Special Offers dropdown                                    | Pass      |
| New Arrivals Link                | Click                         | Redirect to products page filtered by new_arrivals              | Pass      |
| Deals Link                       | Click                         | Redirect to products page filtered by deals                     | Pass      |
| Limited Offers Link              | Click                         | Redirect to products page filtered by limited_offers            | Pass      |
| Hamburger Menu                   | Responsive                    | Display when screen size reduces to medium size                 | Pass      |
| Home Link                        | Click                         | Redirect to home                                                | Pass      |
|                                  |                               | (Only displays when screen size reduces to medium size)         | Pass      |

**Footer:**
| Element                          | Action                        | Expected Result                                                                      | Pass/Fail |
|----------------------------------|-------------------------------|--------------------------------------------------------------------------------------|-----------|
| Social Media Icon Links          | Click                         | Open correct location in new tab                                                     | Pass      |
| Newsletter Email field           | Insert incorrect/empty format | On submit: form won't submit                                                         | Pass      |
| Newsletter Email field           | Insert incorrect/empty format | Error message displays                                                               | Pass      |
| Subscribe Button                 | Click                         | Form submit                                                                          | Pass      |
| Subscribe Button                 | Click                         | Message appears saying Thank You for subscribing!                                    | Pass      |
| All Products Link                | Click                         | Redirect to products page                                                            | Pass      |
| Help Center Link                 | Click                         | Redirect to help_center page                                                         | Pass      |
| Special Offers Link              | Click                         | Redirect to products page filtered by new_arrivals,deals,limited_offers&special=true | Pass      |
| Privacy Policy Modal             | Click                         | Open Privacy Policy Modal                                                            | Pass      |
| Terms of Service Modal           | Click                         | Open Terms of Service Modal                                                          | Pass      |

### All Auth Pages

**Sign up:**
| Element                         | Action                                    | Expected Result                              | Pass/Fail |
|---------------------------------|-------------------------------------------|----------------------------------------------|-----------|
| Sign in link                    | Click                                     | Redirect to sign in page                     | Pass      |
| Email field                     | Insert incorrect format                   | On submit: form won't submit                 | Pass      |
| Email field                     | Insert incorrect format                   | Error message displays                       | Pass      |
| Email field                     | Insert correct format                     | On submit: form submit                       | Pass      |
| Email field                     | Leave empty                               | On submit: form won't submit                 | Pass      |
| Email field                     | Insert duplicate email                    | On submit: form won't submit                 | Pass      |
| Email field                     | Insert duplicate email                    | Error message displays                       | Pass      |
| Email Confirmation field        | Insert different email                    | On submit: form won't submit                 | Pass      |
| Email Confirmation field        | Insert different email                    | Error message displays                       | Pass      |
| Username field                  | Leave empty/incorrect format              | On submit: form won't submit                 | Pass      |
| Username field                  | Leave empty/incorrect format              | Error message displays                       | Pass      |
| Username field                  | Insert correct format                     | On submit: form submit                       | Pass      |
| Username field                  | Insert duplicate username                 | On submit: form won't submit                 | Pass      |
| Username field                  | Insert duplicate username                 | Error message displays                       | Pass      |
| Password field                  | Insert incorrect format/length            | On submit: form won't submit                 | Pass      |
| Password field                  | Insert incorrect format/length            | Error message displays                       | Pass      |
| Password field                  | Passwords don't match                     | On submit: form won't submit                 | Pass      |
| Password field                  | Passwords don't match                     | Error message displays                       | Pass      |
| Password field                  | Insert correct format and passwords match | On submit: form submit                       | Pass      |
| Sign Up button(form valid)      | Click                                     | Form submit                                  | Pass      |
| Sign Up button(form valid)      | Click                                     | Redirect to Verify Email Address page        | Pass      |
| Sign Up button(form valid)      | Click                                     | Alert message confirming email sent appears  | Pass      |
| Confirmation Email Confirm Link | Click                                     | Open Confirm Email Address Page              | Pass      |
| Confirm Button                  | Click                                     | Success message confirming new user appears  | Pass      |
| Confirm Button                  | Click                                     | Redirect to sign in page                     | Pass      |

**Sign in:**
| Element                         | Action                                    | Expected Result                              | Pass/Fail |
|---------------------------------|-------------------------------------------|----------------------------------------------|-----------|
| Sign up link                    | Click                                     | Redirect to sign up page                     | Pass      |
| Username field                  | Leave empty                               | On submit: form won't submit                 | Pass      |
| Username field                  | Leave empty                               | Error message displays                       | Pass      |
| Username field                  | Insert wrong username                     | On submit: form won't submit                 | Pass      |
| Username field                  | Insert wrong username                     | Error message displays                       | Pass      |
| Password field                  | Leave empty                               | On submit: form won't submit                 | Pass      |
| Password field                  | Leave empty                               | Error message displays                       | Pass      |
| Password field                  | Insert wrong password                     | On submit: form won't submit                 | Pass      |
| Password field                  | Insert wrong password                     | Error message displays                       | Pass      |
| Login button(form valid)        | Click                                     | Form submit                                  | Pass      |
| Login button(form valid)        | Click                                     | Redirect to home page                        | Pass      |
| Login button(form valid)        | Click                                     | Success message confirming login appears     | Pass      |
| Forgot Password Link            | Click                                     | Redirect to Password Reset page              | Pass      |
| Email field                     | Leave empty/incorrect format              | On submit: form submit                       | Pass      |
| Reset My Password Button        | Click                                     | Confirmation message that email sent         | Pass      |
| Password Reset Email Link       | Click                                     | Open Change Password Page                    | Pass      |
| Change Password Button          | Click                                     | Success message confirming Password Changed  | Pass      |

**Sign out:**
| Element          | Action | Expected Result                             | Pass/Fail |
|------------------|--------|---------------------------------------------|-----------|
| Sign Out  button | Click  | Redirect to homepage                        | Pass      |
| Sign Out  button | Click  | Success message confirming Sign Out appears | Pass      |

### Pages

**Home Page:**
| Element                | Action  | Expected Result                                     | Pass/Fail |
|------------------------|---------|-----------------------------------------------------|-----------|
| Carousel images        | Click   | Redirect to products page filtered by correct brand | Pass      |
| Carousel buttons       | Click   | Go back and forth through carousel images           | Pass      |
| New Arrival Section    | Display | Only displays 6 of the new_arrivals                 | Pass      |
| All New Arrivals button| Display | Redirect to products filtered by new_arrivals       | Pass      |
| New Arrival Products   | Click   | Redirect to correct product details                 | Pass      |

**Products:**
| Element                         | Action  | Expected Result                                                                     | Pass/Fail |
|---------------------------------|---------|-------------------------------------------------------------------------------------|-----------|
| Sort By' Dropdown               | Click   | Open 'sort by' options                                                              | Pass      |
| Sort By' Options (x6)           | Click   | Re-order products correctly                                                         | Pass      |
| Catergory Selected              | Display | Category label appears                                                              | Pass      |
| Product Card                    | Click   | Redirect to product detail page                                                     | Pass      |
| If Searched Product             | Display | Only display products with search term in either the product's title or description | Pass      |
| If Searched Product             | Display | Display number of products found for "searched product"                             | Pass      |
| If Searched Product             | Display | Display "Products Home" Link                                                        | Pass      |
| If Searched Product (Home Link) | Click   | Redirect to products page                                                           | Pass      |
| Back to top button              | Click   | Scrolls back to top of the page                                                     | Pass      |
| **As logged in superuser**      | ------- |                                                                                     |           |
| Edit product link               | Click   | Redirect to edit product page                                                       | Pass      |
| Delete product link             | Click   | Open delete confirmation  page                                                      | Pass      |

**Edit Product:**
| Element                       | Action           | Expected Result                                                                                                                   | Pass/Fail |
|-------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------|
| Edit Product                  | Access           | If a user tries to edit a product (by changing the url) without being signed in as superuser they are redirected to the home page | Pass      |
| Edit Product                  | Access           | An error is shown to indicate that only superusers can edit products from the store                                               | Pass      |
| Edit Product                  | Display          | Info message showing what product the superuser is currently editing appears                                                      | Pass      |
| Edit product form             | Display          | Form prefilled with previous product information                                                                                  | Pass      |
| Edit product form             | Submit           | If any required field is empty the form doesn't submit                                                                            | Pass      |
| Form Text Input (if required) | Leave blank      | On Submit: Warning appears, form won't submit                                                                                     | Pass      |
| Form Text Input (if required) | Input whitespace | On Submit: Form won't submit                                                                                                      | Pass      |
| Edit Product Form             | Display          | Thumbnail of original image is shown                                                                                              | Pass      |
| Select Image button           | Click            | Opens image selector                                                                                                              | Pass      |
| Cancel button                 | Click            | Redirect to products page                                                                                                         | Pass      |
| Update Product button         | Click            | Redirect to product detail page with all information displaying correctly                                                         | Pass      |
| Update Product button         | Click            | Success message appears informing the superuser that the product has been updated                                                 | Pass      |

**Delete Product:**
| Element                        | Action | Expected Result                                                                                                                     | Pass/Fail |
|--------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Delete Product page            | Access | If a user tries to delete a product (by changing the url) without being signed in as superuser they are redirected to the home page | Pass      |
| Delete Product page            | Access | An error is shown to indicate that only superusers can delete products from the store                                               | Pass      |
| Delete Product - cancel button | Click  | Redirect to product details page                                                                                                    | Pass      |
| Delete Product - delete button | Click  | Delete product                                                                                                                      | Pass      |
| Delete Product - delete button | Click  | Success message appears confirming product deleted successfully                                                                     | Pass      |

**Product Detail:**
| Element                      | Action                   | Expected Result                                                                | Pass/Fail |
|------------------------------|--------------------------|--------------------------------------------------------------------------------|-----------|
| Product Content              | Display                  | Display correct product image, name, price, categories, rating and description | Pass      |
| Category Links               | Click                    | Redirect to products filtered by clicked category                              | Pass      |
| Size Dropdown                | Display                  | Display if product has sizes / select M as default                             | Pass      |
| Size Dropdown                | Click                    | Change of size is possible (XS,S,M,L,XL)                                       | Pass      |
| Qty control buttons          | Click                    | Increase/decrease quantity                                                     | Pass      |
| Qty control buttons          | Click                    | Minus button disabled if quantity is 1                                         | Pass      |
| Qty control buttons          | Click                    | Plus button disabled if quantity is 49                                         | Pass      |
| Qty control buttons          | Manually Input <1 or >49 | If quantity >49 or <1 manually entered, change value to 1 / 49                 | Pass      |
| Add to cart button           | Click                    | Add item to cart                                                               | Pass      |
| Add to cart button           | Click                    | Toast Success appears                                                          | Pass      |
| Add to cart button           | Click                    | Display current cart in success message                                        | Pass      |
| Keep Shopping button         | Click                    | Redirect to products page                                                      | Pass      |
| Wishlist Heart Icon (border) | Click (logged in)        | Add item to wishlist & Redirect to users wishlist / Display success message    | Pass      |
| Wishlist Heart Icon (border) | Click (not logged in)    | Redirect to login page                                                         | Pass      |
| Wishlist Heart Icon (filled) | Click / Display          | Remove item from wishlist                                                      | Pass      |
| **As logged in superuser**   | ------------------------ |                                                                                |           |
| Edit product link            | Click                    | Redirect to edit product page                                                  | Pass      |
| Delete product link          | Click                    | Open delete confirmation  page                                                 | Pass      |

**Add Product:**
| Element                  | Action           | Expected Result                                                                                                       | Pass/Fail |
|--------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|
| Add product page         | Access           | If a user tries to add a product (by changing the url) without being a superuser they are redirected to the home page | Pass      |
| Add product page         | Access           | An error is shown to indicate that only superusers can add products to the store                                      | Pass      |
| Add product form         | Display          | Show an empty product form for the superuser to fill out                                                              | Pass      |
| Form Input (if required) | Leave blank      | On Submit: Warning appears, form won't submit                                                                         | Pass      |
| Form Input (if required) | Input whitespace | On Submit: Form won't submit                                                                                          | Pass      |
| Select Image button      | Click            | Opens image selector                                                                                                  | Pass      |
| Cancel button            | Click            | Redirect to products page                                                                                             | Pass      |
| Add Product button       | Click            | Redirect to product detail page with all information displaying correctly                                             | Pass      |
| Add Product button       | Click            | Success message appears informing the superuser that the product has been added                                       | Pass      |

**Cart:**
| Element                                            | Action             | Expected Result                                        | Pass/Fail |
|----------------------------------------------------|--------------------|--------------------------------------------------------|-----------|
| No cart items                                      | Display            | Empty cart message                                     | Pass      |
| Keep Shopping button                               | Click              | Redirect to products page                              | Pass      |
| Items in cart                                      | ------------------ |                                                        |           |
| Qty control buttons                                | Click              | Increase/decrease quantity                             | Pass      |
| Qty control buttons                                | Click              | Minus button disabled if quantity is 1                 | Pass      |
| Qty control buttons                                | Click              | Plus button disabled if quantity is 49                 | Pass      |
| Qty control buttons                                | Manually Input >49 | Automatically changes value to 49                      | Pass      |
| Qty control buttons                                | Manually Input <1  | Automatically changes value to 1                       | Pass      |
| Update button                                      | Click              | Update cart item quantity                              | Pass      |
| Update button                                      | Display            | Updated confirmation message appears                   | Pass      |
| Remove button                                      | Click              | Remove item from cart                                  | Pass      |
| Remove button                                      | Display            | Removed confirmation message appears                   | Pass      |
| Line item subtotal / cart total / delivery / total | Calculate          | All numbers are calculated correctly                   | Pass      |
| Keep shopping button                               | Click              | Redirect to products page                              | Pass      |
| Secure Checkout button                             | Click              | Redirect to checkout page                              | Pass      |

**Checkout:**
| Element                             | Action                          | Expected Result                                                    | Pass/Fail |
|-------------------------------------|---------------------------------|--------------------------------------------------------------------|-----------|
| Checkout Page                       | Direct URL input (empty bag)    | redirect to products page                                          | Pass      |
| Checkout Page                       | Direct URL input (empty bag)    | empty cart message appears                                         | Pass      |
| Form fields (if user logged in)     | On load                         | fields populated with user default info (if previously saved)      | Pass      |
| Text Input (if required)            | Leave blank                     | On submit:form won't submit                                        | Pass      |
| Text Input (if required)            | Leave blank                     | error message on invalid field(s)                                  | Pass      |
| Text Input (if required)            | Just whitespace                 | On submit:form won't submit                                        | Pass      |
| Text Input (if required)            | Just whitespace                 | error message on invalid field(s)                                  | Pass      |
| Text Input (if required)            | Fill in correctly               | On submit: form submits                                            | Pass      |
| Phone number Input                  | Leave blank                     | On submit:form won't submit                                        | Pass      |
| Phone number Input                  | Leave blank                     | error message on field                                             | Pass      |
| Phone number Input                  | Just whitespace                 | On submit:form won't submit                                        | Pass      |
| Phone number Input                  | Just whitespace                 | error message on field                                             | Pass      |
| Phone number Input                  | Use non numeric characters      | On submit:form won't submit                                        | Pass      |
| Phone number Input                  | Use non numeric characters      | error message on field                                             | Pass      |
| Email Input                         | Leave blank                     | On submit:form won't submit                                        | Pass      |
| Email Input                         | Leave blank                     | error message on field                                             | Pass      |
| Email Input                         | Just whitespace                 | On submit:form won't submit                                        | Pass      |
| Email Input                         | Just whitespace                 | error message on field                                             | Pass      |
| Email Input                         | Fill in correctly               | On submit: form submits                                            | Pass      |
| Country Dropdown                    | Click                           | Show dropdown options                                              | Pass      |
| Save to profile checkbox            | On load(user logged in)         | Shown                                                              | Pass      |
| Save to profile checkbox            | On load(user not logged in)     | Not shown                                                          | Pass      |
| Save to profile checkbox            | Checked                         | On submit:Delivery information saved to user profile               | Pass      |
| Save to profile checkbox            | Unchecked                       | On submit:Delivery information not saved to user profile           | Pass      |
| Payment card input                  | Input invalid card number       | Error message on field                                             | Pass      |
| Payment card input                  | Input invalid date              | Error message on field                                             | Pass      |
| Adjust Cart button                  | Click                           | Redirect to cart page                                              | Pass      |
| Complete Order button(form invalid) | Click                           | Form won't submit                                                  | Pass      |
| Complete Order button(form invalid) | Click                           | Error message on invalid fields                                    | Pass      |
| Complete Order button(form valid)   | Payment succeeds                | loading screen reappears                                           | Pass      |
| Complete Order button(form valid)   | Payment succeeds                | form submits                                                       | Pass      |
| Complete Order button(form valid)   | Payment succeeds                | redirect to order confirmation page                                | Pass      |
| Complete Order button(form valid)   | (if user logged in)             | order saved to user profile                                        | Pass      |
| Complete Order button(form valid)   | Payment failed                  | Loading animation appears                                          | Pass      |
| Complete Order button(form valid)   | Payment failed                  | form won't submit                                                  | Pass      |
| Complete Order button(form valid)   | Payment failed                  | error message displays                                             | Pass      |
| Complete Order button(form valid)   | Click                           | Success message appears confirming order successfully processed    | Pass      |
| Complete Order button(form valid)   | Payment Requires authentication | Authentication box appears                                         | Pass      |
| Fail Authentication button          | Click                           | Authentication box closes                                          | Pass      |
| Fail Authentication button          | Click                           | User directed back to form                                         | Pass      |
| Fail Authentication button          | Click                           | error message displays                                             | Pass      |
| Complete Authentication button      | Click                           | loading screen reappears                                           | Pass      |
| Complete Authentication button      | Click                           | form submits                                                       | Pass      |
| Complete Authentication button      | Click                           | redirect to order confirmation page                                | Pass      |
| Complete Order button(form valid)   | Click                           | Success message appears confirming order successfully processed    | Pass      |
| Complete Order button(form valid)   | Click                           | User receives an order confirmation email with correct information | Pass      |

**Checkout Success:**
| Element                  | Action  | Expected Result               | Pass/Fail |
|--------------------------|---------|-------------------------------|-----------|
| Order Confirmation       | Display | Display Correct Order Details | Pass      |
| Continue Shopping button | Click   | Redirect to products page     | Pass      |

**Profile:**
| Element                | Action            | Expected Result                                                                                                                | Pass/Fail |
|------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Open Profile page      | Access            | If a user tries to access the profile page (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Form fields            | On load           | fields populated with user default info(if previously saved)                                                                   | Pass      |
| All input fields       | Leave blank       | On submit: form submits                                                                                                        | Pass      |
| All input fields       | Just whitespace   | On submit: form submits                                                                                                        | Pass      |
| All input fields       | Fill in correctly | On submit: form submits                                                                                                        | Pass      |
| Country Dropdown       | Click             | Show dropdown options                                                                                                          | Pass      |
| Update button          | Click             | Form submits                                                                                                                   | Pass      |
| Update button          | Click             | Success message appears confirming profile successfully updated                                                                | Pass      |
| Order History          | Display           | Show order history for currently logged in account                                                                             | Pass      |
| Order Number Link      | Click             | Display order details                                                                                                          | Pass      |
| Message                | Display           | Info message appears                                                                                                           | Pass      |
| Back to Profile button | Click             | Redirect to profile page                                                                                                       | Pass      |

**My Questions:**
| Element           | Action  | Expected Result                                                                                                               | Pass/Fail |
|-------------------|---------|-------------------------------------------------------------------------------------------------------------------------------|-----------|
| My Questions page | Access  | If a user tries to access their questions (by changing the url) without being signed in they are redirected to the login page | Pass      |
| My Questions page | Display | Show current users submitted questions                                                                                        | Pass      |
| View Link         | Click   | Redirect to question # details page                                                                                           | Pass      |
| Delete Link       | Click   | Redirect to delete question # page                                                                                            | Pass      |

**My Question Details:**
| Element                 | Action  | Expected Result                                                                                             | Pass/Fail |
|-------------------------|---------|-------------------------------------------------------------------------------------------------------------|-----------|
| My Question Detail page | Access  | If a user tries to access another users question (by changing the url) they are redirected to the home page | Fail      |
| My Question Detail page | Access  | An error message is shown to indicate the user can only see their own questions                             | Fail      |
| My Question Detail page | Display | Show correct question # details                                                                             | Pass      |
| Back button             | Click   | Redirect to my questions page                                                                               | Pass      |
| Delete button           | Click   | Redirect to delete question # page                                                                          | Pass      |

**Help Center:**
| Element                  | Action           | Expected Result                                                      | Pass/Fail |
|--------------------------|------------------|----------------------------------------------------------------------|-----------|
| Help Center page         | Display          | Show question form                                                   | Pass      |
| Question form            | Display          | Show current username and disable field                              | Pass      |
| Question form Dropdown   | Display          | Show "question regarding" dropdown and select "the order" as default | Pass      |
| Form Input (if required) | Leave blank      | On Submit: Warning appears, form won't submit                        | Pass      |
| Form Input (if required) | Input whitespace | On Submit: Form won't submit                                         | Pass      |
| Keep shopping button     | Click            | Redirect to products page                                            | Pass      |
| Submit button            | Click            | Redirect to question submitted page                                  | Pass      |

**Question Submitted:**
| Element                 | Action  | Expected Result               | Pass/Fail |
|-------------------------|---------|-------------------------------|-----------|
| Question Submitted page | Display | Show submitted question       | Pass      |
| Go shopping button      | Click   | Redirect to products page     | Pass      |
| My Questions button     | Click   | Redirect to my questions page | Pass      |

**Help Center Dashboard:**
| Element               | Action  | Expected Result                                                                                                                                                | Pass/Fail |
|-----------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Help Center Dashboard | Access  | If a user tries to access the dashboard (by changing the url) without being a superuser they are redirected to the products page with an error message showing | Fail      |
| Help Center Dashboard | Access  | An error message is shown to indicate that only superusers can access the questions dashboard                                                                  | Fail      |
| Help Center Dashboard | Display | Show all users submitted questions                                                                                                                             | Pass      |
| View Link             | Click   | Redirect to question # details page                                                                                                                            | Pass      |
| Delete Link           | Click   | Redirect to delete question # page                                                                                                                             | Pass      |

**Question Details:**
| Element              | Action  | Expected Result                                                                                                                   | Pass/Fail |
|----------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------|-----------|
| Question Detail page | Access  | If a user tries to access a question (by changing the url) without being the questions owner they are redirected to the home page | Fail      |
| Question Detail page | Access  | An error message is shown to indicate the user can only see their own questions                                                   | Fail      |
| Question Detail page | Display | Show correct question # details                                                                                                   | Pass      |
| Back button          | Click   | Redirect to my questions page                                                                                                     | Pass      |
| Answer button        | Click   | Redirect to answer page                                                                                                           | Pass      |
| Delete button        | Click   | Redirect to delete question # page                                                                                                | Pass      |

**Answer Question:**
| Element                  | Action           | Expected Result                                                                                                           | Pass/Fail |
|--------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
| Answer Question page     | Access           | If a user tries to answer a question (by changing the url) without being a superuser they are redirected to the home page | Fail      |
| Answer Question page     | Access           | An error message is shown to indicate that only superusers can answer questions                                           | Fail      |
| Help Center page         | Display          | Show answer form                                                                                                          | Pass      |
| Answer form              | Display          | Show current superusername and disable field                                                                              | Pass      |
| Form Input (if required) | Leave blank      | On Submit: Warning appears, form won't submit                                                                             | Pass      |
| Form Input (if required) | Input whitespace | On Submit: Error 500                                                                                                      | Pass      |
| Back to Dashboard button | Click            | Redirect to help center dashboard                                                                                         | Pass      |
| Submit button            | Click            | Redirect to help center dashboard                                                                                         | Pass      |

**Delete Question:**
| Element         | Action | Expected Result                                                                                                                                      | Pass/Fail |
|-----------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Delete Question | Access | If a user tries to delete their question (by changing the url) without being signed in they are redirected to the login page                         | Pass      |
| Delete Question | Access | If a user tries to delete a question of another user (by changing the url) without being signed in as superuser they are redirected to the home page | Fail      |
| Delete Question | Access | An error message is shown to indicate that only superusers can delete any users question                                                             | Fail      |
| Cancel button   | Click  | Redirect to product details page                                                                                                                     | Pass      |
| Delete button   | Click  | Delete product                                                                                                                                       | Pass      |
| Delete button   | Click  | Success message appears confirming question deleted successfully                                                                                     | Pass      |

**Wishlist:**
| Element              | Action | Expected Result                                                                                                              | Pass/Fail |
|----------------------|--------|------------------------------------------------------------------------------------------------------------------------------|-----------|
| Wishlist page        | Access | If a user tries to access their wishlist (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Remove Link          | Click  | Remove that item from the wishlist                                                                                           | Pass      |
| Product Name Link    | Click  | Redirect to specific product details page                                                                                    | Pass      |
| Keep Shopping button | Click  | Success message appears confirming question deleted successfully                                                             | Pass      |

## Fixed Bugs

The buttons on the product detail page needed to be rearranged a couple of times because one of the buttons submits the form for the cart while another button is supposed to add the item to the users wishlist.

- After spending some time in tutor support we came up with a solution similar to [this](https://til.hashrocket.com/posts/v2s2gxgifj-submit-a-form-with-a-button-outside-the-form#:~:text=You%20can%20tie%20a%20submit,with%20the%20button's%20form%20property.&text=With%20this%20setup%2C%20clicking%20the,Button%20docs%20for%20more%20details). With that I could drag the "Add to Cart" button out of the form and align all buttons together.

I changed the lenght of the order number for better visibilty and ran into an error with stripe. Once I checked out stripe showed a 500 ERROR: value too long for type character varying(25).

- Since I used the exact same code for stripe as the walkthrough project I had to change the order model to return a 25 long string instead of the 32 long string.

After successfully submitting a question I wanted the question to render to the user so they can check if everything is correct, but all I got was an [empty form](https://downloads.intercomcdn.com/i/o/836802483/aa4f73174569122bc101e4a8/image.png?expires=1696272986&signature=87efa080905e3d63f364f998ec613b391bed806e12abda835f76772c4b3297bb).

- In order to fix this I first needed to make sure to check if request method is POST, to ensure the form is being submitted. After successfully saving the question using question_form.save(), I created a context dictionary containing the user's name and the created question. Then I render the "question_submitted.html" template with this context, which displays the user's name and the question.

The view should bring the user to the details of the question and if available should show the answer to it, instead I received a 404 error.

- I used get_object_or_404 in order to get the answer. If no answer exists it throws the 404 error. In order to fix this I added a try/except block, to see if an answer can be found. If not the answer is set to None so it's still defined.

## Unfixed Bugs

Pressing enter in any quantity field results in reducing the amount by one instead of updating the amount.

- This issue comes from using the IntegerField. The enter key registeres the button on the left of the quantity field and presses that button. A simple click out of the field adjusts the value already.

The cart saves if you add items to it and log in after, but it loses all content if you log out.

- I spoke with my mentor about this bug and we found that Boutique Ado had the same issue. He said, it's not a bug, it's a feature.

The date field on the questions is not accurate to the timezone the user is in.

- The date fields are stored as UTC Time and timezone support is disabled by default in the version of django I am using.
