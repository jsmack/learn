export {};

type Moji = string

let name: Moji = "hoge";


type Profile = {
    name: string;
    age: number
}

let example2: Profile = {
    name: 'Ham',
    age: 53
}

// 型をコピー
type Profile2 = typeof example2;