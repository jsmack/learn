export {};

let numbers:  number[] = [1, 2, 3];
console.log(numbers)
// not recoomended
// <> generics 型を抽象化
let numbers2: Array<number> = [1, 2, 3];
let strings2: Array<string> = ['Tokyo', 'Osaka', 'Kyoto'];

let strings: string[] = ['Type', 'Java', 'Coffee'];

let twodimensionalarray: number[][] = [
    [50, 100],
    [150, 300],
]

console.log(twodimensionalarray[0][1]);

let array2: (string | number | boolean)[] = [ 1, false, 'Java'];
