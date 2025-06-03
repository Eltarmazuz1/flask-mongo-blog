let index = 0;

function showSlide(i) {
  const slides = document.querySelectorAll(".slide");
  if (slides.length === 0) return; // No slides available
  if (i >= slides.length) index = 0;
  if (i < 0) index = slides.length - 1;
  document.querySelector(".slides").style.transform = `translateX(-${index * 100}%)`;
}

function nextSlide() {
  index++;
  showSlide(index);
}

function prevSlide() {
  index--;
  showSlide(index);
}

// Auto-slide every 10 seconds
setInterval(nextSlide, 10000);
