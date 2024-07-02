document
  .getElementById("showQuestionBtn")
  .addEventListener("click", function () {
    loadContent("/html/showQuestion.html");
  });

document.getElementById("showPostBtn").addEventListener("click", function () {
  loadContent("/html/showPost.html");
});

document.getElementById("showAnswerBtn").addEventListener("click", function () {
  loadContent("/html/showAnswer.html");
});

document.getElementById("showScrapBtn").addEventListener("click", function () {
  loadContent("/html/showScrap.html");
});

function loadContent(url) {
  fetch(url)
    .then((response) => response.text())
    .then((data) => {
      const contentDiv = document.createElement("div");
      contentDiv.innerHTML = data;
      const showProfileDiv = document.getElementById("show_selection");
      showProfileDiv.innerHTML = ""; // 기존의 내용을 지웁니다
      showProfileDiv.appendChild(contentDiv);
      showProfileDiv.classList.remove("hidden");
    })
    .catch((error) => {
      console.error("Error fetching the content:", error);
    });
}
