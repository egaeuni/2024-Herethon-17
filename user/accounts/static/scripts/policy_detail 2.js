const scrapBtn = document.getElementById("scrap");
const scrapImg = document.getElementById("scrap_img");

let count = document.getElementById("scrapCount");

let isClicked = false;

scrapBtn.addEventListener("click", function () {
  var scrapCount = parseInt(count.innerText, 10);
  console.log("클릭되었음");
  if (isClicked) {
    scrapCount--;
    scrapImg.src = "/img/scrap.png";
  } else {
    scrapCount++;
    scrapImg.src = "/img/scrap2.png";
  }

  count.innerText = scrapCount;

  isClicked = !isClicked;
});
