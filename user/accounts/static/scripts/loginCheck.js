<<<<<<< HEAD
// const loggedIn = localStorage.getItem("loggedIn");
// const username = localStorage.getItem("username");

// // if (loggedIn === "true") {
// //   document.getElementById("login").style.display = "none";
// //   document.getElementById("signup").style.display = "none";
// //   document.getElementById("logout").style.display = "block";
// //   console.log("로그인 된 사용자:", username);
// // } else {
// //   document.getElementById("logout").style.display = "none";
// // }

// document.getElementById("logout").addEventListener("click", function () {
//   localStorage.removeItem("loggedIn");
//   console.log("로그아웃 성공:", username);

//   window.location.href = "{% url 'mainpage' %}";
// });
=======
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
  window.location.href = "{% url 'mainpage' %}";
});
>>>>>>> 800d85480886c6d9c524a3f6366d0b32c780f561
