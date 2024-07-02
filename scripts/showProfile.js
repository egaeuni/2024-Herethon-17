const loggedIn = localStorage.getItem("loggedIn");
const username = localStorage.getItem("username");

const questionCount = localStorage.getItem("question-count");
const postCount = localStorage.getItem("post-count");
const answerCount = localStorage.getItem("answer-count");
const scrapCount = localStorage.getItem("scrap-count");

const gender = document.getElementById("gender");
const birthdate = document.getElementById("birthdate");

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
  window.location.href = "/html/mainpage.html";
});

function displayUsername() {
  const usernameElement = document.getElementById("username");
  const questionCountElement = document.getElementById("question-count");
  const postCountElement = document.getElementById("post-count");
  const answerCountElement = document.getElementById("answer-count");
  const scrapCountElement = document.getElementById("scrap-count");

  if (loggedIn === "true" && username) {
    usernameElement.textContent = username;
    questionCountElement.textContent = questionCount;
    postCountElement.textContent = postCount;
    answerCountElement.textContent = answerCount;
    scrapCountElement.textContent = scrapCount;
  } else {
    usernameElement.textContent = "사용자 이름 / 닉네임";
    questionCountElement.textContent = "-";
    postCountElement.textContent = "-";
    answerCountElement.textContent = "-";
    scrapCountElement.textContent = "-";
  }
}

// 페이지 로드 시 사용자 이름 출력
displayUsername();
