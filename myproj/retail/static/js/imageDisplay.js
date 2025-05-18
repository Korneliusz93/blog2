document.addEventListener("DOMContentLoaded", function() {
    var img = document.getElementById("blog-image");
    if (img) {
        img.onerror = function() {
            var container = document.getElementById("image-container");
            if (container) {
                container.style.display = "none";
            }
        };
        img.onload = function() {
            var container = document.getElementById("image-container");
            if (container) {
                container.style.display = "block";
            }
        };
    }
});