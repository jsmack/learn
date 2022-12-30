export {};

let bmi: (height: number, weight: number) => number = function(
    height: number,
    weight: number
    ): number {
    return weight / ( height * height);
};
console.log(bmi(1.70, 90));


let bmi2 = (hei: number, wei: number): number => wei / ( hei * hei );
console.log(bmi2(1.70, 90));


let bmi3 = (hei2, wei2) => {
    return wei2 / ( hei2 * hei2)
};
console.log(bmi3(1.70, 90));