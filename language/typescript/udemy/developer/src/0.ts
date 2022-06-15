export {};

type Profile = {
    name: string;
    age: number;
};

//type Partial<T> = {
//     keyof T is Tというオブジェクトの型の全てのプロパティをユニオン型として定義
//    [P in keyof T]?: T[P];
//}

type PartialProfile = Partial<Profile>;

// type PropertyTypes = "name | age"
type PropertyTypes = keyof Profile;


type Optional <T> = {
    [P in keyof T]?: T[P] 
};
type OptionalProfile = Optional<Profile>;