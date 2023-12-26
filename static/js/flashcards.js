// static/js/flashcards.js
function displayCard() {
    const flashcard = document.getElementById('flashcard');

    if (currentIndex >= 0 && currentIndex < flashcardsData.length) {
        const currentCard = flashcardsData[currentIndex];

        // Check the language toggle state and update content accordingly
        const frontContent = isEnglishOnFront ? currentCard['English'] : currentCard['Hindi'];
        const backContent = isEnglishOnFront ? currentCard['Hindi'] : currentCard['English'];

        flashcard.innerHTML = `
            <div class="flashcard ${getCardColor(currentCard['Gender'])}" 
                 data-english="${currentCard['English']}" 
                 data-hindi="${currentCard['Hindi']}">
                <div class="front">
                    <p>${frontContent}</p>
                </div>
                <div class="back">
                    <p>${backContent}</p>
                </div>
            </div>`;
        
        // Add the event listener for the flip functionality
        flashcard.querySelector('.flashcard').addEventListener('click', function() {
            this.classList.toggle('flipped');
        });
    } else {
        flashcard.innerHTML = '<p>No more flashcards</p>';
    }
}



// Add a function to determine the card color based on gender
function getCardColor(gender) {
    if (gender === 'M') {
        return 'blue';
    } else if (gender === 'F') {
        return 'pink';
    } else {
        return 'basecardcolour';
    }
}

function markCorrect() {
    console.log('Marked as Correct');
    currentIndex = (currentIndex + 1) % flashcardsData.length;
    displayCard();
}

function markIncorrect() {
    console.log('Marked as Incorrect');
    currentIndex = (currentIndex + 1) % flashcardsData.length;
    displayCard();
}

// Initial display
displayCard();
