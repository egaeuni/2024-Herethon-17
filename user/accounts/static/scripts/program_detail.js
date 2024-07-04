const scrapBtn = document.getElementById("scrap");
const scrapImg = document.getElementById("scrap_img");

let isClicked = false;

scrapBtn.addEventListener("click", function () {
  console.log("클릭되었음");
  if (isClicked) {
    scrapImg.src = "/img/scrap.png";
  } else {
    scrapImg.src = "/img/scrap2.png";
  }

  isClicked = !isClicked;
});
