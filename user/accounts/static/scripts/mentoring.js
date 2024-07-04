const result_btn = document.getElementsByClassName("result_btn");
const result_img = document.getElementsByClassName("result_img");

const recent = document.getElementById("recent");
const hot = document.getElementById("hot");
let recent_isClicked = false;
let hot_isClicked = false;

for (let i = 0; i < result_btn.length; i++) {
  result_btn[i].addEventListener("click", function () {
    result_img[i].src = "/img/check.png";
  });
}

recent.addEventListener("click", function () {
  recent_isClicked = true;
  hot_isClicked = false;

  recent.style.border = "1px solid #fb8129";
  recent.style.color = "#fb8129";
  hot.style.border = "1px solid #eff0f1";
  hot.style.color = "black";
});

hot.addEventListener("click", function () {
  hot_isClicked = true;
  recent_isClicked = false;

  hot.style.border = "1px solid #fb8129";
  hot.style.color = "#fb8129";
  recent.style.border = "1px solid #eff0f1";
  recent.style.color = "black";
});
