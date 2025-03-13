document.addEventListener("DOMContentLoaded", function() {
    var img = document.getElementById("blog-image");
    img.onerror = function() {
        document.getElementById("image-container").style.display = "none";
    };
    img.onload = function() {
        document.getElementById("image-container").style.display = "block";
    };
});