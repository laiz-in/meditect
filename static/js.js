/* ===============================TO CHANGE THE BG COLOR WHEN SCROLLING=========================*/
window.addEventListener('scroll', function() {
    var header = document.querySelector('.header');
    var scrollPosition = window.scrollY;

    if (scrollPosition > 0) {
      header.classList.add('header-scrolled');
    } else {
      header.classList.remove('header-scrolled');
    }
  });

  /* ============================================================================================*/

  