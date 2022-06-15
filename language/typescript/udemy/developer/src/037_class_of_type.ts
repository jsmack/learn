
export {};

// not neeed semicoron
class Person {
    name: string;
    age: number;

    // constructor method is new auto execute method
    // type not defined because not return 
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    //method
    profile(): string {
        // format
        return `name: ${this.name}. age: ${this.age}`;
    }
}
let taro = new Person('taro', 30);
console.log(taro);
//Person { name: 'taro', age: 30 }
console.log(taro.name);
//taro
console.log(taro.age);
//30
console.log(taro.profile());
//name: taro. age: 30