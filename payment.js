// Use page.js for client-side routing
import page from 'page';

// Define routes
page('/', showHome);
page('/payment', showPayment);

// Define route handler functions
function showHome() {
    // Load and display the home page
    fetch('home.html')
        .then(response => response.text())
        .then(html => {
            document.querySelector('#content').innerHTML = html;
        });
}

function showPayment() {
    // Fetch payment.html and display it
    fetch('/payment')
        .then(response => response.text())
        .then(html => {
            document.querySelector('#content').innerHTML = html;
        });
}

// Start page.js to enable routing
page();