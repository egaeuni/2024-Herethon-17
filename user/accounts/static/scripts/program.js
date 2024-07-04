const submitButton = document.getElementsByClassName("submitBtn")[0];

const program_list = document.getElementById("programs");
const find_list = document.getElementById("find");

const page = document.getElementsByClassName("page")[0];

const one = document.getElementById("one");
const two = document.getElementById("two");
const three = document.getElementById("three");
const next = document.getElementById("next");

submitButton.addEventListener("click", function () {
  console.log("클릭됨");
  program_list.style.display = "none";
  find_list.style.display = "block";
  page.style.display = "none";
});

one.addEventListener("click", function () {
  one.style.background = "rgb(252, 221, 205, 0.5)";
  two.style.background = "none";
  three.style.background = "none";
  next.style.background = "none";
});

two.addEventListener("click", function () {
  one.style.background = "none";
  two.style.background = "rgb(252, 221, 205, 0.5)";
  three.style.background = "none";
  next.style.background = "none";
});

three.addEventListener("click", function () {
  one.style.background = "none";
  two.style.background = "none";
  three.style.background = "rgb(252, 221, 205, 0.5)";
  next.style.background = "none";
});

next.addEventListener("click", function () {
  one.style.background = "none";
  two.style.background = "none";
  three.style.background = "none";
  next.style.background = "rgb(252, 221, 205, 0.5)";
});
