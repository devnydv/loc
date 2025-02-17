let page = 2;
    const path = window.location.pathname;
    const segments = path.split('/').filter(Boolean);
    let cat = segments[1] || "all";
    let isLoading = false; // Prevent multiple requests
    
    async function loadmore() {
        if (isLoading) return; // Prevent multiple requests
        isLoading = true; 
    
        try {
            const res = await fetch(`/homepage/${page}/${cat}`, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });
    
            let data = await res.text();
            if (data !== "0") {
                let newsdiv = document.getElementById("deals-container");
                newsdiv.insertAdjacentHTML("beforeend", data);
                page++;
            } else {
                window.removeEventListener("scroll", handleScroll); // Stop listening when no more data
            }
        } catch (error) {
            console.error("Error loading more data:", error);
        }
    
        isLoading = false;
    }
    
    function handleScroll() {
        // Check if user has scrolled near the bottom (adjust threshold if needed)
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
            loadmore();
        }
    }
    
    // Attach the scroll event listener
    window.addEventListener("scroll", handleScroll);

    



    function addShareEventListeners() {
        const shareBtns = document.querySelectorAll('.share-button');
        shareBtns.forEach(btn => {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation(); // Prevent the card click event from firing
                const url = this.dataset.url;
                if (navigator.share) {
                    navigator.share({
                        title: 'Check out this news!',
                        url: url
                    }).then(() => {
                        console.log('Thanks for sharing!');
                    }).catch(console.error);
                } else {
                    // Fallback for browsers that don't support the Web Share API
                    const tempInput = document.createElement('input');
                    document.body.appendChild(tempInput);
                    tempInput.value = `https://lowoncost.vercel.app${url}`;
                    tempInput.select();
                    document.execCommand('copy');
                    document.body.removeChild(tempInput);
                    alert('Link copied to clipboard!');
                }
            });
        });
    }


    addShareEventListeners()

    document.querySelectorAll('.stat-chip').forEach(chip => {
        chip.addEventListener('click', function () {
            alert(`${this.textContent.trim()} clicked!`);
        });
    });


// old pagination system with load more button

    // let loadbut = document.getElementById("loadbut")
    // const path = window.location.pathname;
    // const segments = path.split('/').filter(Boolean);
    // let cat = segments[1]
    
    // let page = 2
    // if (cat == undefined) {
    //     cat = "all"
    // }
    // console.log(cat)
    // async function loadmore() {
        
    //     const res = await fetch(`/homepage/${page}/${cat}`, {
    //         method: 'GET',
    //         headers: { 'Content-Type': 'application/json' }, // Set the content type
            
    //     });
    //     data = await res.text()
    //     //console.log(data)
    //     if (data !== "0") {
    //         let html = data
            
    //         let newsdiv = document.getElementById("deals-container")
    //         newsdiv.insertAdjacentHTML("beforeend", html)

    //     } else {
    //         loadbut.remove()
    //     }

    //     page++
    // }