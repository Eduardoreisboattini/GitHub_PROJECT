// main.js
// Scroll to section when clicking on navigation menu links
const menuLinks = document.querySelectorAll('.menu a[href^="#"]');
menuLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      window.scrollTo({
        top: target.offsetTop,
        behavior: 'smooth'
      });
    }
  });
});

// Toggle navigation menu on small screens
const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.menu');

menuToggle.addEventListener('click', function () {
  menu.classList.toggle('show');
});

// Animation for hero section
const hero = document.querySelector('.hero');
const heroContent = document.querySelector('.hero-content');

window.addEventListener('load', function () {
  hero.classList.add('animate');
});

// Animation for course details section
const courseDetails = document.querySelector('.course-details-container');

window.addEventListener('scroll', function () {
  if (isInViewport(courseDetails)) {
    courseDetails.classList.add('animate');
  }
});

// Helper function to check if element is in viewport
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}
// main.js

// Scroll to section when clicking on navigation menu links
const menuLinks = document.querySelectorAll('.menu a[href^="#"]');
menuLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      window.scrollTo({
        top: target.offsetTop,
        behavior: 'smooth'
      });
    }
  });
});

// Toggle navigation menu on small screens
const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.menu');

menuToggle.addEventListener('click', function () {
  menu.classList.toggle('show');
});

// Animation for hero section
const hero = document.querySelector('.hero');
const heroContent = document.querySelector('.hero-content');

window.addEventListener('load', function () {
  hero.classList.add('animate');
});

// Animation for course details section
const courseDetails = document.querySelector('.course-details-container');

window.addEventListener('scroll', function () {
  if (isInViewport(courseDetails)) {
    courseDetails.classList.add('animate');
  }
});

// Helper function to check if element is in viewport
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}
