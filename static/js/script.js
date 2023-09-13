function toggleActiveClass() {
  // Get all navigation links
  const navLinks = document.querySelectorAll("header nav a");

  // Remove the "active" class from all navigation links
  navLinks.forEach((navLink) => {
    navLink.classList.remove("active");
  });

  // Add the "active" class to the clicked link
  this.classList.add("active");
}

// Add a click event listener to each navigation link
document.querySelectorAll("header nav a").forEach((link) => {
  link.addEventListener("click", toggleActiveClass);
});

// Get the current URL
const currentURL = window.location.pathname;

// Get all navigation links
const navLinks = document.querySelectorAll("header nav a");

// Loop through each navigation link
navLinks.forEach((link) => {
  // Check if the current URL contains the link's href
  if (currentURL.includes(link.getAttribute("href"))) {
    // Remove "active" class from all links
    navLinks.forEach((navLink) => {
      navLink.classList.remove("active");
    });

    // Add "active" class to the link that matches the current URL
    link.classList.add("active");
  }
});

// Rest of your existing code for toggling the menu icon and scrolling sections
let menuIcon = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

menuIcon.onclick = () => {
  menuIcon.classList.toggle("bx-x");
  navbar.classList.toggle("active");
};

let sections = document.querySelectorAll("section");
let navlinks = document.querySelectorAll("header nav a");

window.onscroll = () => {
  let top = window.scrollY;

  // Check if user scrolled to the top
  if (top <= 100) {
    let header = document.querySelector("header");
    header.classList.remove("sticky");
  } else {
    let header = document.querySelector("header");
    header.classList.add("sticky");
  }

  sections.forEach((sec) => {
    let offset = sec.offsetTop - 100;
    let height = sec.offsetHeight;
    let id = sec.getAttribute("id");

    if (top >= offset && top < offset + height) {
      // active navbar links
      navlinks.forEach((links) => {
        links.classList.remove("active");
        document
          .querySelector("header nav a[href*=" + id + "]")
          .classList.add("active");
      });
    }
  });

  menuIcon.classList.remove("bx-x");
  navbar.classList.remove("active");
};
