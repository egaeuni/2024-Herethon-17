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
