<<<<<<< HEAD
<<<<<<< HEAD
document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const correctUsername = "test";
    const correctPassword = "1234";

    if (username === correctUsername && password === correctPassword) {
      // 로그인 상태를 localStorage에 저장
      localStorage.setItem("loggedIn", "true");
      localStorage.setItem("username", username);
      console.log("로그인 성공:", username);
      window.location.href = "/html/mainpage.html";
    } else {
      document.getElementById("error-message").textContent =
        "아이디 또는 비밀번호가 올바르지 않습니다.";
    }
  });
=======
=======
>>>>>>> 800d85480886c6d9c524a3f6366d0b32c780f561
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
<<<<<<< HEAD
>>>>>>> b80f800ce6f26dd3fcbada442c3aea7fbf704b77
=======
>>>>>>> 800d85480886c6d9c524a3f6366d0b32c780f561
