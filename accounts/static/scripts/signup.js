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
