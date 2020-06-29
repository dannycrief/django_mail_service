$(document).ready(function showBlock() {
    const mainContent = document.querySelector('.main-content__p');
    const cardFull = document.querySelectorAll('.card-text.full');
    const lessButtons = document.querySelectorAll('.less-button');


    if (mainContent) {
        mainContent.classList.add('b-show');
        mainContent.animate(
            {marginBottom: '180px'}, 5000
        );
    }

    if (cardFull) {
        for (let i = 0; i < cardFull.length; i++) {
            cardFull[i].style.display = 'none';
            lessButtons[i].style.display = 'none';
            // if ([i].innerText.length < 27) {
            //     document.querySelector(`.more-button`).style.display = 'none';
            // }
        }
    }
});


function showMore(number) {
    document.querySelector(`.card-text.hidden.el-${number} + p`).style.display = 'none';
    document.querySelector(`.card-text.full.el-${number}`).style.display = 'block';
    document.querySelector(`.more-button.el-${number}`).style.display = 'none';
    document.querySelector(`.less-button.el-${number}`).style.display = 'block';
}

function showLess(number) {
    document.querySelector(`.card-text.hidden.el-${number} + p`).style.display = 'block';
    document.querySelector(`.card-text.full.el-${number}`).style.display = 'none';
    document.querySelector(`.more-button.el-${number}`).style.display = 'block';
    document.querySelector(`.less-button.el-${number}`).style.display = 'none';
}