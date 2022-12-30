export {};
// bmi(身長、体重、console出力)
// ? optionable 

let bmi6: (heigth: number, weight: number, printable?: boolean) => void = (
    heigth: number,
    weight: number,
    printable?: boolean
): void =>  {
    const bmi: number = weight / ( heigth * heigth);
    if (printable) { 
        console.log(bmi);
    } 
}

bmi6(1.71, 90, true)
//30.778701138811947

bmi6(1.71, 90, false)
bmi6(1.71, 90)
