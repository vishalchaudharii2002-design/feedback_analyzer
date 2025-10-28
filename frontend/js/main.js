function showPage(pageId, context = {}){
    if (pageId === 'upload'){
        window.location.href = 'upload.html'
    }
    else if(pageId === 'status'){
        window.location.href = 'status.html'
    }
    else if(pageId === 'home'){
        window.location.href = 'index.html'
    }
    else{
        window.location.href = 'analytics.html'
    }

}