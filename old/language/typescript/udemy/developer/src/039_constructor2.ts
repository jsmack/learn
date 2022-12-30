export {};


class Person {
//    public name: string;
//    protected age: number;
//    constructor(name: string, age: number) {

    // 修飾子をつけるとauto initialize
    constructor(public name: string, protected age: number) {
//        this.name = name;
//        this.age = age;
    }
}

const me = new Person('Ham', 40);
console.log(me);
//Person { name: 'Ham', age: 40 }
console.log(me.name);
//Ham