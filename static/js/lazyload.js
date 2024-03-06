window.addEventListener(
  "load",
  (event) => {
    let observer = new IntersectionObserver((entries) => {
      const image = entries[0];
      if (image.isIntersecting) {
        intersected = true;
        loadImage();
        observer.disconnect();
      }
    });
  },
  false,
);

function loadImage() {
  const image = document.getElementById("lazy-image");
  image.src = image.getAttribute("data-url");
}