let data = [
    {
        name:'Nduva',
        age: 20
    },
     {
        name:'Lucy',
        age: 40
    },
     {
        name:'Mwanyolo',
        age: 36
    },
    {
        name:'Mutheu',
        age: 21
    },
    {
        name:'Robby',
        age: 24
    },
    {
        name:'Mwende',
        age: 23
    },
    {
        name:'Rita',
        age: 25
    },
    {
        name:'Ndinda',
        age: 22
    }
]

const info = document.querySelector('#info')

let details = data.map(function(item) {
    return ('<div>' + item.name + ' '+ 'is '+ item.age +' years old'+ '</div>')
})


info.innerHTML = details.join('\n');