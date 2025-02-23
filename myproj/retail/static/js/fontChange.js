document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.entry p').forEach(el => {
        el.style.removeProperty('font-size');
    });
});
