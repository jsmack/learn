export {};

type Profile = {
    name: string;
    age: number;
};

const me: Profile = {
    name: 'Tom',
    age: 50
}

me.age++;
console.log(me.age);
//51

//type PersonalDataType = {
//     readonly name: string;
//     readonly age: number;
// }
// type Readonly<T> = { readonly [P in keyof T]: T[P]; }
type PersonalDataType = Readonly<Profile>;

const friend: PersonalDataType = {
    name: 'Hanks',
    age: 11
};

// Cannot assign to 'age' because it is a read-only property.ts(2540)
// friend.age++;

