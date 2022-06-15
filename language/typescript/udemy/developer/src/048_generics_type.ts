export {};


// function echo4(arg4: number): number {
//     return arg4;
// };

// const echo2: (arg2: number) => number = function (
//     arg2: number
//     ): number {
//     return arg2;
// };

// const echo5: (arg5: number) => number = (
//     arg5: number
// ): number => arg5;

// const echo = (arg: number): number => {
//     return arg;
// };

// const echo3 = (arg3: null): number => arg3;

// T is abstract type
const echo = <T>(arg: T): T => {
    return arg;
};


//console.log(typeof console.log(echo('T')));
//undefined


console.log(console.log(echo<number>(100)));
//100
//undefined
console.log(console.log(echo<string>('Tom')));
//Tom
//undefined
console.log(console.log(echo<boolean>(false)));
//false
//undefined


// class Mirror {
//     constructor(public value: number) {}

//     echo(): number {
//         return this.value;
//     }
// }

// console.log(new Mirror(123))
// //Mirror { value: 123 }
// console.log(new Mirror(123).echo());

class Mirror<T> {
    constructor(public value: T) {}

    echo(): T {
        return this.value;
    }
}

console.log(new Mirror(123))
//Mirror { value: 123 }
console.log(new Mirror<number>(123).echo())
//123
console.log(new Mirror<string>("Tom!").echo())
//Tom!
console.log(typeof new Mirror<string>("Tom!").echo())
//string