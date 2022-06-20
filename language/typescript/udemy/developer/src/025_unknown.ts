export {};

const func = (): number  => 43;

let numberAny: any = func();
let numberUnknown: unknown = func();

console.log(typeof numberAny);
console.log(typeof numberUnknown);

//  Operator '+' cannot be applied to types 'unknown' and '10'.ts(2365)
//let sunUnknwon = numberUnknown + 10;


// type guard
if (typeof numberUnknown == 'number') {
    let sunUnknwon = numberUnknown + 10;
    console.log(numberUnknown);
} 
