document.addEventListener("DOMContentLoaded", function () {
  // 페이지가 로드되면 실행될 함수
  var usernameInput = document.getElementById("username");
  var passwordInput = document.getElementById("password");

  // 입력값 초기화
  if (usernameInput) {
    usernameInput.value = "";
  }
  if (passwordInput) {
    passwordInput.value = "";
  }
});
