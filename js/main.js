document.addEventListener('DOMContentLoaded', () => {

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Scroll Progress Indicator
    const progressBar = document.getElementById('scroll-progress-container');
    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - window.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = scrolled + '%';
    });

    // Animate on Scroll (AOS)
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Apply stagger delay if it's part of a group
                if (entry.target.parentElement.classList.contains('services-grid') || 
                    entry.target.parentElement.style.display === 'grid') {
                    const children = Array.from(entry.target.parentElement.children);
                    const childIndex = children.indexOf(entry.target);
                    entry.target.style.transitionDelay = (childIndex * 0.15) + 's';
                }
                
                entry.target.classList.add('aos-animate');
                
                if (entry.target.classList.contains('counter')) {
                    startCounter(entry.target);
                }
            }
        });
    }, observerOptions);

    document.querySelectorAll('[data-aos], .counter').forEach(el => observer.observe(el));

    // Numerical Counter Animation
    function startCounter(el) {
        const target = parseInt(el.innerText);
        let count = 0;
        const duration = 2000;
        const increment = target / (duration / 16); // 16ms approx frame rate

        const updateCount = () => {
            count += increment;
            if (count < target) {
                el.innerText = Math.ceil(count) + (target > 100 ? '+' : '+');
                requestAnimationFrame(updateCount);
            } else {
                el.innerText = target + (target > 50 ? '+' : '+');
            }
        };
        updateCount();
    }

    // Smooth scroll for anchors
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Handle Mobile Logic (if added later)
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');
    const navItems = document.querySelectorAll('.nav-links li a');
    
    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.replace('fa-bars', 'fa-times');
            } else {
                icon.classList.replace('fa-times', 'fa-bars');
            }
        });
    }

    // Close mobile menu when a link is clicked
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            navLinks.classList.remove('active');
            const icon = mobileToggle.querySelector('i');
            if (icon) icon.classList.replace('fa-times', 'fa-bars');
        });
    });

});
