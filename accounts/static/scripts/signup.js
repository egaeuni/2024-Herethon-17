const password = document.getElementById("password1");
const confirmPassword = document.getElementById("password2");
const message = document.getElementById("message");
const submitButton = document.getElementById("submitButton");

function validatePasswords() {
  if (password.value === confirmPassword.value && password.value !== "") {
    message.style.display = "none";
    submitButton.disabled = false;
  } else {
    message.style.display = "block";
    submitButton.disabled = true;
  }
}

password.addEventListener("input", validatePasswords);
confirmPassword.addEventListener("input", validatePasswords);
