
export {};

type ObjectType =  {
    name: string;
    age: number;
};

interface ObjectInterface {
    name: string;
    age: number;
};

let object1: ObjectType = {
    name: false,
    age: 43
};

let object2: ObjectInterface = {
    name: false,
    age: 43
};
