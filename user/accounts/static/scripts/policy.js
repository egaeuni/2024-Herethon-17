document.addEventListener("DOMContentLoaded", function () {
  const recent = document.getElementById("recent");
  const hot = document.getElementById("hot");
  const one = document.getElementById("one");
  const two = document.getElementById("two");
  const three = document.getElementById("three");
  const next = document.getElementById("next");
  const page = document.getElementsByClassName("page")[0];

  // 로컬 스토리지에서 정렬 기준을 읽어서 적용
  const sortBy = localStorage.getItem("sort_by");
  if (sortBy === "created_at") {
    setActiveButton(recent, hot);
  } else if (sortBy === "scrap_count") {
    setActiveButton(hot, recent);
  }

  recent.addEventListener("click", function () {
    localStorage.setItem("sort_by", "created_at");
    setActiveButton(recent, hot);
  });

  hot.addEventListener("click", function () {
    localStorage.setItem("sort_by", "scrap_count");
    setActiveButton(hot, recent);
  });

  one.addEventListener("click", function () {
    setPageButton(one, [two, three, next]);
  });

  two.addEventListener("click", function () {
    setPageButton(two, [one, three, next]);
  });

  three.addEventListener("click", function () {
    setPageButton(three, [one, two, next]);
  });

  next.addEventListener("click", function () {
    setPageButton(next, [one, two, three]);
  });

  function setActiveButton(activeBtn, inactiveBtn) {
    const activeLink = activeBtn.querySelector("a");
    const inactiveLink = inactiveBtn.querySelector("a");

    activeBtn.style.border = "1px solid #fb8129";
    activeLink.style.color = "#fb8129";
    inactiveBtn.style.border = "1px solid #eff0f1";
    inactiveLink.style.color = "black";
    // page.style.display = "none";
  }

  function setPageButton(activeBtn, inactiveBtns) {
    activeBtn.style.background = "rgb(252, 221, 205, 0.5)";
    inactiveBtns.forEach((btn) => (btn.style.background = "none"));
  }
});
