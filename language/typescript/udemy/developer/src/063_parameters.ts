
export {};


const dP = (name: string, age: number): any => console.log({name, age});
dP('hoge',20);
//{ name: 'hoge', age: 20 }


const debugProfile = (name: string, age: number) => {
    console.log({name, age})
}
debugProfile('hoge',20);
//{ name: 'hoge', age: 20 }

type Profile = Parameters<typeof debugProfile>;
//type Profile = [name: string, age: number]

const profile: Profile = ['F', 400];

dP(...profile);
//{ name: 'F', age: 400 }