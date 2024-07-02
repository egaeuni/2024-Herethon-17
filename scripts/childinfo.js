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
