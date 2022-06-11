export {};


const sum: (...values: number[]) => number = (...values: number[]): number => {
    //console.log(values);
    return values.reduce(reducer);
}

const reducer = (accumulator: number, currentValue: number): number => {
    console.log({ accumulator, currentValue });
    return accumulator + currentValue;
};

sum(1,2,3,4,5);
//[ 1, 2, 3, 4, 5 ]


//[1,2,3,4].reduce(reducer);
//{ accumulator: 1, currentValue: 2 }
//{ accumulator: 3, currentValue: 3 }
//{ accumulator: 6, currentValue: 4 }

console.log(sum(1,2,3,4,5));
/*
{ accumulator: 1, currentValue: 2 }
{ accumulator: 3, currentValue: 3 }
{ accumulator: 6, currentValue: 4 }
{ accumulator: 10, currentValue: 5 }
15
//*/

const data = [1,2,3,4,5]
console.log(data.reduce(function(a,b){return a + b;}));
// 15