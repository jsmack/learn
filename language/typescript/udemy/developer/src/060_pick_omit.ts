
export {};

type DetailProfile = {
    name: string;
    height: number;
    weight: number;
};



type SimpleProfile = Pick<DetailProfile, 'name' | 'weight'>;
// type SimpleProfile = {
//     name: string;
//     weight: number;
// }

type SmallProfile = Omit<DetailProfile, 'height'>;
// type SmallProfile = {
//     name: string;
//     weight: number;
// }
//type Omit<T, K extends string | number | symbol> = { [P in Exclude<keyof T, K>]: T[P]; }


type MyOmit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;
type MySmallProfile = MyOmit<DetailProfile, 'height'>;



type MyOmit2<T> = Pick<T, Exclude<keyof T, 'height'>>;
type MySmallProfile2 = MyOmit2<DetailProfile>;


type MyOmit3= Pick<DetailProfile, Exclude<'name' | 'height' | 'weight', 'height'>>;
type MySmallProfile3 = MyOmit3;


type MyOmit4= Pick<DetailProfile, 'name' | 'height'>;
type MySmallProfile4 = MyOmit4;

