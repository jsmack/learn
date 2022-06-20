
export {};


function add(a: number, b: number) :number {
    return a +b;
}

let  add2: (a: number, b: number) => number = function (
    a: number,
    b: number
): number {
    return a +b;
}

let add3 = (a:number, b:number ): number => a + b;


console.log(add3(3,4));

type ReturnTypeFormAdd = ReturnType<typeof add>;
//type ReturnTypeFormAdd = number
