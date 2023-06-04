// var slides = document.querySelector(".slides");
// var slideWidth = document.querySelector(".slide").clientWidth;
// var currentSlide = 0;

// function showSlide(n) {
//   slides.style.transform = `translateX(-${slideWidth * n}px)`;
//   currentSlide = n;
// }

// function nextSlide() {
//   currentSlide++;
//   if (currentSlide >= slides.childElementCount) {
//     currentSlide = 0;
//   }
//   showSlide(currentSlide);
// }

// function previousSlide() {
//   currentSlide--;
//   if (currentSlide < 0) {
//     currentSlide = slides.childElementCount - 1;
//   }
//   showSlide(currentSlide);
// }

// // Mostrar el primer slide al cargar la página
// showSlide(currentSlide);

// // Cambiar al slide siguiente o anterior al presionar las teclas de flecha izquierda y derecha
// document.addEventListener("keydown", function (event) {
//   if (event.key === "ArrowLeft") {
//     previousSlide();
//   } else if (event.key === "ArrowRight") {
//     nextSlide();
//   }
// });