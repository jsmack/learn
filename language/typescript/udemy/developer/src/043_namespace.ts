export {};

namespace Japanese {
    export namespace Tokyo {
        export class Person {
            constructor(public name: string) {}
        }
    }
    export namespace Osaka {
        export class Person {
            constructor(public name: string) {}
        }
    }
}

namespace English {
    export class Person {
        constructor(
            public firstName: string, 
            public middleName: string, 
            public lastName: string
        ) {}
    }
}

const me = new Japanese.Tokyo.Person('Taro');
console.log(me.name);
//taro
const me2 = new English.Person('Tom', 'Jag', 'Hanks');
console.log(me2);
//Person { firstName: 'Tom', middleName: 'Jag', lastName: 'Hanks' }
const me3 = new Japanese.Osaka.Person('Biriken');
console.log(me3.name);
//Biriken