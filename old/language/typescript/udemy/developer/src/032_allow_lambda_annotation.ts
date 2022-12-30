export {};


let bmi4: (hei4: number, wei4: number) => number = (
    hei4: number,
    wei4: number
): number =>  wei4 / ( hei4 * hei4 );

console.log(bmi4(1.70, 90));


let bmi5 = (hei5, wei5) =>  wei5 / ( hei5 * hei5 );

console.log(bmi5(1.70, 90));