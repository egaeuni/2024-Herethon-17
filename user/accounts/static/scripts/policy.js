const recent = document.getElementById("recent");
const hot = document.getElementById("hot");
let recent_isClicked = false;
let hot_isClicked = false;

// const one = document.getElementById("one");
// const two = document.getElementById("two");
// const three = document.getElementById("three");
// const next = document.getElementById("next");

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

// one.addEventListener("click", function () {
//   one.style.background = "rgb(252, 221, 205, 0.5)";
//   two.style.background = "none";
//   three.style.background = "none";
//   nextstyle.background = "none";
// });

// two.addEventListener("click", function () {
//   one.style.background = "none";
//   two.style.background = "rgb(252, 221, 205, 0.5)";
//   three.style.background = "none";
//   nextstyle.background = "none";
// });

// three.addEventListener("click", function () {
//   one.style.background = "none";
//   two.style.background = "none";
//   three.style.background = "rgb(252, 221, 205, 0.5)";
//   nextstyle.background = "none";
// });

// next.addEventListener("click", function () {
//   one.style.background = "none";
//   two.style.background = "none";
//   three.style.background = "none";
//   next.style.background = "rgb(252, 221, 205, 0.5)";
// });
