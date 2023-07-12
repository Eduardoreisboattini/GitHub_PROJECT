// JavaScript code for words animation when scrolling

window.addEventListener('DOMContentLoaded', () => {
  const animatedWords = document.querySelectorAll('.animated-word');

  function animateWords() {
    animatedWords.forEach((word) => {
      const wordTop = word.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;

      if (wordTop < windowHeight * 0.8) {
        const letters = word.textContent.split('');
        word.textContent = '';

        letters.forEach((letter, index) => {
          const span = document.createElement('span');
          span.textContent = letter;
          span.style.animationDelay = `${index * 150}ms`;
          word.append(span);
        });

       
      }
    });
  }

  window.addEventListener('scroll', animateWords);
});

