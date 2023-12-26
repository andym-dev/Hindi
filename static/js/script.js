// static/js/script.js
let isEnglishOnFront = true;
let currentIndex = 0;

document.addEventListener('click', function(event) {
    const clickedElement = event.target;

    if (clickedElement.classList.contains('correct-button')) {
        markCorrect();
    } else if (clickedElement.classList.contains('incorrect-button')) {
        markIncorrect();
    }
});

function toggleLanguage() {
    isEnglishOnFront = !isEnglishOnFront;
    const flashcards = document.querySelectorAll('.flashcard');

    flashcards.forEach(card => {
        const front = card.querySelector('.front');
        const back = card.querySelector('.back');

        if (isEnglishOnFront) {
            front.innerHTML = `<p>${card.dataset.english}</p>`;
            back.innerHTML = `<p>${card.dataset.hindi}</p>`;
        } else {
            front.innerHTML = `<p>${card.dataset.hindi}</p>`;
            back.innerHTML = `<p>${card.dataset.english}</p>`;
        }
    });

    const toggleButton = document.querySelector('.toggle-language button');
    toggleButton.textContent = isEnglishOnFront ? 'Hindi' : 'English';
}
