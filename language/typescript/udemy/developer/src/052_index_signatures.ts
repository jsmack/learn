export {};

interface Profile {
    name: string;
    underTwenty: boolean;
    [index: string]: string | number | boolean;
}

let profile: Profile = { name: 'Tom', underTwenty: false};

// How to write index signatures
// { [ index: typeForIndex ]: typeForValue}
profile.name = 'Tom';
profile.age = 43;
profile.nationality = 'Japan';