/**
 * ORYGIN Kampus — main.js
 * Scroll reveal, compteurs animés, navigation mobile
 */

"use strict";

// ─────────────────────────────────────────────
// 1. Navigation mobile
// ─────────────────────────────────────────────
const menuToggle = document.getElementById("menu-toggle");
const mobileMenu = document.getElementById("mobile-menu");
const hamburgerIcon = document.getElementById("hamburger-icon");
const closeIcon = document.getElementById("close-icon");

if (menuToggle && mobileMenu) {
  menuToggle.addEventListener("click", () => {
    const isOpen = !mobileMenu.classList.contains("hidden");

    mobileMenu.classList.toggle("hidden", isOpen);
    hamburgerIcon.classList.toggle("hidden", !isOpen);
    closeIcon.classList.toggle("hidden", isOpen);
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
  });

  // Fermer le menu au clic sur un lien
  mobileMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      mobileMenu.classList.add("hidden");
      hamburgerIcon.classList.remove("hidden");
      closeIcon.classList.add("hidden");
      menuToggle.setAttribute("aria-expanded", "false");
    });
  });
}

// ─────────────────────────────────────────────
// 2. Navbar — ombre au scroll
// ─────────────────────────────────────────────
const header = document.getElementById("main-header");

if (header) {
  const handleScroll = () => {
    header.classList.toggle("navbar-scrolled", window.scrollY > 60);
  };
  window.addEventListener("scroll", handleScroll, { passive: true });
}

// ─────────────────────────────────────────────
// 3. Scroll reveal
// ─────────────────────────────────────────────
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
);

document.querySelectorAll(".reveal, .reveal-left, .reveal-right").forEach((el) => {
  revealObserver.observe(el);
});

// ─────────────────────────────────────────────
// 4. Compteurs animés
// ─────────────────────────────────────────────
/**
 * Easing easeOutCubic pour un rendu naturel.
 * @param {number} t — progression 0…1
 * @returns {number}
 */
const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);

/**
 * Anime un compteur de 0 jusqu'à data-target.
 * @param {HTMLElement} el
 */
const animateCounter = (el) => {
  const target = parseInt(el.dataset.target, 10);
  const duration = 2000;
  let startTime = null;

  const step = (timestamp) => {
    if (!startTime) startTime = timestamp;
    const elapsed = timestamp - startTime;
    const progress = Math.min(elapsed / duration, 1);
    el.textContent = Math.floor(easeOutCubic(progress) * target);

    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      el.textContent = target;
    }
  };

  requestAnimationFrame(step);
};

const counterObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.5 }
);

document.querySelectorAll(".counter").forEach((el) => {
  counterObserver.observe(el);
});

// ─────────────────────────────────────────────
// 5. Navigation active — highlight du lien courant
// ─────────────────────────────────────────────
const sections = document.querySelectorAll("section[id], footer[id]");
const navLinks = document.querySelectorAll(".nav-link");

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        navLinks.forEach((link) => {
          const href = link.getAttribute("href");
          const isActive = href === `#${entry.target.id}`;
          link.classList.toggle("nav-active", isActive);
          link.classList.toggle("text-white/70", !isActive);
        });
      }
    });
  },
  { rootMargin: "-50% 0px -50% 0px" }
);

sections.forEach((section) => sectionObserver.observe(section));

// ─────────────────────────────────────────────
// 6. Smooth scroll pour les ancres internes
// ─────────────────────────────────────────────
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", (e) => {
    const targetId = anchor.getAttribute("href").slice(1);
    const target = document.getElementById(targetId);
    if (!target) return;

    e.preventDefault();
    const headerHeight = header ? header.offsetHeight : 80;
    const targetTop = target.getBoundingClientRect().top + window.scrollY - headerHeight;

    window.scrollTo({ top: targetTop, behavior: "smooth" });
  });
});
