const result_btn = document.getElementsByClassName("result_btn");
const result_img = document.getElementsByClassName("result_img");

const recent = document.getElementById("recent");
const hot = document.getElementById("hot");

let recent_isClicked = false;
let hot_isClicked = false;

for (let i = 0; i < result_btn.length; i++) {
  result_btn[i].addEventListener("click", function () {
    result_img[i].src = "/img/check.png";
  });
}

document.addEventListener("DOMContentLoaded", function () {
  // 스크롤 위치 복원
  const scrollPosition = sessionStorage.getItem("scrollPosition");
  if (scrollPosition) {
    window.scrollTo(0, parseInt(scrollPosition, 10));
    sessionStorage.removeItem("scrollPosition"); // 페이지를 새로 고침할 때마다 저장된 위치가 한 번만 복원되도록 삭제
  }

  const recent = document.getElementById("recent");
  const hot = document.getElementById("hot");

  // 로컬 스토리지에서 정렬 기준을 읽어서 적용
  const sortBy = localStorage.getItem("sort");
  if (sortBy === "latest") {
    setActiveButton(recent, hot);
  } else if (sortBy === "popular") {
    setActiveButton(hot, recent);
  }

  recent.addEventListener("click", function (event) {
    localStorage.setItem("sort", "latest");
    setActiveButton(recent, hot);
  });

  hot.addEventListener("click", function (event) {
    localStorage.setItem("sort", "popular");
    setActiveButton(hot, recent);
  });

  // 스크롤 위치 저장
  window.addEventListener("beforeunload", function () {
    sessionStorage.setItem("scrollPosition", window.scrollY);
  });

  function setActiveButton(activeBtn, inactiveBtn) {
    const activeLink = activeBtn.querySelector("a");
    const inactiveLink = inactiveBtn.querySelector("a");

    activeBtn.style.border = "1px solid #fb8129";
    activeLink.style.color = "#fb8129";
    inactiveBtn.style.border = "1px solid #eff0f1";
    inactiveLink.style.color = "black";
  }
});
