
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

type MyReturnType<T extends (...args: any) => any> = T extends (
    ...args: any
) => infer R 
    ? R : 
    any;
// (...args: any) => any> 関数の型である制約
// inferは条件式に記載できるもの。ジェネリクス型
// 戻り値の方がRとして扱われる
// infer:推論する