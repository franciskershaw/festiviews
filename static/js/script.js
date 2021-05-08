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

document.addEventListener("DOMContentLoaded", function (event) {
    // Alternates between three bars and 'x' on mobile navbar
    $('.navbar-toggler').click(function () {
        $('#navbar-open-icon').toggleClass('hide')
        $('#navbar-close-icon').toggleClass('hide')
    });

    assignPageTrue();
    
    if(pages.edit_festival === true || pages.edit_review === true) {
        populateEditForm();
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
    // const options = document.querySelectorAll('option');
    // const selections = document.querySelectorAll('.selected-option');
    // selections.forEach((selected) => {
    //     for (option of options) {
    //         if (option.value === selected.innerHTML) {
    //             option.setAttribute('selected', 'true');
    //             console.log(option.value);
    //         }
    //     }
    // })

    
    
}