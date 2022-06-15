
export {};

// method access public private protected
// public all ok
// private only access within class
// procted access within class and subclass


// not neeed semicoron
class Person {
    public name: string;
    private age: number;
    protected nationality: string;

    // constructor method is new auto execute method
    // type not defined because not return 
    constructor(name: string, age: number, nationality: string) {
        this.name = name;
        this.age = age;
        this.nationality = nationality;
    }
    //method
    profile(): string {
        // format
        return `name: ${this.name}. age: ${this.age}`;
    }
    getter_age(): number {
        return this.age;
    }
}

class Android extends Person {
    constructor(name: string, age: number, nattionality: string) {
        // call parent same class name(constructor)
        super(name, age, nattionality);
    }
    profile(): string {
        // not use age becaouse private 
        return `name: ${this.name}, age: ${this.age}, nationality ${this.nationality}`; 
    }
}


let taro = new Person('taro', 30, 'Japan');
console.log(taro);
//Person { name: 'taro', age: 30 }
console.log(taro.name);
//taro
//console.log(taro.age);
//30
console.log(taro.getter_age())
//30

console.log(taro.profile());
//name: taro. age: 30