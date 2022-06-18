export {};

type Profile = {
    name: string;
    age: number;
    zipCode: number;
};


// type Profile2 = {
//     name?: string;
//     age?: number;
// };


// type PartialType = {
//     name?: string;
//     age?: number;
//     zipCode?: number;
// }
//Make all properties in T optional
type PartialType = Partial<Profile>;


type Profile3 = {
    name: string;
    age?: number;
    zipCode: number;
};
// type RequiredType = {
//     name: string;
//     age: number;
//     zipCode: number;
// }
//Make all properties in T required


type RequiredType = Required<Profile3>;