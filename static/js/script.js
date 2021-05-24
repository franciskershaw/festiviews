// Existing pages
const pages = {
    add_festival: false,
    add_review: false,
    browse: false,
    edit_festival: false,
    edit_review: false,
    faq: false,
    favourites: false,
    index: false,
    login: false,
    signup: false,
    view_festival: false
}

/*
Wait for the document to load before enabling the use of the 'x' when the mobile
navbar is open, assigning 'true' to whichever page is loaded, and then finally
executing the relevant functions to that page.
*/

document.addEventListener("DOMContentLoaded", function (event) {
    // Alternates between three bars and 'x' on mobile navbar
    $('.navbar-toggler').click(function () {
        $('#navbar-open-icon').toggleClass('hide')
        $('#navbar-close-icon').toggleClass('hide')
    });

    assignPageTrue();
    
    if(pages.edit_festival || pages.edit_review) {
        populateEditForm();
    }

    if(pages.view_festival) {
        readMore();
        covidStatus();
        showRecentReviews();
    }
})

/*
This function checks which page the user is on and assigns the relevant variable
above as 'true', for when functions are only needed on certain pages.
*/

function assignPageTrue() {
    const keys = Object.keys(pages);
    const pageSectionClasses = document.querySelector('section').classList;
    keys.forEach((key) => {
        for (sectionClass of pageSectionClasses) {
            if (sectionClass === key) {
                pages[key] = true;
            }
        }
    })
}

/*
This function loops over options in select dropdowns and adds the 'selected'
attribute to the correct option when editting a form.
*/
function populateEditForm() {
    const spans = document.querySelectorAll('span');
    const options = document.querySelectorAll('option');
    for (option of options) {
        optionClass = option.classList.value;
        for (span of spans) {
            spanClass = span.classList.value;
            if (optionClass == spanClass && option.value === span.innerHTML) {
                option.setAttribute('selected', 'true');
            }
        }
    }
}

/*
This function is listening for a click event on the 'read more' button to reveal
the rest of the user submitted review on a festival's page.
*/
function readMore() {
    $('.read-more-less-btn').click(function() {
        if (this.innerHTML === 'Read More') {
            this.innerHTML = 'Read Less';
        }
        else {
            this.innerHTML = 'Read More';
        }
        $(this).closest('.review-row').toggleClass('height-100');
        $(this).parent().prev().toggleClass('ellipsis');
    })
}

/*
This function checks the covid status on a festival page and changes the colour depending on what it is
*/
function covidStatus() {
    let paragraph = document.querySelector('.covid-status');
    if (paragraph.innerHTML === 'Cancelled') {
        paragraph.classList.add('cancelled');
    } else if (paragraph.innerHTML === 'Going ahead') {
        paragraph.classList.add('going-ahead');
    }
}

/*
This function displays the 10 most recent reviews on view_festival.html
*/
function showRecentReviews() {
    let reviews = document.querySelectorAll('.review-row');
    for (let i = 0; i <= reviews.length && i < 10; i++) {
        reviews[i].classList.remove('hide');
    };
    if (reviews.length > 10) {
        showTenMore();
    }
};

/*
This function listens for a click on 'show older' button on view_festival.html
to reveal 10 further 
*/
function showTenMore() {
    console.log('function called')
    let olderButton = document.querySelector('#see-older');
    olderButton.addEventListener('click', () => {
        console.log('hi')
    })
};