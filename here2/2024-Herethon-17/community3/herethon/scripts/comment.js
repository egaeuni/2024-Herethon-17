document.addEventListener('DOMContentLoaded', function() {
    let goodCount = 0;
    let commentCount = 0;
    let scrapeCount = 0;

    const goodButton = document.querySelector('.good');
    const commentButton = document.querySelector('.comment-button');
    const scrapeButton = document.querySelector('.scrape');

    const goodCountDisplay = document.getElementById('good-count');
    const commentCountDisplay = document.getElementById('comment-count');
    const scrapeCountDisplay = document.getElementById('scrape-count');

    goodButton.addEventListener('click', function() {
        goodCount++;
        goodCountDisplay.textContent = goodCount;
    });

    commentButton.addEventListener('click', function() {
        commentCount++;
        commentCountDisplay.textContent = commentCount;
    });

    scrapeButton.addEventListener('click', function() {
        scrapeCount++;
        scrapeCountDisplay.textContent = scrapeCount;
    });
});

document.getElementById('submitComment').addEventListener('click', function() {
    // 댓글 입력창과 댓글 컨테이너 요소를 가져오기
    var commentInput = document.getElementById('commentInput');
    var commentsContainer = document.getElementById('commentsContainer');
    
    // 입력된 댓글 내용 가져오기
    var commentText = commentInput.value;
    
    // 댓글 내용이 비어 있지 않은 경우에만 추가
    if (commentText.trim() !== "") {
        // 새로운 댓글 요소 생성
        var commentElement = document.createElement('div');
        commentElement.className = 'comment';
        commentElement.textContent = commentText;

        // 댓글 컨테이너에 새로운 댓글 추가
        commentsContainer.appendChild(commentElement);

        // 입력창 초기화
        commentInput.value = '';
    } else {
        alert("댓글을 입력해주세요.");
    }
});

