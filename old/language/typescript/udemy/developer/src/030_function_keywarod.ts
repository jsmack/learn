export {};

// return type is number (: number)
function bmi(height: number, weight: number): number  {
    return weight / ( height * height);
}

console.log(bmi(1.71, 90));