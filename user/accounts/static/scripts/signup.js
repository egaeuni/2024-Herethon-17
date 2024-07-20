<<<<<<< HEAD
<<<<<<< HEAD
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm_password");
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
=======
=======
>>>>>>> 800d85480886c6d9c524a3f6366d0b32c780f561
document
  .getElementById("signupForm")
  .addEventListener("submit", function (event) {
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;
    var message = document.getElementById("message");

    if (password1 !== password2) {
      event.preventDefault(); // 폼 제출을 막음
      message.style.display = "block"; // 에러 메시지 표시
    } else {
      message.style.display = "none"; // 에러 메시지 숨김
    }
  });
<<<<<<< HEAD
>>>>>>> b80f800ce6f26dd3fcbada442c3aea7fbf704b77
=======
>>>>>>> 800d85480886c6d9c524a3f6366d0b32c780f561
