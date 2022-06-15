export {};

let fooCompatible: any;
let barCompatible: string = 'Type';

console.log(typeof fooCompatible);
//undefined
console.log(typeof barCompatible);
//string

fooCompatible = barCompatible;
console.log(typeof fooCompatible);
//string


let fooIncompatible: string;
let barIncompatible: number = 1;

console.log(typeof fooIncompatible);
//undefined
fooIncompatible = barCompatible;
console.log(typeof fooIncompatible);
//string

let fooString: string;
let barString: string;


fooString = barString;

let fooStringLiteral: 'fooStringLiteral' = 'fooStringLiteral';
console.log(typeof fooStringLiteral);
//string

fooString = fooStringLiteral;



interface Animal {
    age: number;
    name: string;
}

class Person {
    constructor(public age: number, public name: string) {}
}

let me: Animal;
me = new Person(40, "Tom");
