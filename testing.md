# Testing

Click [here](README.md) to return to the main project documentation.

Testing of this project was carried out through the following methods:

* Constant review during development using Gitpod's browser previewers and Chrome developer tools.
* User testing of the deployed site when close to completion.
* Manual user story testing during and after the writing of the code.
* Automated testing of the HTML and CSS files using the WC3 validators.
* Automated testing of the JavaScript and Python files using JSHINT and PEP8 using PEP8 Online.
* Automated testing of the site's accessibility using the WAVE accessibility tool.
* Automated testing of the site's general performance through Google's lighthouse feature.

As per my previous project, I attempted to stick to agile principles by using Trello to make sure that the project was first built to its most simple iteration - breaking large sections of the code to be written into sprints, with those sprints further broken up into individual tasks to be completed. Each completed task would then usually be assigned to its own git commit so that I had the option to revert to working versions of the code if my game was to break for an unknown reason.

## Table of Contents

* [Testing During Development](#testing-during-development)
   * [Browser Preview and Chrome Developer Tools](#browser-preview-and-chrome-developer-tools)
   * [Post Deployment](#post-deployment)
   * [Notable Bugs](#notable-bugs)
* [User Story Testing](#manual-user-story-testing)
* [Stakeholder Story Testing](#manual-stakeholder-testing)
* [HTML Validator](#html-validator)
* [CSS Validator](#css-validator)
* [JS Validator](#js-validator)
* [PEP8 Compliance](#pep8-compliance)
* [Accessibility Testing](#accessibility-testing)
* [Google Lighthouse](#google-lighthouse)

## Testing During Development

### Browser Preview and Chrome Developer Tools

Visuals/Responsiveness

* Testing of the front-end visuals was carried out using Gitpod's browser preview in order to make sure that elements and styles were displaying as intended.
* While on the temporary browser previews, Google Chrome's developer tools were always in use to check the responsiveness of my pages across a number of screen sizes.

Logic

Following on from my previous project, where the application of JavaScript was the main focus, I made sure I kept the same process in place when developing both the JavaScript functions and the backend logic for my site - that is to say start small and build up, making sure to check the console and print statements at all stages to ensure that the right results are being reached. Environment variables were also used and included in my .gitignore file to ensure that none of the sensitive secret keys were ever pushed to GitHub.

I started by building the most basic version of the front end, with forms containing only a few fields so that I wasn't wasting time filling out required information for submission each time I needed to test my python functions. After taking great care and plenty of time to ensure that all of my CRUD logic was working on the backend, with the adding, editing, deleting of both the festival hubs and the reviews all doing what I was expecting to the relevant MongoDB collections, did I feel more comfortable moving onto the next stage of development.

For my JavaScript, I wanted a way to make sure that only certain functions were being applied to certain pages as this would greatly help with the code formatting as would negate the need for me to create several specific JavaScript functions. To achieve this, I wrote a function that checked which page the user was on, and an *if/else* statement then applied only the relevant functions to the relevant pages.

There were inevitably several interesting bugs that needed attention, for more information please see the 'notable' bugs section below.

### Post Deployment

As this project depended almost entirely on the ability of external users being able to interact with the site through creating, reading, updating and deleting content from a common dataset, it was especially important on this project that the user testing I instigated was thorough. With that in mind, I sent the live version of the website to 15 people with the following directives, leaving out specific instructions of *how* to achieve what the site could do to check that it was intuitive enough:

1. Create an account, log out and sign back in.
2. Browse the available festivals for information and add some to favourites.
3. Remove some festivals from your favourites.
4. Add a few reviews to different festival hubs, edit one of them, and delete one.
5. Provide me with general feedback and let me know what device and browser was being used.

This very defined structure for user testing helped me focus my testers to test the integral parts of the site and answer the following questions:

1. Is my site intuitive enough to use very quickly?
2. Do all of my backend functions work outside of my own development environment and tools?
3. Is there any extra information I should be adding to my FAQ page?
4. Is there anything at all not working as it should do?

One key issue highlighted that I considered a UX issue as opposed to a code bug was the lack of information given on the sign up page as to what was allowed when choosing a username and password, as I had included a restriction to alphanumeric characters. This was amended by including small print underneath the username and password fields to clear up any confusion.

Overall though, I felt that questions 1-2 were answered with a yes as the general feedback was positive with regard to the ease of use on the site - and all of my backend functions were working exactly as I needed them to. I also didn't think I needed to add any further information to the FAQ page as there were no questions asked to me as to how the site needed to be used.

There were however a few bugs and general UX issues brought to my attention, which I will detail below.

### Notable bugs

This being my very first full stack website, there were inevitably plenty of bugs to sink my teeth into throughout development of this project, from creating the site to user testing:

#### Fixed

*Commented out jinja templating code*

My browse page was throwing an exception error without me having the faintest idea why, as I didn't see the problem being highlighted appearing anywhere on my code. It was only after a great deal of time that I was reminded that jinja templating does not ignore commented out code, and some code I'd commented out earlier to bring back later was actually causing everything to break. A frustratingly simple fix that I am now very unlikely to forget about!

*Updating festivals*

Initially when updating updating anything to do with the festival hubs, all of the reviews were being removed. This was because my edit functioning was inputting an empty array (the same as when adding a festival to begin with) instead of just leaving the reviews as they were. **This was fixed easily by removing the empty array from the edit_festival function.**

Later on, I also found issues when updating the name of the festival as it wasn't updating the URL to be that of the new festival. Initially my fix was to simply have the edit function not change the URL, but eventually I worked out that a more satisfactory fix was to **create a new_url variable at the beginning of the function, which would then be inputted to MongoDB and then used to reload the page.**

*JS function to assign certain pages as 'true' not working at various points*

As mentioned above, I wrote a function that would assign 'true' to whichever page the user was currently browsing. This appeared to be working fine, but then all of a sudden was not working as intended. After checking the developer tools, I realised that my method of assigning 'true' by locating the first section of the page (which included the name of the page as a class) was being broken by the appearance of flash messages when certain user actions were taking place. **This was fixed quite easily by changing the flash messages *section* element to a *div*.**

*Appear animation on festival hubs blocking defensive programming*

It was clear from testing that there were occasionally quite noticeable loading times for the hero images on the festival hubs. These images were pulled straight from google images via their URL, so I was unable to optimise them properly as I would do via direct upload - but I figured using the same kind of delayed entry animation as on my previous projects would help mask this. However once this was applied to the template, the bootstrap modals for deleting of reviews suddenly was not working properly as it trapped users in place on a modal that wouldn't let you quit or even proceed with deleting. This was obviously not acceptable, and I never quite worked out why this was happening within the timeframe I had available before project submission, however the fix was made **by opting to allow the minor UX issue in liew of including the appear animation on the hubs.**

#### Outstanding bugs

There were a few bugs and general UX comments that time constraints did not allow me to work on before submission. However, I am very much keen to return to this project later with a version 2 that will put all of these as top priority and will be fixed before any further features are worked on.

*Form dropdown information not being fetched when editing reviews or festivals on Safari*

This bug came out of user testing, as several of my testers are IOS users while I was primarily using Chrome and Android during development. Editing reviews, the form of which is composed mostly of dropdown menus, was not remembering the information for any dropdown information. It turns out this was because of a fix made after the HTML validator flagged an error regarding my lack of use of a default *option* element on these forms. Once I included this default option, Safari automatically would just choose this default option instead of selecting the previously submitted information. Research online showed me this was a common issue with the way Safari is set up, and the issue was not appearing on Chrome and Safari.

To ensure full cross browser compatibility on V2, this will be a high priority task in the future.

*Sort function only going from A-Z and highest-lowest on browse page*

As a bonus feature, I opted to include the ability to sort all of the festivals on browse.html by A-Z and highest to lowest rated. I initially did not even consider the idea of sorting in the other direction, however several of my user testers highlighted this as an issue. 

Due to time constraints, and the relative lack of importance of this issue to the successful completion of the project, I elected to leave this UX issue unfixed for version 1. However It will also be a high priority for version 2 of the website.

*Favouriting festivals on browse.html refreshes the page and loses pagination*

Late in development, I amended my favouriting function (called when clicking on the heart icon on various pages) to refresh the page it was on. This was because for much of the development process, this function was just direction users to their favourites page. While the function is definitely more user friendly in this stage, there is one minor inconvenience caused by it when regarding the browse page, as the pagination included to only show 10 festivals at a time is lost when refreshing the page.

This bug was inconvenient but by no means site breaking, so I elected to leave it unfixed due to the time constraints imposed by submission. As with the other minor issues, its resolution will be prioritised on V2.

*Squashed footer on android mobile (chrome) when creating an account or logging in*

It was brought to my attention that the appearance of a mobile keyboard on Chrome when using certain Android devices was pushing the footer up and squashing the content in a visually displeasing way. I believe this is due to my use of minimum *vh* as a property, with the keyboard decreasing the viewport height when it appeared. A minor issue for sure, but certainly something that would like to sort out on version 2.

## Manual User Story Testing

Testing my own user stories was carried out using the following criteria:

* The user journey must be intuitive.
* (Where applicable) the user must reach their end destination within three clicks.

### ***1. I want to be able to create a profile quickly and intuitively so that I can get started using the website.***

* The moment you arrive on the homepage, a *call to action* button appears in red to draw the user's attention straight away which says 'create account'. **1 click**

### ***2. As a returning user with a profile, I want to be able to sign in quickly so that I can resume my previous activities and have the option to sign out at the end of a session once I am finished.***

* In terms of returning to the site, if the cache has not been cleared and the user never signed out to begin with then the user remains signed in automatically. Navigation to the homepage will remove the 'create account' button entirely. If the user is not signed in, then simply navigating to the 'sign in' page via the link in the fixed navigation bar will direct them to the sign in form. **0 clicks if cache uncleared and never signed out, 1 click if returning having signed out already.**

* Once a user is signed in, the navigation bar updates from 'Sign In' to 'Sign Out', and therefore the user is able to sign out from any page they are browsing ont he site. **1 click.**

### ***3. I want to be able to browse various festival pages so that I can find relevant information/links/reviews and help inform my decision on which festivals to attend.***

* Regardless of whether the user has an account or is a casual browser, the ability to navigate to the all festivals page is available to anyone who ends up on the site. The browse all page is presented via a *call to action* button on the homepage, and is present from the navigation bar at all stages on the user's journey. Once on the browsing page, scrolling and pagination allows the user to browse as little or as many of the festival hubs as possible. **2 clicks when navigating from anywhere on the site to a festival hub, 3-4 if the user decides to 'view more' several times.**

### ***4. I would like to be able to sort festivals by various relevant attributes such as alphabetical, or pupularity.***

* When on the browse page, the user can click on the sort icons next to the name or the rating to sort as required. **2 clicks, 1 to get to the browse page from anywhere on the site, 1 to sort.**

### ***5. I want to search for a specific festival page (perhaps because I am already going to be attending) so that I can consume the same information as above.

The search bar and icon appear in the middle of the navigation bar no matter where you are on the site, and can be used to direct the user to a filtered version of the browse page that shows their results - or no results if the festival doesn't exist on the site. **1 click.**

### ***6.***

6. As a user with a profile, I would like to ‘favourite’ certain festival pages so that I can view all of my favourite festivals in a convenient location.
7. As a user with a profile, I would like to be able to add reviews of the festivals I have been to before so that I can help potential future festival goers make their mind up about where to go.
8. As a user who has uploaded a festival review already, I would like to be able to edit that review so that I can add any retrospective comments or change certain of my scores if needs be.
9. As a user who has uploaded a review, I want to have the option to delete my review so that I can remove my presence on the site if I want to.
10. As a user with a profile, I would like to upvote or downvote reviews that I agree or disagree with.
11. As a user who can’t find a particular festival on the site, I would like to have a means of requesting that the festival be added.
12. As a user who might not understand intuitively how to use the site, I would like some FAQs that might explain the site’s purpose and intended use so that I can learn how to use the site.

## Manual Stakeholder Testing

###

## HTML Validator

## CSS Validator

## JS Validator

## PEP8 Compliance

## Accessibility Testing

## Google Lighthouse

[Back to the top](#testing)

[Back to main document](README.md)



### HTML validator: 
* error thrown for not using semicolons to finish of special characters on my forms (required *), 
* space on the mailto: attribute for 'contact us', 
* warning for section lacking a header on favourites.html (ignored because 'your favourites' acts as the header), 
* heading warnings on view_festival.html (ignored because they're not needed), 
* form error on view_festival (can't have a form as child of h1) which was moved outside of the h1.
* Error on edit review and festival forms as the 'select' options didn't have placeholders as the first child with no 'value' attribute. Added the placeholders in as per the 'add review' and 'add festival' forms.

### CSS validator:
* all good

### JS linter:
* missing semicolons and unnecessary semicolons
* undefined variables (missing let)

### PEP8 online
* All good, one remaining error on gitpod linter about indentation which I deem incorrect.

### WAVE accessibility
* missing form label for search bar
* contrast error for green CTA button
* warning of redundant link from footer and main nav logo
* contrast error from 'contact us' cta on browse all
* 3 contrast errors on the festival hubs info section (external ticket links and covid 'going ahead'), 2 errors for missing header content