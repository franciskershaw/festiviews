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
        noAnnouncement();
        showMoreReviews();
    }
    if(pages.view_festival || pages.browse || pages.favourites) {
        starIcons();
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
This function populates the 'notable acts' section on view_festival.html if no
acts have been added to the new festival form.
*/
function noAnnouncement() {
    let notableActs = document.querySelector('#headliners');
    if (notableActs.innerHTML === ',<br>,<br>.') {
        notableActs.innerHTML = 'No announcement yet.';
    }
} 

/*
This function listens for a click on 'show older' button on view_festival.html
to reveal 10 further reviews (if they exist).
*/
function showMoreReviews() {
    let seeOlder = document.getElementById('see-older');
    if(typeof(seeOlder) != 'undefined' && seeOlder != null) {
        seeOlder.addEventListener('click', () => {
            let hiddenReviews = document.querySelectorAll('.review-row.hide');
            for (let i = 0; i < hiddenReviews.length && i < 10; i++) {
                hiddenReviews[i].classList.remove('hide');
            };
            if (hiddenReviews.length === 0) {
                seeOlder.classList.add('hide');
            }
        })
    }
};

/*
This function checks if there is an average star rating and converts it into
star icons.
*/
function starIcons() {
    if (pages.view_festival) {
        console.log('Star rendering required on festival hub');
        let starsParagraph = document.querySelector('#average-rating');
        if (starsParagraph.innerHTML != "No ratings yet") {
            if (starsParagraph.innerHTML === "5.0") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i>'
            } else if (starsParagraph.innerHTML === "4.5") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star-half hub-star"></i>'
            } else if (starsParagraph.innerHTML === "4.0") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i>'
            } else if (starsParagraph.innerHTML === "3.5") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star-half hub-star"></i>'
            } else if (starsParagraph.innerHTML === "3.0") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i>'
            } else if (starsParagraph.innerHTML === "2.5") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i><i class="fas fa-star-half hub-star"></i>'
            } else if (starsParagraph.innerHTML === "2.0") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star hub-star"></i>'
            } else if (starsParagraph.innerHTML === "1.5") {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i><i class="fas fa-star-half hub-star"></i>'
            } else {
                starsParagraph.innerHTML = '<i class="fas fa-star hub-star"></i>'
            }
        } else {
            starsParagraph.remove();
        }
    } else {
        console.log('Star rendering required on either browse or favourites');
    };
};