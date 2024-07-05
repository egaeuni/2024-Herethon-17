function togglePostList(type) {
  var list = document.getElementById(type + "-post-list");
  if (list.style.display === "none") {
    list.style.display = "block";
  } else {
    list.style.display = "none";
  }
}
