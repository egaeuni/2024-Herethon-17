const submitButton = document.getElementsByClassName("submitBtn")[0];

const program_list = document.getElementById("programs");
const find_list = document.getElementById("find");

const page = document.getElementsByClassName("page")[0];

submitButton.addEventListener("click", function () {
  console.log("클릭됨");
  program_list.style.display = "none";
  find_list.style.display = "block";
  page.style.display = "none";
});
