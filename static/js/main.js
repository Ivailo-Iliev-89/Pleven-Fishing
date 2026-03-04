document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.dropdown-toggle');

    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', function(e) {
            e.preventDefault();
            const content = this.nextElementSibling;
           
            document.querySelectorAll('.dropdown-content').forEach(el => {
                if (el !== content) el.classList.remove('show');
            });

            content.classList.toggle('show');
        });
    });

    window.onclick = function(event) {
        if (!event.target.matches('.dropdown-toggle')) {
            document.querySelectorAll('.dropdown-content').forEach(el => {
                el.classList.remove('show');
            });
        }
    }
});