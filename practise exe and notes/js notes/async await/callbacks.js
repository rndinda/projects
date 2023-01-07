const posts = [
    {title:'Chapter 1',body:'This is the first chapter'},
    {title:'Chapter 2',body: 'This is my second chapter'}
];

// get a post
function getPost(){
    // mimicking fetching data annd thatcould take some time ,setTimeout takes a callback function and the delay time
    setTimeout(() => {
        // To get the post and put the on the page
        let output = '';
        posts.forEach((post, index) => {
            output += `<li>${post.title}</li>`
        });
        document.body.innerHTML = output;

    }, 1000);
}



// Create a new post
function createPost(post,callback){
    setTimeout(() => {
        posts.push(post);
        callback();
    }, 2000);
}

createPost({title:'Chapter 3',body:'This is my third chapter' }, getPost);