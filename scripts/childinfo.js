const gender = document.getElementById("gender");
const birthdate = document.getElementById("birthdate");

localStorage.setItem("gender", document.getElementById("gender").value);
localStorage.setItem("birthdate", document.getElementById("birthdate").value);

document.addEventListener("DOMContentLoaded", function () {
  const radioInputs = document.querySelectorAll(".radio-input");

  radioInputs.forEach(function (input) {
    input.addEventListener("change", function () {
      // Remove 'checked' class from all custom radios
      document.querySelectorAll(".radio-custom").forEach(function (custom) {
        custom.classList.remove("checked");
      });

      if (input.checked) {
        input.nextElementSibling.classList.add("checked");
      }
    });
  });
});
