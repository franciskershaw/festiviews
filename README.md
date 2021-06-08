# FestiViews

## Code Institute's Milestone Project 3 - Backend Development

![Hero image](static/images/amiresponsive.png)

FestiViews is an information and reviews hub created for enthusiasts of the world's greatest pastime - music festivals. Users of the site can browse, search for, and 'favourite' the music festivals of their choice in order to learn key information, such as event dates and ticket cost, as well as discovering subjective opinions displayed by other users through the uploading of a festival review (or a 'festivew' if you will). As a frequent attendee of music festivals myself, I have always felt like festival goers have been missing a convenient and modern looking place to find all the relevant information and links for several events at once, and the closest versions of this vision that currently exist are in my opinion outdated and sometimes unpleasant to use. With that in mind, my aim with this project is to lay the basic groundwork for a site that will eventually end up being a vast improvement for user experience compared to what already exists.

This project is the third of four 'milestone' projects which are required to complete the Code Institute's diploma in full stack web development. Assessment criteria for this milestone project focuses on the ability to produce a full-stack site using HTML, CSS, JavaScript, Python, Flask and MongoDB that allows users to manage a common dataset about a particular domain. As such, part of this task involves implementing CRUD (create, read, update, and delete) capabilities to the users 

You can view the live website (currently unfinished/in development) [here](https://festiviews.herokuapp.com/), and a link to the github repository can be found [here](https://github.com/franciskershaw/festiviews).

## Table of Contents
* [UX](#ux)
    * [User Stories](#user-stories)
* [Planning and Design](#planning-and-design)
    * [Strategy Plane](#strategy-plane)
    * [Scope Plane](#scope-plane)
    * [Structure Plane](#structure-plane)
    * [Skeleton Plane](#skeleton-plane)
    * [Surface Plane](#surface-plane)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
    * [Data Model](#data-model)  

  
## UX

My main goals for the creation of this website were as follows:
* To create a centralised hub of information through which the music festival community can inform themselves and leave reviews for others to consider.
* Have a website of this genre that is more aesthetically pleasing and more user friendly than the current available options.
* Demonstrate my new found backend development skills and ability to manipulate data so as to meet the pass criteria of the Code Institute for this milestone project.

### User Stories

#### Project Stakeholder/Site Developer

As the owner and developer of the site:

1. I want to produce a site where users can post, edit and browse festival reviews so that I can demonstrate my ability to implement C.R.U.D. functionality and pass this part of the course.
2. As the developer, I want the site to function exactly as intended so that only positive emotional responses are produced when interacting with the site.
3. As a bonus goal, I would like to grow the user base of the site so that the content can improve as more data is added by more and more users.

#### Users

1. As a user who wants to contribute to the site’s content, I want to be able to create a profile quickly and intuitively so that I can get started using the website.
2. As a returning user with a profile, I want to be able to sign in quickly so that I can resume my previous activities and have the option to sign out at the end of a session once I am finished.
3. As a user I want to be able to browse various festival pages so that I can find relevant information/links/reviews and help inform my decision on which festivals to attend.
4. As a user who is browsing the site, I would like to be able to sort the festivals by various relevant attributes such as alphabetical, or popularity.
5. As a user I want to search for a specific festival page (perhaps because I am already going to be attending) so that I can consume the same information as above.
6. As a user with a profile, I would like to ‘favourite’ certain festival pages so that I can view all of my favourite festivals in a convenient location.
7. As a user with a profile, I would like to be able to add reviews of the festivals I have been to before so that I can help potential future festival goers make their mind up about where to go.
8. As a user who has uploaded a festival review already, I would like to be able to edit that review so that I can add any retrospective comments or change certain of my scores if needs be.
9. As a user who has uploaded a review, I want to have the option to delete my review so that I can remove my presence on the site if I want to.
10. As a user with a profile, I would like to upvote or downvote reviews that I agree or disagree with.
11. As a user who can’t find a particular festival on the site, I would like to have a means of requesting that the festival be added.
12. As a user who might not understand intuitively how to use the site, I would like some FAQs that might explain the site’s purpose and intended use so that I can learn how to use the site.

## Planning and Design

### Strategy Plane

As with my previous projects, the **user stories** as detailed above were the very first thing I attempted to solidify during strategy sessions in order to properly focus what my priorities should be during the creation of this project. Features that were not in service of the fulfilment of the user stories were not considered during development.

The **focus** of the project is:
* Provide a centralised hub of festival-specific information for festival attendees that site users can both consume and edit/contribute to themselves, thus creating a community-powered resource that increases in quality over time.

The **business goals** of the stakeholder are:
* To have users upload as many reviews as possible and increase engagement on the site.
* Encourage users to return as and when they need festival information.
* Have a site that is more user friendly than the other available options.

*Therefore, a bespoke website using both frontend and backend technologies is required to meet the focus and business goals as it is the only way to produce a hub that is both aesthetically pleasing and contains the data manipulation features necessary to allow users to contribute and edit content themselves.*

At this stage of planning during my previous projects I would usually scour the internet for inspiration from sites that fit a similar niche to what I was trying to achive in order to get a better understanding of what features and design choices would be familiar to my userbase. However, as I've stated already, I am of the belief that the current options are not all that user friendly and as such were used more as a guide to only what I interpreted as the most important and necessary featuers for my own site.

* [eFestivals](https://www.efestivals.co.uk/) - *this site is the current leader for collated festival information, and the objectively outdated visuals on their site as well as the cognitive overload found from several unnecessary features was actually the main reason I went down this route for my project in the first place.*
* [UK Festival Guides](https://www.ukfestivalguides.com/reviews/)
* [Travel Magazine Festival Reviews](https://www.thetravelmagazine.net/festivals/festival-reviews)

Using the below importance vs viability metric, I listed out all of the opportunities on offer when building this site to help me decide what was achievable, relevant and appropriate with regard to my user stories.

| Opportunity                | Importance | Viability
| -------------------------- | ---------- |-----------
| Create account or profile  | 5          | 5
| Browse and sort festival   | 3          | 4
| Search functionality       | 4          | 3
| Add, edit, delete reviews  | 5          | 3
| Display average score      | 2          | 3
| Upvote/downvote reviews    | 2          | 3
| Favourite a festival page  | 4          | 4
| Request missing fests      | 3          | 5
| Mail list sign up          | 2          | 4
| Personalised shopping list | 1          | 2
| FAQs                       | 3          | 5
| Blog                       | 1          | 2
| Forum                      | 2          | 1
| **Total**                  | **37**     | **44**

From this helpful bit of research, I concluded that overall the opportunities on offer were mostly viable when cosidered against their relative importance to the success of the project. However, it was clear at this stage that the following opportunities should not be pursued for this iteration of the project, as a result of the combination of their poor viablity when considered against their importance to my user stories:

* Implementation of a regular blog post.
* Customised shopping list for an upcoming festival.
* Active moderated user communication forum.

### Scope Plane

Based on research and planning achieved during the strategy plane, and considering any limitations of my current coding abilities, the features I decided were critical for the completion of my user stories were as follows:

#### Required functional specifications

* Sign up/login section.
* Festival specific pages, which I will be referring to as 'hubs'.
* Favourite certain hubs which can then be viewed on a separate personal page.
* Add, edit and delete reviews that are visible on a specific festival hub.
* Search function for all festivals available to browse on the site.
* A means of requesting that a new hub be added if it doesn't already exist.
* Admin (me) with the ability to add a new festival hub directly on the site.
* FAQ section.

#### Content requirements

* Sign up needs to be easy and feedback required if incorrect details entered.
* Festival hubs must contain all the information a user would be looking for regarding a festival.
* Feedback must be given when a hub has been favourited or a review has been uploaded/edited/deleted.
* Appropriate defensive measures in place when a user is editing or deleting content.
* Confirmation required when something is being deleted.
* Search bars must work properly and be useful as opposed to a hindrance to the user experience.
* Forms must be easy to use and contain all the required fields to get a request over properly. Invalid data must be dealt with appropriately.
* FAQs must be concise and relevant.

#### Nice to haves

I felt that the scope of this project was relatively ambitious, and as a result it was hard to know exactly how long I would need to implement all the key features. With that in mind, I decided to keep a list of things that I would like to implement if possible, but that were not absolutely necessary to the completion of the project:

* Average rating of each festival based from all user reviews.
* Advanced search function which can filter out certain results based on more detailed parameters.
* Extensive bio section of each music festival appearing on each festival hub.

### Structure Plane

Based on the functional specifications and content requirements outlined during the scope plane, I decided that the following pages would be required to disperse the necessary information and features that would allow users to reach the end of their journeys.

1. **Homepage, containing:**
* Hero image of a festival crowd, with the title and tagline appearing as an overlay.
* CTA button to browse all festivals. This is a feature which can be accessed by both users who have and have not signed up for a personal account. 
* CTA button to create an account, which will not be visible if the user is logged in already.

2. **Sign up and sign in pages, containing:**
* Login or registration form, depending on which one the user needs.
* Feedback if fields are incorrectly populated.
* Option to switch from register to login, or vice versa.

3. **All festivals page, containing:**
* List of all browsable festivals uploaded by the admin user.
* Very basic visible information on each listed festival.
* Ability to sort by alphabetical order or popularity.

4. **Add new festival form (admin only), containing:**

*All required fields to create and populate the generic festival information, such as*: 
* Name, location and date of next iteration.
* Image link for hero image.
* Brief description.
* Link to important links and key information.

5. **Festival specific page (hub), containing:**
* All of the information and visuals provided by the add new festival form (admin only).
* A section to add a review, as well as view any reviews that have already been uploaded.

6. **User review form, containing:**
*All required fields to populate the review section of the festival hub, such as*:
* Year attended and overall location.
* Location, lineup, nightlife, campsites, food selection and value for money ratings out of 5.
* Family appropriateness and toilet ratings.
* Text area to add general comments.

7. **Favourites page, containing:**
* List of all festival hubs that the user has favourited.
* Heart icon that can be clicked on to remove festivals from the list.
* Message if there are no favourites, something along the lines of *'You haven't added any favourites yet, browse festivals'* or link to the login page if the user is not logged in.

8. **FAQ page, containing:**
* Collapsible FAQ sections that reveal answers beneath to questions about how the site is to be used.

#### Interaction Design

* The site needs a nonlinear structure through the use of a fixed navigation bar which allows users to choose what section of the site they can jump to.
* A consistent footer across all pages can display the logo and copyright information.
* User feedback required on all interactable content, such as: 
    * Hovered links. 
    * Underlining of current page on the navigation bar. 
    * Feedback message when a festival gets favourited and when a review gets posted, edited or deleted.
* The same colour scheme and design choices are needed across all pages to maintain consistency.
* Where applicable, content shoudl be viewable just beyond the fold so users know they can continue to scroll.

#### Information Architecture

* Tree structure can be implemented with use of the burger icon on mobile devices.
* Priority of links on the navigation bar should go from left to right.
* Priority reads as follows: logo on the far left, search bar directly in the centre, then far right navigation links are to browse all festivals, sign in/register/log out, favourites, and finally FAQ
* The most important CTAs are present on the home landing page - browse all for any user who reaches the site, and create account for anyone who is not logged in.
* Where applicable the user should not be clicking more than three times to reach the end of their user journey.

### Skeleton Plane

Low fidelity wireframes were my next step during planning of this project, and as with my previous projects I used [inVision](https://www.invisionapp.com/) to produce these. I took a conscious decision this time around to go into serious detail with these wireframes as the scope of the website is so large. This would help iron out most of the design and layout issues before coding began, and also in general would make my life a lot easier by providing a clear vision in my head of how the site should be presented.

![All wireframes](static/images/festiviews_all_wireframes.png)
![Landing wireframe](static/images/homepage_wireframe.png)
![Login/Register wireframe](static/images/login_register_wireframe.png)
![Favourites wireframe](static/images/favourites_wireframe.png)
![All festivals wireframe](static/images/all_festivals_wireframe.png)
![Add new hub wireframe](static/images/add_new_hub_wireframe.png)
![Hub wireframe](static/images/hub_wireframe.png)
![Add review wireframe](static/images/add_review_wireframe.png)
![FAQ wireframe](static/images/faq_wireframe.png)

### Surface Plane

Once the long process of wireframing was complete, I was able to concentrate fully on deciding how the look and feel of the website should appear on the front end. The following general keywords were selected to inform all decisions relating to font and typography:

* Outdoors
* Green
* Exciting
* Professional

#### Colour Scheme

I combined the key associative words with the colour pallette generator found on [Coolors](https://coolors.co/) to find the following codes for consideration during the development of the project:

* Greens: rgba(114, 156, 95, 0.9)
* General background: rgb(243, 242, 236) - this is mostly covered by background images, but is visible on the festival hubs by the reviews section.
* Darker writing to colour: #392d34
* Text colour: #fbf9ef;
* Logo and several headings: #c11e47c9

#### Typography

After deliberating between upwards of fifteen different fonts that fit the professional aesthetic planned for the site, I eventually settled on 'Nunito' from Google Fonts as this font style worked as equally well for headings and general text alike and ensured everything felt very consistent. To ensure headings stood out despite being the same font as the rest of the site's content, I tended to include a subtle text shadow.

### Data Model

#### Conceptual Design Phase

![Conceptual design model](static/images/conceptual_design.png)

#### Logical Design Phase

![Logical design model](static/images/logical_design.png)

#### Physical Design Phase

I used Mongo DB as my database management system as per the above schema.

## Bug notes

03/05/2021 - commented out code on browse.html was breaking the site and I had forgotten that jinja templating reads absolutely everything

05/05/2021 - Updating festivals was deleting all associated reviews because my edit function was adding an empty array (as per when you create a festival in the first place) to the database.

14/05/2021 - Updating festival name was throwing an error as it was trying to change the url of the festival too, initial fix was to ensure that editing a festival would not edit the URL

18/05/2021 - assignPageTrue was not working because flash messages appearing meant that they were the 'section' being targeted on the querySelector. Fixed by changing flash messsage container into a div

04/06/2021 - Appear animation on festival hubs was blocking the defensive modal for deletion of reviews, removed animation

04/06/2021 - User testing highlighted that Safari was not pulling the information in when editing reviews.

07/06/2021 - Defensive programming to stop people getting onto favourites without being logged in caused issues for sign up

## Testing document notes

* Started with the most basic version of the frontend, with forms that only had a few fields in it for convenience
* Took painstaking time first to make sure that the reviews, festivals, and users were all interacting with each other properly (like deleting a review meant it was also being deleted from the festival's document on mongoDB) before proceed with more complicated fields

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

## Photo credit notes

* Index home page hero - Thibault Trillet on Pexels
* Browse page - Nqobile Vundla on Unsplash
* Favourites/FAQ page - Tony Pham on Unsplash
* Festival hubs - google image links