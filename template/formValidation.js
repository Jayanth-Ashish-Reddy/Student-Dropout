// formValidation.js content
function validateForm() {
    var inputs = document.getElementsByTagName('input');
    var selects = document.getElementsByTagName('select');
    var isValid = true;

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].hasAttribute('required') && inputs[i].value.trim() === '') {
            isValid = false;
            alert('Please fill in all the required fields.');
            return false;
        }
    }

    for (var i = 0; i < selects.length; i++) {
        if (selects[i].hasAttribute('required') && selects[i].value === 'None') {
            isValid = false;
            alert('Please fill in all the required fields.');
            return false;
        }
    }

    if (isValid) {
        return true; // Proceed with form submission
    }
}
