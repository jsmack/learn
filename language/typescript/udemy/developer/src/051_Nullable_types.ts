export {};

let profile: { name: string; age: number | null} = {
    name: 'Tom',
    // error TS2322: Type 'null' is not assignable to type 'number'.
    age: null
};


//profile = null;
