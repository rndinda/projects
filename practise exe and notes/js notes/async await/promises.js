const posts = [
    {title:'Chapter 1',body:'This is the first chapter'},
    {title:'Chapter 2',body: 'This is my second chapter'}
];

// get a post
function getPost(){
    setTimeout(() => {
        
        let output = '';
        posts.forEach((post, index) => {
            output += `<li>${post.title}</li>`
        });
        document.body.innerHTML = output;

    }, 1000);
}


// function createPost(post){
//     return new Promise((resolve, reject) =>{
//         setTimeout(() => {
//             posts.push(post);
            
//             const error = false;

//             if(!error) {
//                 resolve();
//             } else {
//                 reject('Something went wrong girl!');
//             }

//         }, 2000);

//     });
   
// }
// createPost({title:'Chapter 4',body:'This is my fourth chapter'}).then(getPost);


// if error was true

function createPost(post){
    return new Promise((resolve, reject) =>{
        setTimeout(() => {
            posts.push(post);
            
            const error = true;

            if(!error) {
                resolve();
            } else {
                reject('Something went wrong girl!');
            }

        }, 2000);

    });
   
}
//createPost({title:'Chapter 4',body:'This is my fourth chapter'}).then(getPost).catch(err => console.log(err));



//Async Await

async function getUsers(){
    const response =await fetch('https://jsonplaceholder.typicode.com/users');
    const data = await response.json();

    console.log(data);
}
//getUsers()


//Promise.all

const promise1 = Promise.resolve('Good morning');
const promise2 = 14;
const promise3 = new Promise((resolve, reject) => {
    setTimeout(resolve, 2000, 'Say hello')
});

//using fetch()
const promise4 = fetch('https://jsonplaceholder.typicode.com/users').then(res => res.json());

//takes the longest promise timeout period to return everything
 //Promise.all([promise1,promise2,promise3,promise4]).then(values => console.log(values));
