const loggedIn = localStorage.getItem("loggedIn");
const username = localStorage.getItem("username");

if (loggedIn === "true") {
  document.getElementById("login").style.display = "none";
  document.getElementById("signup").style.display = "none";
  document.getElementById("logout").style.display = "block";
  console.log("로그인 된 사용자:", username);
} else {
  document.getElementById("logout").style.display = "none";
}

document.getElementById("logout").addEventListener("click", function () {
  localStorage.removeItem("loggedIn");
  console.log("로그아웃 성공:", username);
<<<<<<< HEAD
  window.location.href = "/html/mainpage.html";
=======
  window.location.href = "{% url 'mainpage' %}";
>>>>>>> b80f800ce6f26dd3fcbada442c3aea7fbf704b77
});
