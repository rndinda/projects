let searchBtn = document.querySelector('#search-btn');
let country = document.querySelector('#country');

searchBtn.addEventListener('click', () => {
    let countryName = 'Kenya';
    let finalUrl = `https://restcountries.com/v3.1/name/${countryName}?fullText=true`;
    //console.log(finalUrl);
    fetch(finalUrl).then((response) => response.json()).then((data) =>{
        console.log(data[0]);
        console.log(data[0].capital[0]);
        console.log(data[0].flags.svg);
    })
});