document.addEventListener('DOMContentLoaded', function() {
    const linkBoxes = document.querySelectorAll('.link-box');

    linkBoxes.forEach(function(box) {
        box.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
        });

        box.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1.0)';
        });
    });
});
