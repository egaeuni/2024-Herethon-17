document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Predefined username and password
    const correctUsername = "test"; // Replace with your desired username
    const correctPassword = "1234"; // Replace with your desired password

    if (username === correctUsername && password === correctPassword) {
      window.location.href = "mainpage.html"; // Redirect to main page
    } else {
      document.getElementById("error-message").textContent =
        "아이디 또는 비밀번호가 올바르지 않습니다.";
    }
  });
