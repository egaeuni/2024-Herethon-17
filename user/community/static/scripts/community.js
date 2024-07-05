function increaseCount(id) {
    const countElement = document.getElementById(id);
    let count = parseInt(countElement.textContent);
    count++;
    countElement.textContent = count;
}

