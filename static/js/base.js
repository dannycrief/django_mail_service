const mainContent = document.querySelector('.main-content__p');

$(document).ready(function showBlock() {
    if (mainContent) {
        mainContent.classList.add('b-show');

        mainContent.animate(
            {marginBottom: '180px'}, 5000
        );
    }
});