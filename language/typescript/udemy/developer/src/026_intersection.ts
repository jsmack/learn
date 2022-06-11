export {};

type Pitcher1 = {
    throwingSpeed: number;
};

type Batter1 = {
    BattingAverage: number;
};


const McG: Pitcher1 = {
    throwingSpeed: 155
};

const Murakami: Batter1 = {
    BattingAverage: 0.301
};

// type TwoWayPlayer = {
//     throwingSpeed: number;
//     BattingAverage: number;
// };

type TwoWayPlayer = Pitcher1 & Batter1;
const Ogawa: TwoWayPlayer = {
    throwingSpeed: 170,
    BattingAverage: 0.111
}

console.log(Ogawa)
// { throwingSpeed: 170, BattingAverage: 0.111 }