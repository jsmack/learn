export {};

enum Months {
    January = 1,
    February = 3,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December
}

console.log(Months.January);
console.log(Months.February);

enum COLORS {
    RED ,
    WHITE = '#FFFFFF',
    GREEN = '#008000',
    BLUE = '#0000FF',
    BLACK = '#000000',

}
console.log(COLORS.RED)
// 0
let green = COLORS.GREEN
console.log(green)
//#008000
console.log({ green })
// { green: '#008000' }

enum COLORS {
    YELLOW = '#FFFF00'
}
console.log(COLORS.YELLOW);