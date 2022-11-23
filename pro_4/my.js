//NAME FUNCTIONS

/*function salamu (){
    var greetings = 'Hey, habari yako';
    return greetings;
}
//salamu();
console.log(salamu())


function work (a){
    var kazi = 'I am a ' + a;
    console.log(kazi);

}
work("software engineer");


//ANONYMUS FUNCTION

var testExample = function (a,b){
    var myItems = 'Have you seen my '+ a + ' and ' + b;
    return myItems;
}

console.log(testExample('pen','book'));

var greet = function(a){
    var salamu = "Hi am " + a;
    return salamu
}
var a = 'Nduva'
console.log(greet(a))


//IMMEDIATELY INVOKED FUNCTION - angalia hiyo syntax babygirl

(function (){
    var sayhi = 'good morning';
    console.log(sayhi);
}())

//CONST
const R = 20;
console.log(R);
R = 20
console.log(R)


//OBJECT

let person = new Object();

person.name = 'Rose';
person.age = 24;
person.place = 'Malindi';
person.updateAge = function () {
    return ++person.age;
}

console.log(person.age);
person.updateAge();
console.log(person.age);

let person = {
    name: 'Rita',
    age: 20,
    place: 'Malindi',
    updateAge: function() {
        return ++person.age
    }
}
console.log(person.age);
person.updateAge();
console.log(person.age);


//-OBJECT Constructors

  //-use of this 


  // REMEMBER TO LOOK INTO THIS LADY

  class Person {
    constructor(name, place, age) {
        this.name = name;
        this.place = place;
        this.age = age;
        this.updateAge = function () {
            return ++this.age;
        };
    }
}


function Person (name,place ,age) {
    this.name = name;
    this.place = place;
    this.age = age;
    this.updateAge = function () {
        return ++this.age
    };
}

let per1 =new Person('Nduva','Ribe',17);
console.log(per1.place);*/

