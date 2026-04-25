document.addEventListener('DOMContentLoaded', () => {

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    const isHomePage = window.location.pathname === '/' || window.location.pathname.endsWith('index.html') || window.location.pathname === '';
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else if (isHomePage) {
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
                // Apply stagger delay if it's part of a grid group
                const parent = entry.target.parentElement;
                const parentStyle = window.getComputedStyle(parent);
                if (parentStyle.display === 'grid' || parentStyle.display === 'flex') {
                    const children = Array.from(parent.children).filter(child => child.hasAttribute('data-aos') || child.classList.contains('glass-card') || child.classList.contains('project-card'));
                    const childIndex = children.indexOf(entry.target);
                    if (childIndex !== -1) {
                        entry.target.style.transitionDelay = (childIndex * 0.1) + 's';
                    }
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
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        });
    });

    // Handle incoming hash from other pages
    const handleHash = () => {
        const hash = window.location.hash;
        if (hash) {
            // Wait a bit for AOS and other layout to settle
            setTimeout(() => {
                const target = document.querySelector(hash);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'center'
                    });
                    
                    // Add highlight effect
                    target.classList.add('service-highlight');
                    
                    // Optional: Play video if it's a video card
                    const video = target.querySelector('.card-video');
                    if (video) video.play().catch(() => {});

                    // Remove highlight after animation
                    setTimeout(() => {
                        target.classList.remove('service-highlight');
                    }, 6000);
                }
            }, 500);
        }
    };

    // Check on load
    handleHash();

    // Check on hash change (if already on page)
    window.addEventListener('hashchange', handleHash);

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

    // Feature Card Mobile Touch Interaction
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('click', function() {
            // Remove active class from all other cards to ensure only one is active at a time (like hover)
            featureCards.forEach(c => {
                if(c !== this) c.classList.remove('active-touch');
            });
            // Toggle the clicked card
            this.classList.toggle('active-touch');
        });
    });
    // Service Flip Card Interaction
    const serviceCards = document.querySelectorAll('.service-detail-card');
    serviceCards.forEach(card => {
        card.addEventListener('click', function() {
            // Un-flip others
            serviceCards.forEach(c => {
                if(c !== this) c.classList.remove('active');
            });
            // Toggle this one
            this.classList.toggle('active');
        });
    });

    // Video Hover Play/Pause Logic (Desktop & Mobile)
    const videoHoverCards = document.querySelectorAll('.video-hover-card');
    videoHoverCards.forEach(card => {
        const video = card.querySelector('.card-video');
        if (video) {
            // Desktop Hover
            card.addEventListener('mouseenter', () => video.play().catch(() => {}));
            card.addEventListener('mouseleave', () => {
                video.pause();
                video.currentTime = 0;
            });

            // Mobile Touch Toggle
            card.addEventListener('touchstart', (e) => {
                if (video.paused) {
                    video.play().catch(() => {});
                    card.classList.add('touch-playing');
                } else {
                    video.pause();
                    card.classList.remove('touch-playing');
                }
            }, {passive: true});
        }
    });

    // Floating Review Us Toggle
    const reviewsSection = document.getElementById('testimonials');
    const floatingReviewBtn = document.getElementById('floating-review-trigger');
    
    if (reviewsSection && floatingReviewBtn) {
        const reviewObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    floatingReviewBtn.classList.add('show');
                } else {
                    floatingReviewBtn.classList.remove('show');
                }
            });
        }, { threshold: 0.1 });
        
        reviewObserver.observe(reviewsSection);
    }


    // --- INTERACTIVE SERVICES MARQUEE ---
    const serviceMarquee = document.querySelector('.services-marquee-section .marquee-container');
    const serviceTrack = document.querySelector('.services-marquee-section .marquee-track');

    if (serviceMarquee && serviceTrack) {
        let isInteracting = false;
        let scrollSpeed = 0.8; 
        let currentPos = serviceMarquee.scrollLeft;
        let resumeTimeout;

        // Auto-scroll animation
        const autoScroll = () => {
            if (!isInteracting) {
                currentPos += scrollSpeed;
                serviceMarquee.scrollLeft = Math.floor(currentPos);
                
                // Infinite Loop Reset
                if (serviceMarquee.scrollLeft >= serviceTrack.scrollWidth / 2) {
                    currentPos = 0;
                    serviceMarquee.scrollLeft = 0;
                }
            } else {
                // Sync currentPos when manually scrolling/dragging
                currentPos = serviceMarquee.scrollLeft;
            }
            requestAnimationFrame(autoScroll);
        };
        requestAnimationFrame(autoScroll);

        // Hover/Touch Pause Controls
        const pauseScroll = () => { isHovered = true; };
        const resumeScroll = () => {
            isHovered = false;
            isDown = false;
            currentPos = serviceMarquee.scrollLeft; // Re-sync
        };

        serviceMarquee.addEventListener('mouseenter', pauseScroll);
        serviceMarquee.addEventListener('mouseleave', resumeScroll);

        serviceMarquee.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - serviceMarquee.offsetLeft;
            scrollLeftPos = serviceMarquee.scrollLeft;
            serviceMarquee.style.cursor = 'grabbing';
        });

        window.addEventListener('mouseup', () => {
            isDown = false;
            if (serviceMarquee) serviceMarquee.style.cursor = 'grab';
        });

        window.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - serviceMarquee.offsetLeft;
            const walk = (x - startX) * 2;
            serviceMarquee.scrollLeft = scrollLeftPos - walk;
            
            if (serviceMarquee.scrollLeft <= 0) {
                serviceMarquee.scrollLeft = serviceTrack.scrollWidth / 2;
                startX = e.pageX - serviceMarquee.offsetLeft;
                scrollLeftPos = serviceMarquee.scrollLeft;
            } else if (serviceMarquee.scrollLeft >= serviceTrack.scrollWidth / 2) {
                serviceMarquee.scrollLeft = 0;
                startX = e.pageX - serviceMarquee.offsetLeft;
                scrollLeftPos = serviceMarquee.scrollLeft;
            }
        });

        // Wheel Support
        serviceMarquee.addEventListener('wheel', (e) => {
            if (isHovered) {
                if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
                    e.preventDefault();
                    serviceMarquee.scrollLeft += e.deltaY;
                } else {
                    e.preventDefault();
                    serviceMarquee.scrollLeft += e.deltaX;
                }
                
                if (serviceMarquee.scrollLeft <= 0) {
                    serviceMarquee.scrollLeft = serviceTrack.scrollWidth / 2;
                } else if (serviceMarquee.scrollLeft >= serviceTrack.scrollWidth / 2) {
                    serviceMarquee.scrollLeft = 0;
                }
                currentPos = serviceMarquee.scrollLeft;
            }
        }, { passive: false });

        // Touch Support (Mobile)
        serviceMarquee.addEventListener('touchstart', (e) => {
            isDown = true;
            isHovered = true;
            startX = e.touches[0].pageX - serviceMarquee.offsetLeft;
            scrollLeftPos = serviceMarquee.scrollLeft;
        }, { passive: true });

        serviceMarquee.addEventListener('touchend', () => {
            isDown = false;
            // Resume auto-scroll after 3 seconds of inactivity
            setTimeout(() => {
                if (!isDown) isHovered = false;
            }, 3000);
        }, { passive: true });

        serviceMarquee.addEventListener('touchmove', (e) => {
            if (!isDown) return;
            const x = e.touches[0].pageX - serviceMarquee.offsetLeft;
            const walk = (x - startX) * 1.5; 
            serviceMarquee.scrollLeft = scrollLeftPos - walk;
            
            if (serviceMarquee.scrollLeft <= 0) {
                serviceMarquee.scrollLeft = serviceTrack.scrollWidth / 2;
                startX = e.touches[0].pageX - serviceMarquee.offsetLeft;
                scrollLeftPos = serviceMarquee.scrollLeft;
            } else if (serviceMarquee.scrollLeft >= serviceTrack.scrollWidth / 2) {
                serviceMarquee.scrollLeft = 0;
                startX = e.touches[0].pageX - serviceMarquee.offsetLeft;
                scrollLeftPos = serviceMarquee.scrollLeft;
            }
            currentPos = serviceMarquee.scrollLeft;
        }, { passive: true });
    }
});
