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