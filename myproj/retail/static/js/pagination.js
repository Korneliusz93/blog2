document.addEventListener('DOMContentLoaded', function() {
    const pageSize = 10; // Define the page size

    function fetchBlogEntries(page) {
        fetch(`/blog?page=${page}&page_size=${pageSize}`)
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newBlogEntries = doc.querySelector('.blog ul').innerHTML;
                const newPagination = doc.querySelector('.pagination').innerHTML;

                document.querySelector('.blog ul').innerHTML = newBlogEntries;
                document.querySelector('.pagination').innerHTML = newPagination;

                attachPaginationEventListeners();
            })
            .catch(error => console.error('Error fetching blog entries:', error));
    }

    function attachPaginationEventListeners() {
        document.querySelectorAll('.pagination a').forEach(link => {
            link.addEventListener('click', function(event) {
                event.preventDefault();
                const url = new URL(this.href, window.location.origin);
                const page = url.searchParams.get('page');
                fetchBlogEntries(page);
            });
        });
    }

    attachPaginationEventListeners();
});
