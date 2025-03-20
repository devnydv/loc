
function addShareEventListeners() {
    const shareBtns = document.querySelectorAll('.share-button');
    shareBtns.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation(); // Prevent the card click event from firing
            const url = this.dataset.url;
            if (navigator.share) {
                navigator.share({
                    title: 'Check out this new deal!',
                    url: url
                }).then(() => {
                    console.log('Thanks for sharing!');
                }).catch(console.error);
            } else {
                // Fallback for browsers that don't support the Web Share API
                const tempInput = document.createElement('input');
                document.body.appendChild(tempInput);
                tempInput.value = `https://www.lowoncost.xyz${url}`;
                tempInput.select();
                document.execCommand('copy');
                document.body.removeChild(tempInput);
                alert('Link copied to clipboard!');
            }
        });
    });
}


addShareEventListeners()