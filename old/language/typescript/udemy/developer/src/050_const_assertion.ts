export {};

// constant assertion

let name ='Tom';

name = 'Hanks';

let nickname = 'Hanks' as const;
//Type '"Free"' is not assignable to type '"Hanks"'.ts(2322)
//nickname = 'Free';
nickname = 'Hanks';

// let profile: {
//     readonly name: "Tom";
//     readonly height: 170;
// }
let profile = {
    name: 'Tom',
    height: 170
} as const;

//Cannot assign to 'name' because it is a read-only property.ts(2540)
//profile.name = 'Hanks';

//Cannot assign to 'height' because it is a read-only property.ts(2540)
//profile.height = 190;