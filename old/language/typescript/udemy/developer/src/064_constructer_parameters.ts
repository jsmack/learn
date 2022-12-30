
export {};


class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}


let taro = new Person('Taro',99);
console.log(taro);
//Person { name: 'Taro', age: 99 }


type PersonType = typeof Person;
//type PersonType = typeof Person

type Profile = ConstructorParameters<PersonType>;
//type Profile = [name: string, age: number]


const profile: Profile = ['Tom', 23];
console.log(profile);
//[ 'Tom', 23 ]

const wee = new Person(...profile);
console.log(wee);
//Person { name: 'Tom', age: 23 }