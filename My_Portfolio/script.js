/**
 * Portfolio JavaScript - Mahfuz Sarker Shifat
 * Python & Django Full-Stack Developer
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Navigation & Accessibility
  const menuToggle = document.getElementById('menu-toggle');
  const navLinks = document.getElementById('nav-links');
  const navBackdrop = document.getElementById('nav-backdrop');
  const navbar = document.getElementById('navbar');

  function openMenu() {
    menuToggle.classList.add('active');
    menuToggle.setAttribute('aria-expanded', 'true');
    navLinks.classList.add('open');
    navBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    menuToggle.classList.remove('active');
    menuToggle.setAttribute('aria-expanded', 'false');
    navLinks.classList.remove('open');
    navBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeMenu();
      } else {
        openMenu();
      }
    });
  }

  if (navBackdrop) {
    navBackdrop.addEventListener('click', closeMenu);
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navLinks.classList.contains('open')) {
      closeMenu();
      menuToggle.focus();
    }
  });

  const navItems = document.querySelectorAll('.nav-links a');
  navItems.forEach((link) => {
    link.addEventListener('click', () => {
      closeMenu();
    });
  });

  // 2. Header Elevation on Scroll
  function handleScrollHeader() {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleScrollHeader, { passive: true });
  handleScrollHeader();

  // 3. ScrollSpy (Active Navigation Highlighting)
  const sections = document.querySelectorAll('section[id]');
  const desktopNavLinks = document.querySelectorAll('.nav-links .nav-item');

  function updateActiveNav() {
    const scrollY = window.scrollY + 120;

    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');

      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        desktopNavLinks.forEach((link) => {
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', updateActiveNav, { passive: true });
  updateActiveNav();

  // 4. One-Click Email Copy with Toast Notification
  const copyEmailBtn = document.getElementById('copy-email-btn');
  const emailTextElem = document.getElementById('email-text');
  const toast = document.getElementById('toast');
  let toastTimer = null;

  function showToast(message) {
    if (!toast) return;
    if (message) {
      const toastSpan = toast.querySelector('span');
      if (toastSpan) toastSpan.textContent = message;
    }

    toast.classList.add('show');
    toast.setAttribute('aria-hidden', 'false');

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove('show');
      toast.setAttribute('aria-hidden', 'true');
    }, 2800);
  }

  if (copyEmailBtn && emailTextElem) {
    copyEmailBtn.addEventListener('click', async () => {
      const email = emailTextElem.textContent.trim();

      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(email);
        } else {
          const textArea = document.createElement('textarea');
          textArea.value = email;
          textArea.style.position = 'fixed';
          textArea.style.left = '-999999px';
          document.body.appendChild(textArea);
          textArea.focus();
          textArea.select();
          document.execCommand('copy');
          document.body.removeChild(textArea);
        }

        const copyText = copyEmailBtn.querySelector('.copy-text');
        const originalText = copyText ? copyText.textContent : 'Copy Email';
        
        copyEmailBtn.classList.add('copied');
        if (copyText) copyText.textContent = 'Copied!';
        showToast('Email copied to clipboard!');

        setTimeout(() => {
          copyEmailBtn.classList.remove('copied');
          if (copyText) copyText.textContent = originalText;
        }, 2200);

      } catch (err) {
        showToast('Press Ctrl+C to copy email');
      }
    });
  }
});